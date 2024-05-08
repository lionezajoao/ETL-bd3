FROM python:3.11

WORKDIR /usr/src/app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY . .

CMD ["pipenv", "run", "build"]