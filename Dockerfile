FROM python:3.7.11-alpine3.13
EXPOSE 8888
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
COPY . /home/src
WORKDIR /home/src
CMD ["flask","run","--port=8888", "--host=0.0.0.0"]