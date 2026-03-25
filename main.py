from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import redis
import json

app = FastAPI()

DB_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

cache = redis.from_url(REDIS_URL, decode_responses=True)

def get_db_connection():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

@app.on_event("startup")
def startup_event():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.get("/")
def mostrar_pagina_inicial():
    return FileResponse("index.html")

@app.get("/health")
def health_check():
    return {"status": "ok", "mensagem": "API, Banco e Cache funcionando!"}

@app.post("/produtos")
def criar_produto(nome: str, preco: float):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s) RETURNING id, nome, preco",
        (nome, preco)
    )
    novo_produto = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    cache.delete("produtos_lista")
    
    return {"mensagem": "Produto criado", "produto": novo_produto}

@app.get("/produtos")
def listar_produtos():
    produtos_cacheados = cache.get("produtos_lista")
    if produtos_cacheados:
        return {"origem": "REDIS (Cache)", "produtos": json.loads(produtos_cacheados)}

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    conn.close()

    produtos_formatados = jsonable_encoder(produtos)

    cache.set("produtos_lista", json.dumps(produtos_formatados), ex=60)

    return {"origem": "POSTGRESQL (Banco)", "produtos": produtos_formatados}