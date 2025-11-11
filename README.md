# 🔐 API-ESCOLA com DjangoRestFramework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)

API de uma escola desenvolvida com **DjangoRestFramework** que permite acessar e adicionar **cursos** , **estudantes** e **matriculas**! Porém para conseguir adicionar algo é necessário ter um superuser!

---

## 🚀 Tecnologias utilizadas
- **Python 3.10+**
- **Django 4.x**
- **Docker desktop**
- **WSL**

---

## 📦 Pré-requisitos
- [Python 3.10 ou 3.11](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

---
## ⚙️ Instalação e configuração

### 1️⃣ Clonar o repositório

`git clone https://github.com/matheusroberto04/API-ESCOLA.git`

### 2️⃣ Criar e ativar o ambiente virtual

Instale primeiro o módulo da virtualenv com o seguinte comando:

`pip install virtualenv`

Depois crie a virtualenv e dê um nome para ela ( nome padrão é venv)

`python -m virtualenv .venv`

# Windows (PowerShell)

`.venv\Scripts\Activate.ps1`

# Linux/Mac

`source .venv/bin/activate`

### 3️⃣ Instalar dependências

Para instalar as dependências use o seguinte comando:

`pip install -r requirements.txt`

### 4️⃣ Aplicar migrations

`python manage.py makemigrations`
`python manage.py migrate`

### 5️⃣ Rodar o servidor

`python manage.py runserver`

### 6️⃣ Script para Popular o Banco de Dados

`python popular_banco_cursos.py`
`python popular_banco_estudantes.py`
