FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

ADD . .

RUN pip install -r requirements.txt --default-timeout=100

EXPOSE 5000

CMD python manage.py runserver
