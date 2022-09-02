FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install software-properties-common --yes
RUN apt-get install build-essential wget -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip
RUN mkdir /qualdo
ADD ./requirements.txt /qualdo/requirements.txt
WORKDIR /qualdo
RUN pip install -r /qualdo/requirements.txt
ADD ./app_run.py /qualdo/app_run.py
ENV HOME /qualdo
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app_run:app", "--workers", "1", "--worker-class", "eventlet", "--reload", "--threads", "25", "--timeout", "660"]
# CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app_run:app", "--worker-class", "eventlet", "--reload"]