FROM python:3

ADD app.py /

RUN pip3 install pandas

CMD ["python", "./app.py", "20"]

