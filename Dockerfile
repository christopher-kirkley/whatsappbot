FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash nano vim
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
