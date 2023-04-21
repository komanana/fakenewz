FROM node:14 AS build
WORKDIR /app
ENV VUE_APP_SERVER http://170.64.130.168/api/
RUN apt-get update && apt-get install git
RUN git clone -b production https://swan0182:371402Az@github.sydney.edu.au/2022S2-5703/CS06-1.git
RUN cd /app/CS06-1/frontend && npm install && npm run build

FROM nikolaik/python-nodejs:python3.8-nodejs14
RUN apt-get update && apt-get install git libpq-dev nginx vim net-tools -y
COPY --from=build /app/CS06-1 /home/CS06-1

ADD run.sh /home/CS06-1/
ADD nginx.conf /etc/nginx/sites-available/default
#ADD settings.py /home/CS06-1/backend/django_core/settings.py
RUN pip3 install -r /home/CS06-1/backend/requirements.txt
WORKDIR /home/CS06-1
RUN chmod 777 /home/CS06-1/backend/static/upload -R

CMD ["bash","run.sh"]