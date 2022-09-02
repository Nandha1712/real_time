FROM ubuntu:20.04

USER root
RUN apt-get update
RUN apt-get install -y nginx nodejs
RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/

ADD build /usr/share/nginx/html/
ADD build /var/www/html/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
EXPOSE 80
CMD service nginx start