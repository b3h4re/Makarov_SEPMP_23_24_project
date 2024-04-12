FROM python:3.11

RUN pip install --upgrade pip

EXPOSE 5000

CMD ["python", "./manage.py"]
