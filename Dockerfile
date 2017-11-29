FROM python:3

ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN mkdir /usr/src/app
WORKDIR /usr/src/app/

COPY messenger/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

COPY messenger /usr/src/app/
