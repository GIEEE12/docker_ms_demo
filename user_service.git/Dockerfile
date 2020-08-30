FROM python:3-alpine

MAINTAINER demo lbg

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
	--update-cache \
    	--repository https://alpine.global.ssl.fastly.net/alpine/v3.8/community \
     bash \
     curl \
     py-mysqldb \
     gcc \
     libc-dev \
     mariadb-dev \
     nodejs \
     npm \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app/package.json /app/package.json
RUN npm install

COPY ./app /app

CMD ["python", "app.py"]

