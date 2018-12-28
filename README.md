# Webber

My first Django based project :)

## How started?

Clone repository: `git clone https://github.com/r0v/Webber.git`

Go inside directory `cd Webber`

Install dependencies `pipenv install`

Jump into virtual enviroment `pipenv shell`

Run migrations `python manage.py migrate`

### Generate static files

1. Comment `STATICFILES_DIRS` in Webber/settings.py, uncomment `STATIC_ROOT`.
2. Next, generate nessesery static files: `python manage.py collectstatic` / `yes`.
3. After this, look above pkt. 1 and do vice versa commands from behind

Start developer server `python manage.py runserver` and develop

<sub>*Optionally create admin account if you haven't done it yet*</sub>

## Info

Server run on port [http://localhost:8000](http://localhost:8000)

Have fun and contribute :)
