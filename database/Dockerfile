FROM mysql:latest

RUN --mount=type=secret,id=MYSQL_DATABASE \
  --mount=type=secret,id=MYSQL_ROOT_PASSWORD \
   export MYSQL_DATABASE=$(cat /run/secrets/MYSQL_DATABASE) && \
   export MYSQL_ROOT_PASSWORD=$(cat /run/secrets/MYSQL_ROOT_PASSWORD) &&

RUN chown -R mysql:root /etc/mysql/
RUN chown -R mysql:root /var/lib/mysql/
RUN chown -R mysql:root /var/lib/mysql-files

ADD init.sql /var/lib/mysql-files/init.sql
ADD known_exploited_vulnerabilities.csv /var/lib/mysql-files/known_exploited_vulnerabilities.csv
ADD init.sql /docker-entrypoint-initdb.d

RUN sed -i 's/MYSQL_DATABASE/'cve'/g' /var/lib/mysql-files/init.sql

EXPOSE 3306:3306 

