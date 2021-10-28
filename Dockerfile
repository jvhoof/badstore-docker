# Dockerfile for Badstore
# Apache HTTP foreground https://github.com/chriswayg/apache-php

FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    apache2 \
    mariadb-server \
    supervisor \ 
    libclass-dbi-mysql-perl \
    locales && \
    apt-get clean && rm -r /var/lib/apt/lists/*

COPY apache2/conf/badstore.conf /etc/apache2/sites-available/

# Setup Apache
RUN a2enmod ssl \
	    cgid \
            rewrite && \
    a2dissite 000-default && \
    a2ensite badstore && \
    mkdir -p /data/apache2/log && \
    mkdir -p /data/apache2/htdocs && \
    touch /data/apache2/log/access.log && \
    touch /data/apache2/log/error.log && \
    chown -R www-data:www-data /data/apache2/log
#    ln -sf /dev/stdout /data/apache2/log/access.log && \
#    ln -sf /dev/stderr /data/apache2/log/error.log

COPY apache2/cgi-bin/ /data/apache2/cgi-bin/
COPY apache2/data/ /data/apache2/data/
COPY apache2/htdocs/ /data/apache2/htdocs/
COPY apache2/icons/ /data/apache2/htdocs/icons/
RUN chown www-data /data/apache2/data/guestbookdb
RUN chown www-data /data/apache2/data/uploads
RUN chown www-data:mysql /data/apache2/htdocs/backup

# Setup Mysql

# These scripts will be used to launch MariaDB and configure it
# securely if no data exists in /data/mariadb
RUN mkdir -p /data/mariadb/bin && \
	mkdir -p /data/mariadb/data && \
	mkdir -p /data/mariadb/log && \
	mkdir -p /data/mariadb/run
ADD mariadb/conf/my.cnf /data/mariadb/etc/my.cnf
ADD mariadb/bin/mariadb-start.sh /data/mariadb/bin/mariadb-start.sh 
ADD mariadb/bin/badstore-setup.sql /data/mariadb/bin/badstore-setup.sql
RUN chmod u=rwx /data/mariadb/bin/mariadb-start.sh
RUN chown -R mysql:mysql /data/mariadb/bin/mariadb-start.sh /data/mariadb/bin/badstore-setup.sql /data/mariadb

# Debian maintenance
RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# clean packages
RUN apt-get clean
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

WORKDIR /var/www/html

EXPOSE 80

# copy supervisor conf
ADD supervisor/conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# By default start up apache in the foreground, override with /bin/bash for interative.
# start supervisor
CMD ["/usr/bin/supervisord"]
