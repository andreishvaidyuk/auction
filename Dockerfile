# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /auction
COPY requirements.txt /auction/
RUN pip install -r requirements.txt
COPY . /auction/