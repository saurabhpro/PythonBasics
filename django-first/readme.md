- `(venv) ➜ django-first git:(master) ✗ django-admin startproject learning_log .`
- apps are web pages or group - and a lot of them makes a project
    - to create a new app - open a new terminal venv and
    - `(venv) ➜ django-first git:(master) ✗ python manage.py startapp learning_logs`

- modify `models.py`, call `makemigrations` on learning_logs
    - `(venv) ➜ django-first git:(master) ✗ python manage.py makemigrations learning_logs`
    - `(venv) ➜ django-first git:(master) ✗ python manage.py migrate`

- to start the web app `python manage.py runserver`

> make sure you will need to goto `/admin` and enter some topics and entries for this app to work

# shell
```bash
> from learning_logs.models import Entry

> Entry.objects.all();
<QuerySet [<Entry: This is my first text...>, <Entry: One of the most important concepts in climbing is ...>, <Entry: In the opening phase of the game, it’s important t...>]>
```

# style
- see the static directory
