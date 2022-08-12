FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD exporter.py exporter.py

CMD ["python", "-u", "exporter.py"]

