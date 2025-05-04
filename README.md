# Django Tasks API
#TASK MANAGEMENT USING DRF(DJANGO REST_FRAMEWORK)

This project is a simple Django CRUD API for managing tasks, containerized using Docker and configured to run seamlessly in Gitpod.
It uses PostgreSQL as the database (via Docker Compose) and includes support for .env configuration. 
To get started, 
clone the repository using `git clone https://github.com/Narendran-root/django-tasks.git`,
and open it in Gitpod.


Alternatively, to run it locally,
use `docker-compose up --build` 
and
access the backend at `http://localhost:8000`.
Ensure a `.env` file exists with the following content: 
`POSTGRES_USER=postgres`,
`POSTGRES_PASSWORD=postgres`, 
`POSTGRES_DB=postgres`, 
`SECRET_KEY=your-secret-key`, and 
`DEBUG=True`. 
Run `python manage.py makemigrations` 
and 
`python manage.py migrate` to initialize the database. 
Start the server with `python manage.py runserver 0.0.0.0:8000`. 
The API provides endpoints like `GET /tasks/`, `POST /tasks/`, `PUT /tasks/<id>/`, and `DELETE /tasks/<id>/`.
PostgreSQL runs as the `db` service in Docker, and logs can be accessed with `docker-compose logs db`.


The project is MIT licensed and configured with WhiteNoise for static file handling.

