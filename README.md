# Quiz Backend Management API

A RESTful backend application built with **FastAPI** that allows users to create, manage, and retrieve quiz questions and answer choices. It provides full CRUD operations for quiz management while maintaining relationships between questions and their corresponding choices using a relational database.

This project demonstrates modern backend development practices, including API design, data validation, database management, and scalable application architecture.

## Features

- Create, Read, Update, and Delete (CRUD) operations for quiz questions
- CRUD operations for answer choices
- One-to-Many relationship between questions and choices
- Request and response validation using Pydantic
- Database operations using SQLAlchemy ORM
- RESTful API design
- Interactive API documentation with Swagger UI

## Tech Stack

- FastAPI
- Python
- SQLAlchemy
- Pydantic
- SQLite / MySQL / PostgreSQL
- Uvicorn

## Project Structure

```
quiz-backend-api/
│── app/
│   │── models/
│   │── schemas/
│   │── routes/
│   │── database.py
│   │── main.py
│── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip


### Questions

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/questions` | Create a question |
| GET | `/questions` | Get all questions |
| GET | `/questions/{id}` | Get a question by ID |
| PUT | `/questions/{id}` | Update a question |
| DELETE | `/questions/{id}` | Delete a question |

### Choices

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/choices` | Create an answer choice |
| GET | `/choices` | Get all choices |
| PUT | `/choices/{id}` | Update a choice |
| DELETE | `/choices/{id}` | Delete a choice |

## Learning Outcomes

This project helped in understanding:

- REST API development with FastAPI
- Database modeling using SQLAlchemy
- Data validation using Pydantic
- CRUD operations
- Relational database design
- Backend application architecture

## Future Enhancements

- [ ] User Authentication (JWT)
- [ ] Role-Based Access Control
- [ ] Quiz Attempt History
- [ ] Leaderboards
- [ ] Timer-based Quizzes
- [ ] Analytics Dashboard
- [ ] Adaptive Quiz Recommendation System
- [ ] Machine Learning-based Personalized Quizzes
