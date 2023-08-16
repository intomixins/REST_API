FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -qy install python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
ADD /rest/requirements.txt /app/
RUN pip install -r requirements.txt

ADD /rest /app/backend
ADD /docker /app/docker

RUN chmod +x /app/docker/rest/server-entrypoint.sh
RUN chmod +x /app/docker/rest/worker-entrypoint.sh


