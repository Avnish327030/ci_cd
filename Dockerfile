FROM python:3.7
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt