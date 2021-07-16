FROM python:3.7.11-alpine3.13 AS build
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
COPY . /home/src
WORKDIR /home/src
RUN python3 test.py

FROM python:3.7.11-alpine3.13
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
COPY --from=build /home/src /app
WORKDIR /app
EXPOSE 8888
CMD ["flask","run","--port=8888", "--host=0.0.0.0"]