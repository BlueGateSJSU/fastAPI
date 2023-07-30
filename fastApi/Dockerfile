FROM python:3

WORKDIR /fastapi
ADD requirements.txt /fastapi/requirements.txt
ADD init.sh /fastapi/init.sh
RUN ./init.sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install matplotlib