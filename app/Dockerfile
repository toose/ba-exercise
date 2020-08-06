# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S app && adduser -S app -G app

# set timezone data
RUN apk add --update tzdata
ENV TZ=America/New_York

# create the appropriate directories
ENV APP_HOME=/usr/local/src
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# copy project and install dependencies
COPY . $APP_HOME
RUN pip install -r requirements.txt

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app
