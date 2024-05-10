FROM python:3.11

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install
RUN pipenv install psycopg2-binary

COPY . .

CMD ["pipenv", "run", "prod"]