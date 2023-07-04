# Import the necessary modules
import os
import sys
import django

# Add the current directory to Python's path to find the Django settings module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module for the shell
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bruhforum.settings')

# Initialize the Django application
django.setup()

print("""
Welcome to Bruhforum setup.
You can setup your very-first "forum" system
in this command-line Python program
""")

from django.contrib.auth.models import User
from mainforum.models import Core
from getpass import getpass

username = input("Admin Username: ")
password = getpass("Admin Password: ")
forumname = input("Forum name: ")

user = User.objects.create_user(username, password=password)
user.is_superuser=True
user.is_staff=True
user.save()

forum = Core(name=forumname, needsetup=True)
forum.save()