# 🚀 API de Produtos com FastAPI, PostgreSQL e Redis

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

Este projeto foi desenvolvido como resolução da atividade **[ATV-01] Praticando Docker-Compose**. O objetivo principal é criar um ambiente completo de desenvolvimento backend utilizando múltiplos serviços orquestrados via Docker.

## 🎯 O que este projeto faz?
É uma API RESTful simples para gerenciamento de produtos. A aplicação permite cadastrar novos produtos no banco de dados e listá-los, utilizando um sistema de cache inteligente para otimizar as consultas.

### ✨ Funcionalidades e Bônus Implementados:
- **CRUD Básico:** Rotas para criar e listar produtos.
- **Banco de Dados Relacional:** Dados persistidos de forma segura no PostgreSQL.
- **Cache de Alta Performance (Bônus):** Integração com **Redis** para armazenar a listagem de produtos por 60 segundos, reduzindo a carga no banco de dados.
- **Orquestração de Containers:** Todo o ambiente (API, Banco e Cache) sobe com um único comando usando `docker-compose`.
- **Integração Contínua (CI):** Pipeline configurada com **GitHub Actions** para rodar testes automatizados a cada novo push.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.11 + FastAPI
* **Banco de Dados:** PostgreSQL 15
* **Cache:** Redis Alpine
* **Infraestrutura:** Docker & Docker Compose
* **Testes & CI/CD:** Pytest + GitHub Actions

---

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
Você precisará ter o [Docker](https://www.docker.com/products/docker-desktop) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO