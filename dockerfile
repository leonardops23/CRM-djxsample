FROM python:3.13

WORKDIR /app

COPY requirements.text .

RUN pip install -r requirements.txt

# crear archivos de media subidos por usuarios
RUN mkdir -p media

COPY . .

# puerto que usa django
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
