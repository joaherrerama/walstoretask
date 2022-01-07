FROM python:3.8

# Install GDAL
RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

# Set environment variables
ENV PYTHONUNBUFFERED 1 \
    PYTHONIOENCODING=UTF-8

ENV ggl_place_key=AIzaSyBnndrLxH443KsAD1w2gviA-crDj1CDjp8


COPY requirements.txt /requirements.txt

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

EXPOSE 8000

RUN adduser --disabled-password --gecos '' myuser