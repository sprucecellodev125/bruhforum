### Introducing, bruhforum, the most bruhment forum system made in Django ✨ (atleast still usable)

Uh, why the hell I make this? because why not

Features:
- Login
- Create post and comment a post
- View any post and comments
- Easy to set-up
- Admin panel

How-to:
- First of all, install Python and pip
- Clone this repo (if you haven't) and `cd` into directory where this repo cloned
- Run `pip3 install -r requirements.txt`
- You also have to run `python3 manage.py collectstatic` to collect static file of admin panel
- Now run `python3 manage.py makemigrations mainforum` and `python3 manage.py migrate` to set up the database
- You have to create superuser with `python3 manage.py createsuperuser` and then run `python3 manage.py migrate` just to make sure super user is added
- Now finally run `python3 manage.py runserver` and visit http://localhost:8000/admin to add another user (use superuser credentials to login into admin page)

Note when creating another user, make sure you created groups called "Member" with following permissions:
```
mainforum | mainforum | Can add mainforum
mainforum | mainforum | Can view mainforum
mainforum | maincomment | Can add maincomment
mainforum | maincomment | Can view maincomment
```
and add newly-created user to that groups. Otherwise they're didn't able to create any post or comment to existing post

If you getting error related to CSRF token (when you're visit the forum with domain/hostname instead of IP address, go to settings.py and look for CSRF_TRUSTED_ORIGINS then put the forum URL there. If still the same, look for CORS_ALLOWED_ORIGINS and CORS_ORIGIN_WHITELIST and do the same thing as what you do with CSRF_TRUSTED_ORIGINS)

The easiest way: _coming soon_