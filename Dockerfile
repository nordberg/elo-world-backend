FROM python:3

WORKDIR /app

EXPOSE 5000

COPY requirements.txt /app

RUN pip install --no-cache -r requirements.txt

COPY . /app

CMD ["python", "./app.py"]
