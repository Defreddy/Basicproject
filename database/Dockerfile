FROM mysql:latest

RUN chown -R mysql:root /var/lib/mysql/
RUN chown -R mysql:root /etc/mysql

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD
ARG MYSQL_PORT

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

ADD my.cnf /etc/mysql/my.cnf
ADD init.sql /etc/mysql/init.sql
ADD known_exploited_vulnerabilities.csv /etc/mysql/known_exploited_vulnerabilities.csv

RUN sed -i 's/MYSQL_DATABASE/'basicproject'/g' /etc/mysql/init.sql
RUN cp /etc/mysql/init.sql /docker-entrypoint-initdb.d

EXPOSE $MYSQL_PORT:3306