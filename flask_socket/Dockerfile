FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install software-properties-common --yes
RUN apt-get install build-essential wget -y
RUN apt-get install python3-pip -y
RUN pip install --upgrade pip
RUN mkdir /qualdo
ADD ./requirements.txt /qualdo/requirements.txt

RUN pip install -r /qualdo/requirements.txt
ADD ./app_runner.py /qualdo/app_runner.py
ADD ./api_controller.py /qualdo/api_controller.py
ADD ./cache.py /qualdo/cache.py
ADD ./socket_controller.py /qualdo/socket_controller.py
ADD ./log_utils.py /qualdo/log_utils.py

WORKDIR /qualdo
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app_runner:app", "--workers", "1", "--worker-class", "eventlet", "--threads", "25", "--timeout", "660"]
# CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app_run:app", "--worker-class", "eventlet", "--reload"]