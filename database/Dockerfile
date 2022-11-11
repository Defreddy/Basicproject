FROM mysql:latest

RUN chown -R mysql:root /var/lib/mysql/
RUN chown -R mysql:root /var/lib/mysql-files

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD
ARG MYSQL_PORT

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

ADD init.sql /var/lib/mysql-files/init.sql
ADD known_exploited_vulnerabilities.csv /var/lib/mysql-files/known_exploited_vulnerabilities.csv
ADD init.sql /docker-entrypoint-initdb.d

RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /var/lib/mysql-files/init.sql

EXPOSE $MYSQL_PORT:3306 3306 33060 33061

CMD ["mysqld"]