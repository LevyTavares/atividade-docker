# 🚀 Aplicação Fullstack: Gestão de Produtos com FastAPI e Docker

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

Este projeto foi desenvolvido como resolução da atividade **[ATV-01] Praticando Docker-Compose**, mas expandido para incluir uma interface gráfica de usuário (Front-end) e pipeline de CI/CD.

## 🎯 O que este projeto faz?
É uma aplicação completa para gerenciamento de produtos. Conta com um Front-end interativo em HTML/JS que se comunica perfeitamente com uma API RESTful em FastAPI, utilizando PostgreSQL para persistência e Redis para cache de alta velocidade.

### ✨ Funcionalidades e Bônus Implementados:
- **Interface Gráfica (Novo):** Tela amigável servida diretamente pela API para cadastrar e visualizar produtos em tempo real.
- **Banco de Dados Relacional:** Dados salvos de forma segura no PostgreSQL.
- **Cache Inteligente (Bônus):** Integração com **Redis** para armazenar a listagem de produtos, com indicador visual no Front-end mostrando se a resposta veio do Banco ou do Cache.
- **Orquestração Completa:** Todo o ecossistema (API, Front, Banco e Cache) sobe com um único comando via `docker compose`.
- **Integração Contínua (CI):** Pipeline configurada com **GitHub Actions** para rodar testes automatizados a cada novo push, garantindo a estabilidade da aplicação.

---

## 🛠️ Tecnologias Utilizadas

* **Front-end:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Back-end:** Python 3.11 + FastAPI
* **Banco de Dados:** PostgreSQL 15
* **Cache:** Redis Alpine
* **Infraestrutura:** Docker & Docker Compose
* **Qualidade de Código:** Pytest + GitHub Actions

---

## ⚙️ Como executar o projeto localmente

### Pré-requisitos
Ter o [Docker](https://www.docker.com/products/docker-desktop) instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO