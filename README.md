# Library Project - exam prep

### Why this project:

This projsect is designed to prepare myself for the exam next week.

### A few words about this project:

This project constitutes a fully capable library managment system.

This means including both book and membership managment and how not - the links & actions between those.

# Tech stack:

### Software:

- pytyhon 3.14
- FastAPI
- uvicorn
- pydantic

### Infrastructure:

- docker
- mysql (in docker)
- docker-compose

# Directory tree for this project:

```plaintext
library-api/
┃
┃
┣━━ main.py
┣━━ database/
┃ ┣━━ db_connection.py
┃ ┣━━ book_db.py
┃ ┗━━ member_db.py
┣━━ routes/
┃ ┣━━ book_routes.py
┃ ┣━━ member_routes.py
┃ ┗━━ report_routes.py
┣━━ logs/
┃ ┗━━ app.log
┃
┣━━ README.md
┣━━ requirements.txt
┗━━ .gitignorelibrary-api/
```
  
# Setup & How to run:
first clone the project and `cd` into it
open your terminal and run:
```bash
git clone "https://github.com/ariWeinberg/library-project-exam-prep.git" ./library-project && cd ./library-project
```
Then you can run this project in one of three ways:

1. #### localy with mysql in a container:

   ##### first start a mysql container:


   ```plaintext
   docker run \
   --name mysql_library_project\
    -p 3307:3306\
    -e MYSQL_ROOT_PASSWORD=secret\
    -e MYSQL_DATABASE=library_db\
    -d\
    mysql:8
   ```

   #### note that you may change the name of the container, its port, passowrd or DB name as long as you update the .env file accordingly.

   ##### Then create a virtual environment:

   ```bash
   python3 -m venv ./.venv
   ```

   ##### source the virtual environment

   ```bash
   source ./.venv/bin/activate
   ```

   #### install the requirements:

   ```bash
   pip install -r ./requirements.txt
   ```

   #### finaly start the app with either command:

   ```bash
   python3 ./main.py
   ```

   ```bash
   uvicorn "main:app" --host 0.0.0.0 --port 9995
   ```

   note that you can add the optional flag `--reload` while editing the code and the server will reload on every save.
2. #### run with docker compose:


   ```bash
   docker compose up -d
   ```

   then to shut it down:

   ```
   docker compose down
   ```
3. #### run docker compose as dev container (automatic reload):


   ```bash
   docker compose -f ./dev.compose.yaml up -d
   ```

   then

   ```
   docker compose -f ./dev.compose.yaml down
   ```

# DB table structure:

### table: `books`

| column name               | column type                                               | constraints                | description                                                                                                                   |
| ------------------------- | --------------------------------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `id`                    | int                                                       | NOT NULL PK AUTO_INCREMENT | internal id for the book                                                                                                      |
| `title`                 | VARCHAR(50)                                               | NOT NULL                   | title of the book                                                                                                             |
| `author`                | VARCHAR(50)                                               | NOT NULL                   | author name                                                                                                                   |
| `genere`                | ENUM('Fiction','Non-Fiction','Science','History','Other') | NOT NULL                   | book genere                                                                                                                   |
| `is_avilable`           | boolean (tinyint)                                         | NOT NULL                   | is this book avilable (`borrowed_by_member_id` must be `NULL`)                                                            |
| `borrowed_by_member_id` | int                                                       | default null FK            | the id of the currently borrowing member.<br />must be `NULL` if `is_avilable` is `true` must not be `NULL` otherwise |

---

### table: `members`

| column name       | column type | constraints                | description                                                |
| ----------------- | ----------- | -------------------------- | ---------------------------------------------------------- |
| `id`            | int         | NOT NULL PK AUTO_INCREMENT | internal id for the member                                 |
| `name`          | VARCHAR(50) | NOT NULL                   | member's name                                              |
| `email`         | VARCHAR(50) | NOT NULL UNIQUE            | member's email address                                     |
| `is_active`     | boolean     | NOT NULL                   | is this user active? (an inactive user can't borrow books) |
| `total_borrows` | int         | NOT NULL default 0         | the total times this member borrowed a book.               |

---




# Endpoints:

| method | endpoint                       | description                                 | path parameters                                                        | query parameters | request body                                                                                                                                                  | response           |
| ------ | ------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| POST   | /books                         | create a new book.                          | none                                                                   | none             | ``{'title': "string", 'author':'string', 'genere':'string, one of: ('Fiction','Non-Fiction','Science','History','Other')'}``                                  | 201, 503, 400, 409 |
| GET    | /books                         | get all books                               | none                                                                   | none             | none                                                                                                                                                          | 503, 200 - []      |
| GET    | /books/{id}                    | get a spesific book                         | `id` - the id of the book                                            | none             | none                                                                                                                                                          |                    |
| PUT    | /books/{id}                    | update the details of a spesific book.      | `id` - the id of the book                                            | none             | ``{'title': "string - optional", 'author':'string - optional', 'genere':'string, one of: ('Fiction','Non-Fiction','Science','History','Other') - optional'}`` |                    |
| PUT    | /books/{id}/borrow/{member_id} | borrow a book to a member                   | `id` - the id of the book,<br />`member_id` - the id of the member | none             | none                                                                                                                                                          |                    |
| PUT    | /books/{id}/return/{member_id} | return the book from the member             | `id` - the id of the book,<br />`member_id` - the id of the member | none             | none                                                                                                                                                          |                    |
| POST   | /members                       | create a new member.                        | none                                                                   | none             | ``{'name': "string", 'email':'string'}``                                                                                                                      | 201, 503, 400, 409 |
| GET    | /members                       | get all members                             | none                                                                   | none             | none                                                                                                                                                          |                    |
| GET    | /members/{id}                  | get a spesific member                       | `id` - the member's id                                               | none             | none                                                                                                                                                          |                    |
| PUT    | /members/{id}                  | update a spesific member's detailes         | `id` - the member's id                                               | none             | ``{'name':'string', 'email':'string'}``                                                                                                                       |                    |
| PUT    | /members/{id}/deactivate       | deactivate a member                         | `id` - the member's id                                               | none             | none                                                                                                                                                          |                    |
| PUT    | /members/{id}/activate         | activate a member                           | `id` - the member's id                                               | none             | none                                                                                                                                                          |                    |
| GET    | /reports/summary               | get a general summary report for the system | none                                                                   | none             | none                                                                                                                                                          |                    |
| GET    | /reports/books-by-genre        | get how many books are in each genere       | none                                                                   | none             | none                                                                                                                                                          |                    |
| GET    | /reports/top-member            | get the member who borrowed the most        | none                                                                   | none             | none                                                                                                                                                          |                    |



---
  

# System rules:
1. A book is created with title, author, genere (supplied by user) and `is_available`=True, `borrowed_by`=NULL.
2. Genere must be one of the folowing values:  `Fiction` / `Non-Fiction` / `Science` / `History` / `Other`.
3. A member is created with name, email (supplied by user) and `is active`=True, `total_borrows`=0.
4. `email` must be unique across all records.
5. A member with`is active`=False cannot borrow any book.
6. Nobody can borow a book with `is_available`=False (already borowed).
7. A user can have a maximum of 3 borrowed books at any given time.
8. A book can only be returned by the member it is currently borrowed to.


# System flow:
### System setup  
### ↓  
### A request comes in  
### ↓  
### Request is handled  
### ↓  
### DB is updated  
### ↓  
### Response sent to user  
---