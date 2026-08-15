# Week 1 — Foundation & Project Setup

## Objective

The goal of Week 1 is to establish the foundation of the AI-Powered RAG Knowledge Assistant.

This includes:

- Setting up the project repository
- Creating the Next.js frontend
- Creating the FastAPI backend
- Provisioning PostgreSQL
- Enabling pgvector
- Designing the database schema
- Connecting the backend to the database

## Current Progress

- [x] Project folder created
- [x] Git repository initialized
- [x] Basic project structure created
- [x] README created
- [ ] Next.js frontend
- [ ] FastAPI backend
- [ ] PostgreSQL
- [ ] pgvector
- [ ] Database schema
- [ ] Backend-database connection

## Architecture

The initial architecture will consist of:

```text
Next.js Frontend
       |
       | HTTP API
       |
       v
FastAPI Backend
       |
       | SQLModel
       |
       v
PostgreSQL + pgvector