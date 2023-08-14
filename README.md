# NOTE: This branch isn't production ready. Some feature would be missing

Features:
- Nothing

How-to:
- First, install Python, pip, and MySQL server (if you haven't)
- Since the frontend is now based on React, it's time to install Node.js and Npm (Yay!!!!!!!)
- Clone this repo (if you haven't) and `cd` into directory where this repo cloned
- cd to `backend/` then run `pip3 install -r requirements.txt`
- Prepare MySQL server, because you need it for Database (fill required field in `.env` (see `.env.example`))
- Now run `python3 manage.py makemigrations backend` and `python3 manage.py migrate` to set up the database
- You have to run `python3 manage.py migrate` just to make sure super user is added
- Now finally run `python3 manage.py runserver` and visit http://localhost:8000/ to test API connection
- Go back to repository directory and go to `frontend`, run `npm i`

The easiest way: _coming soon_