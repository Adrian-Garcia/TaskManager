# Task Manager

## Setup
Install django
```
pip install django
```

Install djangorestframework to use the api
```
pip install django djangorestframework
```

Create virtual environment
```
python3 -m venv venv
```

Activate virtual environment
```
source venv/bin/activate
```

Run migrations
```
python3 manage.py migrate
```

Start local server
```
python3 manage.py runserver
```

# User interface
After starting local server, you can go to http://127.0.0.1:8000/tasks/ and start creatring tasks.

# API

This API allows you to manage tasks. You can create, read, update, and delete tasks using the provided endpoints.

## Base URL

```
http://127.0.0.1:8000/api/
```

---

## Endpoints

### 1. **GET /api/tasks**

Retrieve a list of all tasks.

#### Request

- **Method**: `GET`
- **URL**: `/api/tasks/`
- **Headers**:
  - `Content-Type: application/json`

#### Response

- **Status Code**: `200 OK`
- **Body**: A list of tasks, each containing:
  - `id`: Task ID
  - `title`: The title of the task
  - `description`: The description of the task
  - `email`: email of the person that created the task

Example response:

```json
[
  {
    "id": 1,
    "title": "Task 1",
    "description": "This is the first task.",
    "email": "mail@mail.com"
  },
  {
    "id": 2,
    "title": "Task 2",
    "description": "This is the second task.",
    "email": "email@email.com"
  }
]
```

---

### 2. **POST /api/tasks/post**

Create a new task.

#### Request

- **Method**: `POST`
- **URL**: `/api/tasks/post/`
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
  - `title`: (Required) The title of the task.
  - `description`: (Required) The description of the task.
  - `description`: (Required) The email of the person that created the task.

Example request body:

```json
{
  "title": "New Task",
  "description": "This task was created using the POST endpoint.",
  "email": "email@email.com"
}
```

#### Response

- **Status Code**: `201 Created`
- **Body**: The created task object, including its `id`, `title`, and `description`.

Example response:

```json
{
  "id": 3,
  "title": "New Task",
  "description": "This task was created using the POST endpoint.",
  "email": "email@email.com"
}
```

---

### 3. **PUT /api/tasks/{id}**

Update an existing task.

#### Request

- **Method**: `PUT`
- **URL**: `/api/tasks/{id}/`  
  Replace `{id}` with the ID of the task you want to update.
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
  - `title`: (Optional) New title of the task.
  - `description`: (Optional) New description of the task.

Example request body:

```json
{
  "title": "Updated Task Title",
  "description": "Updated description of the task."
}
```

#### Response

- **Status Code**: `200 OK`
- **Body**: The updated task object.

Example response:

```json
{
  "id": 1,
  "title": "Updated Task Title",
  "description": "Updated description of the task.",
  "email": "mail@mail.com"
}
```

---

### 4. **DELETE /api/tasks/delete/{id}**

Delete a task by its ID.

#### Request

- **Method**: `DELETE`
- **URL**: `/api/tasks/delete/{id}/`  
  Replace `{id}` with the ID of the task you want to delete.

#### Response

- **Status Code**: `204 No Content`
- **Body**: An empty body indicating the task was successfully deleted.

Example response:

```json
{
  "message": "Task deleted successfully."
}
```

---

## Example Usage

### CURL Examples

#### 1. **Get the list of tasks**

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/
```

#### 2. **Create a new task**

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
     -H "Content-Type: application/json" \
     -d '{"title": "New Task", "description": "This is a newly created task."}'
```

#### 3. **Update an existing task**

```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Task", "description": "Updated task description."}'
```

#### 4. **Delete a task**

```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/
```