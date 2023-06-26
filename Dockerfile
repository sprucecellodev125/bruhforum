FROM python:3.11
EXPOSE 8000
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations mainforum
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000