FROM mysql:latest

COPY envsql/.env .env

ARG MYSQL_DB=$MYSQL_DATABASE
ARG MYSQL_ROOT=$MYSQL_ROOT_PASSWORD

ENV DATABASE=$MYSQL_DB
ENV PASSWORD=$MYSQL_ROOT

RUN chown -R mysql:root .env
RUN chown -R mysql:root /etc/mysql/
RUN chown -R mysql:root /var/lib/mysql/
RUN chown -R mysql:root /var/lib/mysql-files

ADD init.sql /var/lib/mysql-files/init.sql
ADD known_exploited_vulnerabilities.csv /var/lib/mysql-files/known_exploited_vulnerabilities.csv
ADD init.sql /docker-entrypoint-initdb.d

RUN sed -i 's/MYSQL_DATABASE/'cve'/g' /var/lib/mysql-files/init.sql

EXPOSE 3306:3306 

RUN pwd
RUN ls -a
RUN cat ./.env
