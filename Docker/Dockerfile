FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

COPY . .

EXPOSE DOCKER_BUILDKIT=0

RUN pip3 install -r requirements.txt


CMD ["python3","manage.py", "runserver", "0.0.0.0:8000"]