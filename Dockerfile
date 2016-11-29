FROM ubuntu:16.04
MAINTAINER jairomatias

ARG SUPERSET_VERSION

ENV SUPERSET_VERSION ${SUPERSET_VERSION:-0.13.2}

RUN apt-get update && apt-get install -y \
      python \
      python-dev \
      python-pip \
      libsasl2-dev \
      libldap2-dev \
      libssl-dev \
      libmysqlclient-dev \
      libffi-dev \
      libpq-dev \
    && pip install \
      superset==$SUPERSET_VERSION \
      mysqlclient==1.3.9 \
      python-ldap==2.4.28 \
      psycopg2==2.6.2 \
      redis==2.10.5 \
      sqlalchemy-redshift==0.5.0

# Default config
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PATH=$PATH:/home/superset/.bin \
    PYTHONPATH=/home/superset/superset_config.py:$PYTHONPATH \
    SQLALCHEMY_DATABASE_URI=sqlite:////home/superset/.superset/superset.db

# Run as superset user
WORKDIR /home/superset
COPY superset .
RUN addgroup superset && APPGROUP=`grep "superset" /etc/group|cut -d: -f3` && \
    adduser --system --home /home/superset --gid $APPGROUP superset && \
    mkdir /home/superset/.superset && \
    touch /home/superset/.superset/superset.db && \
    chown -R superset:superset /home/superset
USER superset

# Deploy
EXPOSE 8088
HEALTHCHECK CMD ["curl", "-f", "http://localhost:8088/health"]
ENTRYPOINT ["superset"]
CMD ["runserver"]

