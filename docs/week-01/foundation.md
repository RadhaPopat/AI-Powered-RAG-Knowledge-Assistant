# Week 1 — Foundation & Project Setup

## 🌱 What are we doing this week?

Before building the actual AI assistant, we need to build the foundation of the application.

Think of building a house: before constructing the rooms, you need a solid foundation. Our software project is similar.

In Week 1, we are setting up:

- The frontend
- The backend
- The database
- The vector database capability
- The initial database structure
- Git and GitHub
- Project documentation

---

## 1. What are we building?

The project is called **AI-Powered RAG Knowledge Assistant**.

The goal is to build an AI assistant that can answer questions using the user's own documents.

For example, if a user uploads a 200-page PDF, instead of manually searching through it, they can ask:

> *"What does this document say about gradient descent?"*

Our application will eventually:

1. Read the document.
2. Break the document into smaller pieces.
3. Convert those pieces into numbers called **embeddings**.
4. Store those embeddings in a database.
5. Find the pieces related to the user's question.
6. Feed those pieces to an AI model.
7. Generate an answer using the retrieved information.

This process is called **Retrieval-Augmented Generation (RAG)**.

We will build these features step by step over the coming weeks.

---

## 2. Goal of Week 1

The goal of Week 1 is not to build the complete AI assistant.

Instead, we are preparing the foundation.

By the end of Week 1, we will have:

- A Next.js frontend
- A FastAPI backend
- A PostgreSQL database
- The `pgvector` extension enabled
- A functional connection between Python and PostgreSQL
- The initial database tables created
- A GitHub repository set up
- Documentation explaining our architecture and choices

---

## 3. Project Structure

We are using a **monorepo** structure.

A monorepo means keeping different parts of the same project inside a single Git repository.

This makes it easier to manage the whole project in one place.

Our project structure looks like this:

```text
AI-Powered-RAG-Knowledge-Assistant/
│
├── frontend/
│   └── Next.js application
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── docs/
│   └── week-01/
│       └── foundation.md
│
├── .gitignore
└── README.md
```

---

## 4. Git and GitHub Setup

### What is Git?

Git is a version control tool that keeps track of changes in our project.

Think of it like a history book for the project.

For example:

```text
Project created
      ↓
Frontend added
      ↓
Backend added
      ↓
Database added
      ↓
RAG features added
```

Each important milestone can be saved as a **commit**.

This allows us to see how the project developed over time.

### What is GitHub?

GitHub is where we store our Git repository online.

It allows us to:

- Back up our project
- Track development
- Share our project
- Show our work to teachers and interviewers
- Maintain our project history

The GitHub repository is:

**AI-Powered-RAG-Knowledge-Assistant**

The repository was connected using:

```bash
git remote add origin https://github.com/RadhaPopat/AI-Powered-RAG-Knowledge-Assistant.git
```

We are documenting the project while building it instead of trying to document everything at the end.

---

## 5. Frontend Setup

### What is the frontend?

The frontend is the part of the application that the user can see and interact with.

Eventually, it will contain features such as:

- Login page
- Document upload page
- Chat interface
- AI-generated answers
- Document citations

For the frontend, we are using **Next.js**.

### Why Next.js?

Next.js is a framework built on React that helps us create modern web applications.

It provides features such as:

- App Router and page routing
- TypeScript support
- Good project structure
- Tailwind CSS integration
- Fast development using Turbopack

### Creating the frontend

The frontend was initialized using:

```bash
npx create-next-app@latest frontend
```

The generated project uses:

- Next.js 16.3.1
- React
- TypeScript
- Tailwind CSS
- ESLint
- App Router
- Turbopack

### Testing the frontend

We started the development server using:

```bash
npm run dev
```

The application was successfully available at:

```text
http://localhost:3000
```

This confirmed that the Next.js frontend was working correctly.

---

## 6. Backend Setup

### What is the backend?

The backend is the part of the application that works behind the scenes.

Later, the backend will handle tasks such as:

- Uploading documents
- Processing documents
- Searching the database
- Generating embeddings
- Finding relevant information
- Communicating with AI models

For the backend, we are using **FastAPI with Python**.

### Why Python?

Python has a large ecosystem for Artificial Intelligence and Machine Learning.

Later in this project, we will work with technologies such as:

- PDF processing
- Embedding models
- LangChain
- Vector search
- LLM APIs

Python makes working with these technologies easier.

### Python Virtual Environment

We created a Python virtual environment called:

```text
venv
```

A virtual environment creates an isolated space for the project's Python packages.

For example:

```text
Project A
    ↓
Its own Python packages

Project B
    ↓
Different Python packages
```

This prevents packages from different projects from interfering with each other.

