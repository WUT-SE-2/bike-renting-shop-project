FROM python:3.8-slim-buster
CMD ["python", "bikeshop/manage.py", "migrate"]
# set work directory
WORKDIR .:/usr/src/app/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY bikeshop .
CMD ["gunicorn", "bikeshop.wsgi:application"]


