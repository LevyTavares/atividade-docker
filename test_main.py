from fastapi.testclient import TestClient
from main import app

# Cria um cliente de teste que simula um navegador/usuário acedendo à API
client = TestClient(app)

def test_health_check():
    # Fazemos uma requisição GET à rota /health
    response = client.get("/health")
    
    # Verificamos se o status HTTP é 200 (Sucesso)
    assert response.status_code == 200
    
    # Verificamos se a mensagem retornada é a que esperamos
    assert response.json() == {"status": "ok", "mensagem": "API, Banco e Cache funcionando!"}