### Backend Dependencies

The backend uses:

- FastAPI
- Uvicorn
- SQLModel
- SQLAlchemy
- Psycopg
- python-dotenv

The database-related packages were installed using:

```bash
pip install sqlmodel psycopg[binary] python-dotenv
```

---

## 7. PostgreSQL Setup

### What is PostgreSQL?

PostgreSQL is the database we are using for our application.

A database is a place where our application can store information.

Think of it like a large, organized filing cabinet.

Instead of putting everything in one place, we create separate tables for different types of information.

For our project, we will have tables for:

```text
Users
Documents
Document Chunks
```

### Why do we need PostgreSQL?

Our application needs to remember information.

For example, when a user uploads:

```text
Machine_Learning.pdf
```

the application needs to remember:

- Who uploaded it
- What the file is called
- Where the file is stored
- What pieces of text came from it
- The embeddings of those pieces

PostgreSQL will store this information.

### PostgreSQL Installation

PostgreSQL 18.6 was installed on the computer.

The PostgreSQL `bin` directory was added to the PATH environment variable.

This allows us to run PostgreSQL commands directly from PowerShell.

For example:

```bash
psql --version
```

The PostgreSQL server version was checked using:

```sql
SELECT version();
```

The result confirmed:

```text
PostgreSQL 18.6
```

---

## 8. pgvector

### What is pgvector?

`pgvector` is an extension for PostgreSQL.

An extension gives an existing program an additional ability.

PostgreSQL is already good at storing normal information such as:

```text
Name
Email
File name
Date
Number
```

But our RAG application also needs to store **vectors**.

### What is a vector?

Later, we will use an embedding model to convert text into a list of numbers.

For example:

```text
"What is machine learning?"
```

could be converted into something like:

```text
[0.12, -0.45, 0.73, 0.21, ...]
```

These numbers are called an **embedding**.

An embedding represents the meaning of the text in numerical form.

### Why do we need pgvector?

Suppose our database contains:

```text
"Python is commonly used for artificial intelligence."

"Python is a programming language."

"The weather is sunny today."
```

A user asks:

```text
"What can Python be used for?"
```

We don't want our system to only look for exact matching words.

We want it to find text with a similar meaning.

`pgvector` allows PostgreSQL to store vectors and later compare them to find similar information.

This will become very important when we build the RAG retrieval system.

---

## 9. Checking pgvector Availability

We checked whether the `vector` extension was available in PostgreSQL using:

```sql
SELECT name, default_version
FROM pg_available_extensions
WHERE name = 'vector';
```

The result was:

```text
 name  | default_version
-------+----------------
 vector | 0.8.6
```

This confirmed that `pgvector` was available.

---

## 10. Creating the Project Database

We created a separate database for this project.

The database was created using:

```sql
CREATE DATABASE rag_knowledge_db;
```

Then we connected to it:

```text
\c rag_knowledge_db
```

### Enabling pgvector

Inside our project database, we enabled the vector extension:

```sql
CREATE EXTENSION vector;
```

We then verified it using:

```sql
SELECT extname, extversion
FROM pg_extension
WHERE extname = 'vector';
```

The result was:

```text
 extname | extversion
---------+------------
 vector  | 0.8.6
```

This means that our project database can now work with vector data.

---

## 11. Connecting Python to PostgreSQL

We needed to allow our Python backend to communicate with PostgreSQL.

The database connection information is stored in:

```text
backend/.env
```

The actual database password is not written in this documentation.

The `.env` file is also excluded from Git so that sensitive information is not uploaded to GitHub.

### Why use `.env`?

We should never put passwords or secret keys directly inside our source code.

For example, this is **not** a good idea:

```python
password = "mypassword123"
```

Instead, sensitive information is stored in environment variables.

This keeps secrets separate from our source code.

---

## 12. Database Connection Architecture

We created:

```text
backend/app/database.py
```

This file is responsible for creating the connection between our Python application and PostgreSQL.

The basic flow is:

```text
Python Application
        ↓
     SQLModel
        ↓
    SQLAlchemy
        ↓
      Psycopg
        ↓
   PostgreSQL
```

We tested the database connection and confirmed that Python could successfully communicate with PostgreSQL.

---

## 13. Database Schema

### What is a database schema?

A database schema is the design or blueprint of our database.

Before building a house, we create a blueprint.

Similarly, before storing application data, we decide:

- What tables do we need?
- What information should each table contain?
- How should the tables be connected?

For Week 1, we created three main tables:

```text
Users
Documents
Document Chunks
```

---

### Users Table

The `users` table will store information about users of the application.

It contains:

```text
id
name
email
password_hash
created_at
updated_at
```

