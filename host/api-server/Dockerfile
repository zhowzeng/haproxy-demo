FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 2244
CMD ["python", "server.py"]
