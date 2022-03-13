FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app
COPY ./src .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]