### Why `password_hash` instead of `password`?

We should never store a user's actual password.

Instead, we store a **password hash**.

Authentication will be implemented in a later phase.

---

### Documents Table

The `documents` table stores information about documents uploaded by users.

It contains:

```text
id
user_id
name
s3_url
created_at
```

The `user_id` tells us which user owns the document.

The `s3_url` will eventually store the location of the actual uploaded file.

---

### Document Chunks Table

Large documents can contain hundreds of pages.

Giving an entire document to an AI model at once would be inefficient.

Instead, we will eventually break the document into smaller pieces.

For example:

```text
Large PDF
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
...
Chunk 100
```

Each small piece is called a **chunk**.

The `document_chunks` table stores these pieces.

It contains:

```text
id
document_id
chunk_text
chunk_index
page_number
created_at
```

The `document_id` connects each chunk to the document it came from.

---

### Why is there no vector column yet?

The project roadmap mentions that `DocumentChunks` will eventually contain a vector column.

However, the vector size depends on the embedding model we choose.

For example:

```text
Embedding Model
       ↓
Embedding Dimension
       ↓
Vector Column
```

We should not randomly choose a vector dimension before deciding which embedding model we will use.

Therefore, the vector column will be added when we reach the embedding stage.

---

## 14. Creating and Verifying the Tables

We used SQLModel to define our database tables.

After starting the FastAPI application, SQLModel created the tables in PostgreSQL.

We verified them using:

```text
\dt
```

The result was:

```text
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+----------
 public | document_chunks | table | postgres
 public | documents       | table | postgres
 public | users           | table | postgres
```

This confirmed that all three tables were successfully created.

---

## 15. System Architecture Overview

Our Week 1 architecture looks like this:

```text
                 AI-Powered RAG Assistant
                            │
           ┌────────────────┴────────────────┐
           │                                 │
           ▼                                 ▼
    Next.js Frontend                   FastAPI Backend
           │                                 │
           │ HTTP API                        │
           └────────────────┬────────────────┘
                            │
                            ▼
                         SQLModel
                            │
                            ▼
                         Psycopg
                            │
                            ▼
                    PostgreSQL 18.6
                    rag_knowledge_db
                            │
               ┌────────────┼────────────┐
               ▼            ▼            ▼
             users      documents   document_chunks
```

`pgvector` is enabled inside PostgreSQL and will be used later when we start storing embeddings.

---

## 16. Challenges & Solutions

### Problem 1 — `psql` command was not recognized

#### Cause

Windows did not initially know where PostgreSQL's command-line tools were located.

#### Solution

We added PostgreSQL's `bin` directory to the PATH environment variable.

After restarting the terminal, `psql` worked correctly.

#### What I learned

PATH tells Windows where to look for programs when we type commands in the terminal.

---

### Problem 2 — `pgvector` was not initially available

#### Cause

PostgreSQL itself does not automatically include the `pgvector` extension.

#### Solution

We installed `pgvector` and configured PostgreSQL so that the `vector` extension became available.

The final check returned:

```text
vector | 0.8.6
```

---

### Problem 3 — Windows build tools

Installing `pgvector` on Windows required build tools.

We checked that `nmake` was available using:

```bash
nmake /?
```

We also checked PostgreSQL's configuration tool using:

```bash
pg_config --version
```

Both tools were successfully available.

---

## 17. Week 1 Checklist

- [x] Create project folder structure
- [x] Initialize Git repository
- [x] Connect GitHub repository
- [x] Set up documentation directory
- [x] Create Next.js frontend
- [x] Test Next.js application
- [x] Create FastAPI backend
- [x] Create Python virtual environment
- [x] Install backend dependencies
- [x] Install PostgreSQL 18.6
- [x] Add PostgreSQL to PATH
- [x] Verify PostgreSQL installation
- [x] Install `pgvector`
- [x] Verify `pgvector`
- [x] Create `rag_knowledge_db`
- [x] Enable `pgvector` in the database
- [x] Create `.env`
- [x] Configure database connection
- [x] Test Python → PostgreSQL connection
- [x] Create `users` table
- [x] Create `documents` table
- [x] Create `document_chunks` table
- [x] Verify database tables

---

## 18. Week 1 Result

At the beginning of Week 1, we had:

```text
An empty project foundation
```

At the end of Week 1, we have:

```text
Next.js frontend
       +
FastAPI backend
       +
PostgreSQL database
       +
pgvector
       +
SQLModel
       +
Initial database schema
       +
GitHub documentation
```

The application cannot answer questions yet.

That's completely fine.

We have built the foundation first. The actual RAG pipeline will be developed in the upcoming weeks.