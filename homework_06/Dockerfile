FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY . .

RUN poetry install


CMD ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "main.py", \
    "--callable", "app", "--stats", "0.0.0.0:81"]

