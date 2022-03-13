FROM python:3

WORKDIR /app
COPY ./src .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]