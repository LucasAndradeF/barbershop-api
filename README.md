# 💈 barbershop-api 💈

API RESTful desenvolvida com Django e Django REST Framework para gerenciamento completo de uma barbearia.  
Possui autenticação via JWT, controle de usuários (clientes e barbeiros), agendamentos e serviços diversos.

---

## 📌 Funcionalidades

### 🔐 Autenticação JWT

- Cadastro e login de usuários.
- Visualização de perfil.
- Exclusão de conta.
- Diferenciação de permissões entre **clientes** e **barbeiros**.

### 🧔‍♂️ Barbeiros

- Cadastro de barbeiros com campos específicos.
- Atualização e exclusão de perfil.
- Consulta de agendamentos relacionados ao barbeiro.
- Registro e listagem de **serviços oferecidos**.

### 👤 Clientes

- Cadastro e login de clientes.
- Criação, atualização e exclusão de **agendamentos**.
- Visualização de serviços disponíveis pelos barbeiros.
- Visualização de agendamentos próprios.

### 💈 Serviços

- CRUD de serviços oferecidos por cada barbeiro.
- Preço, nome e duração definidos por barbeiro.
- Consulta por cliente e barbeiro.

### 📅 Agendamentos

- CRUD de agendamentos feitos por clientes.
- Validação automática de disponibilidade.
- Associação direta com barbeiros e serviços.

---

## 🛠️ Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite (ambiente local)
- Simple JWT (autenticação)
- VS Code

---

## 🚀 Como rodar o projeto

```bash
# 1. Clone o repositório
git clone git@github.com:LucasAndradeF/barbershop-api.git
cd barbershop_api

# 2. Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou no Linux/macOS:
# source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrações
python manage.py makemigrations
python manage.py migrate

# 5. Crie um superusuário (opcional)
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver
```

---


## 📚 Documentação da API

A documentação API está disponível nas seguintes rotas:

- 🔷 Swagger UI: [`/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/)  
- 🔶 Redoc: [`/api/schema/redoc/`](http://localhost:8000/api/schema/redoc/)  

> Acesse para visualizar e testar todos os endpoints da API com descrições, parâmetros e exemplos.


## 🧑‍💻 Autor

Desenvolvido por **Lucas Ferreira**  
Estudante de Ciência da Computação  
