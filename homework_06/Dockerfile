FROM python:3.11.4-slim-bookworm

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0
