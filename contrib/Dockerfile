# Docker
# sudo docker build -t dwagon/home_status .
# sudo docker run -p 127.0.0.1:8000:8000 -v /var/log/docker/home_status:/var/log dwagon/home_status
# sudo docker run -t -i -t dwagon/home_status /bin/bash
FROM ubuntu
MAINTAINER dougal.scott@gmail.com 
RUN apt-get update
RUN apt-get install -y python-dev 
RUN apt-get install -y git
RUN apt-get install -y gunicorn
RUN apt-get install -y python-pip

RUN git clone https://github.com/dwagon/home_status.git
WORKDIR /home_status
RUN pip install -r requirements.txt
ADD apikey.py /home_status/apikey.py

EXPOSE 8000
CMD ["/usr/bin/gunicorn", "-w", "4", "-b", "127.0.0.1:8000", "--log-file", "/var/log/gunicorn.log", "sck:app"]

#EOF
