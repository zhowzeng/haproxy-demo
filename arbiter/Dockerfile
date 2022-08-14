FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 2222
CMD ["python", "server.py"]
