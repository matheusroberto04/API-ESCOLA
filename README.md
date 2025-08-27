# 🎓 School API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

API desenvolvida com Django e Django Rest Framework para gerenciamento de estudantes e seus cursos.
Permite realizar operações de CRUD (Create, Read, Update, Delete) e expõe endpoints organizados para integração com outros sistemas.

## 🚀 Tecnologias utilizadas

Python 3.12.2+

Django 4.x

Django Rest Framework 3.x

SQLite3 (banco de dados padrão do Django)

HTML5 / CSS3 (interface administrativa do Django)

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

Python 3.12.2

pip

Visual Studio Code
 (opcional, mas recomendado)

## 🔗 Endpoints principais (exemplo)

Estudantes

GET /api/estudantes/ → Lista todos os estudantes

POST /api/estudantes/ → Cria um novo estudante

GET /api/estudantes/{id}/ → Detalhes de um estudante específico

PUT /api/estudantes/{id}/ → Atualiza um estudante

DELETE /api/estudantes/{id}/ → Remove um estudante

Cursos

GET /api/cursos/ → Lista todos os cursos

POST /api/cursos/ → Cria um novo curso

GET /api/cursos/{id}/ → Detalhes de um curso específico

PUT /api/cursos/{id}/ → Atualiza um curso

DELETE /api/cursos/{id}/ → Remove um curso

Relação Estudante ↔ Curso

GET /api/estudantes/{id}/cursos/ → Cursos em que o estudante está matriculado
## ⚙️ Instalação e execução

### 1️⃣ Verifique a versão do Python

Confirme que está usando Python 3.10 ou 3.11:

`python --version`

2️⃣ Instale o Virtualenv

`pip install virtualenv`

3️⃣ Crie o ambiente virtual
(Use .venv ou outro nome à sua escolha)

`python -m virtualenv .venv`

4️⃣ Ative o ambiente virtual

Windows (PowerShell):

`.venv\Scripts\Activate.ps1`

Windows (cmd):

`.venv\Scripts\activate`
Linux / macOS:

`source .venv/bin/activate`

5️⃣ Selecione o interpretador no VS Code
Abra o VS Code e pressione Ctrl + Shift + P → Python: Select Interpreter → escolha a versão/venv criada.

6️⃣ Instale as dependências

`pip install -r requirements.txt`

7️⃣ Rode as migrations

`python manage.py migrate`

8️⃣ Inicie o servidor

`python manage.py runserver`
