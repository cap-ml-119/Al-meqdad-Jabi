FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt  .
RUN pip3 install -r requirements.txt

COPY /app .

RUN apt-get update && apt-get install make
RUN make install

CMD ["python", "main.py"]
