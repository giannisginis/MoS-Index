FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL Maintainer="Ioannis Gkinis - giannisginis53@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app