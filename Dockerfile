FROM python:3.10-alpine as prod
RUN apk update && apk add postgresql-dev gcc musl-dev && apk cache clean

RUN pip install poetry==1.4.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/
WORKDIR /app/

# Installing requirements
RUN poetry install --only main

# Copying actuall application
COPY . /app/
RUN poetry install --only main

RUN chmod +x /app/entrypoint.sh

# Run app
CMD ["./entrypoint.sh"]

FROM prod as dev

RUN poetry install
