FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano vim
COPY ./requirements.txt /var/www/requirements.txt
COPY . /app
RUN pip install -r /var/www/requirements.txt

