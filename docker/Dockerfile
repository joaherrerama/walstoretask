FROM python:3.7-alpine

# Install GDAL
RUN apk update && apk upgrade \
    && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        postgresql-client \
        postgresql-dev \
        musl-dev \
        gcc \
    && apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        gdal-dev \
        geos-dev \
        proj-dev

# Set environment variables
ENV PYTHONUNBUFFERED 1 \
    PYTHONIOENCODING=UTF-8


COPY requirements.txt /requirements.txt

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

EXPOSE 8000