# A minimal django set-up template


## Set up local environment

- _Clone repository_ `git clone https://github.com/ChogirmaliYigit/django-template.git`
- _Run_ `bash set_pre_commit.sh` to set the pre-commit.
- _Run_ `cp .env.example .env`. Then configure the `.env` file's constants.
- Create an environment using command `python -m venv venv` for Windows and `python3 -m venv venv` for Unix-based OS.
- Install requirements using command `pip install -r requirements.txt` for Windows and `pip3 install -r requirements.txt` for Unix-based OS.
- After configure your database, you can run `python manage.py makemigrations` and `python manage.py migrate`.
- Also run the commands: `python manage.py collectstatic` and `python manage.py compilemessages`
- Create a superuser using the command `python manage.py createsuperuser` and start development!


## Useful commands
- If you want to create an app, you need to go to the `apps` directory using command `cd apps/` and run this command: `python ../manage.py startapp <app_name>`
