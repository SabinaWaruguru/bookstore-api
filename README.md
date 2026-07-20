# Bookstore API 📚

A FastAPI-based Book Inventory Management API that allows a small bookstore to manage books using CRUD (Create, Read, Update, Delete) operations. The API uses PostgreSQL as the database and SQLModel for database models and interactions.

## Features

* Create new books
* View all books
* View a single book by ID
* Update book details
* Delete books
* Search books by title or author
* PostgreSQL database integration
* Automatic API documentation using Swagger UI

---

## Technologies Used

* **Python**
* **FastAPI**
* **SQLModel**
* **PostgreSQL**
* **Uvicorn**
* **Alembic**
* **Docker**
* **Pydantic**

---

## Project Structure

```
bookstore-api/
│
├── main.py                 # FastAPI application and CRUD endpoints
│
├── models/
│   ├── __init__.py
│   └── book.py             # Book database models
│
├── database/
│   ├── __init__.py
│   └── session.py          # Database connection and session management
│
├── .env                    # Environment variables
├── docker-compose.yml      # PostgreSQL container setup
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Dependency lock file
└── README.md               # Project documentation
```

---

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/SabinaWaruguru/bookstore-api.git
```

Navigate into the project:

```bash
cd bookstore-api
```

---

## 2. Create and Activate Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Using uv:

```bash
uv add fastapi uvicorn sqlmodel psycopg2-binary alembic python-dotenv
```

---

# Database Setup

The project uses PostgreSQL through Docker.

Start the database:

```bash
docker compose up -d
```

Database configuration:

```
Database Name: bookstore_db
Username: postgres
Password: postgres
Port: 5432
```

The `.env` file contains:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/bookstore_db
```

---

# Running the Application

Start the FastAPI server:

```bash
uv run uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides Swagger UI documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Available endpoints:

| Method | Endpoint           | Description                     |
| ------ | ------------------ | ------------------------------- |
| POST   | `/books`           | Create a new book               |
| GET    | `/books`           | Retrieve all books              |
| GET    | `/books/{book_id}` | Retrieve a book by ID           |
| PATCH  | `/books/{book_id}` | Update book details             |
| DELETE | `/books/{book_id}` | Delete a book                   |
| GET    | `/books/search`    | Search books by title or author |

---

# Book Data Model

Each book contains:

| Field          | Description                 |
| -------------- | --------------------------- |
| id             | Auto-generated book ID      |
| title          | Book title                  |
| author         | Book author                 |
| isbn           | Unique ISBN number          |
| published_year | Year the book was published |
| price          | Book price                  |
| stock          | Available stock quantity    |
| available      | Book availability status    |
| created_at     | Date created                |
| updated_at     | Date updated                |

---

# Example Request

## Create a Book

POST `/books`

```json
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "isbn": "9780061122415",
  "published_year": 1988,
  "price": 800,
  "stock": 10,
  "available": true
}
```

---

# CRUD Operations

## Create

Adds a new book into the inventory.

## Read

Retrieves all books or a specific book using its ID.

## Update

Modifies existing book information.

## Delete

Removes a book from the inventory.

---

# Testing

The API can be tested using:

* Swagger UI
* Postman

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# Author

**Sabina Waruguru**