FROM tiangolo/uwsgi-nginx-flask:python3.11

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY . .

RUN poetry install

EXPOSE 8000

CMD python main.py
#uvicorn main:app --host 0.0.0.0
