FROM tiangolo/uwsgi-nginx:python3.8-alpine
RUN apk --update add bash nano
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app /app
RUN pip install -r /var/www/requirements.txt

