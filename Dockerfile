FROM python:3.8-slim-buster
LABEL maintainer="akimrx"

RUN pip3 install redis

COPY ./app.py /root/app.py
RUN chmod +x /root/app.py

WORKDIR /root
CMD [ "python3", "./app.py" ]
