# DjangoProject

## Play2Learn Complete Website Project

## Instructions

You'll need a [SendGrid](https://sendgrid.com/) account. Email settings in `settings.py` begin on line 122 with your SENDGRID_API_KEY.

I put my SENDGRID_API_KEY in a `local_settings.py`.

**Note to instructor(s):**

I set up my SendGrid account just like I was taught in Lesson 7 of the Django course.
Hopefully that makes it easier to get this app up and running so you can grade the thing.

1. Unzip the file
2. Open terminal.
3. `$=> python -m venv .venv`
4. Activate your virtual env
5. `$=> pip install -r requirements.txt`
6. `$=> python manage.py runserver`

Don't forget to create a superuser for Django's admin and run migrations

7. Open a new terminal in vue-games app directory.
8. `$=> npm install`
9. `$=> npm run serve`

You should have the Django application running at:

http://127.0.0.1:8000/#/

and the Vue application running at:

http://127.0.0.1:8080/#/

If you want to run this app on your localhost, update `settings.py` accordingly.

**TESTS:**

`$=> python3 manage.py test`

**To view test coverage:**

`$=> coverage run --omit='*/venv/*' manage.py test`

`$=> coverage report` # PRINT TO TERMINAL

`$=> coverage html ` # PRINT TO FILE

`$=> open -a "browser name here" htmlcov/index.html`
