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
- You have to create superuser first with `python3 manage.py createsuperuser`
- You also have to run `python3 manage.py collectstatic` to collect static file of admin panel
- Now finally run `python3 manage.py runserver` and visit http://localhost:8000/admin to add another user (use superuser credentials to login into admin page)

Note when creating another user, make sure they have these permissions so they're able to create a post and comment existing post:
```
mainforum | mainforum | Can add mainforum
mainforum | mainforum | Can view mainforum
mainforum | maincomment | Can add maincomment
mainforum | maincomment | Can view maincomment
```

The easiest way: _coming soon_