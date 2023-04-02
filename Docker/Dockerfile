FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

CMD ["export DOCKER_BUILDKIT=0", "export COMPOSE_DOCKER_CLI_BUILD=0", "python3","manage.py", "runserver", "0.0.0.0:8000"]