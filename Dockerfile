FROM httpd


RUN apt-get update -y

COPY ./config/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./html /var/www/html
RUN chmod -R a+xr /var/www/html

# Carrega módulo CGI
RUN echo 'LoadModule cgi_module /usr/local/apache2/modules/mod_cgi.so' >>/usr/local/apache2/conf/httpd.conf

# Define usuário e grupo para execução do Apache
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_RUN_DIR /var/www/html

#  Pacotes para obter informações sobre o sistema
RUN apt-get install procps -y && apt-get install net-tools -y \
  && apt-get install lm-sensors -y && apt-get install vim -y

# Configura hora
ENV TZ=America/Sao_Paulo

# Exibe porta 80
EXPOSE 80

# Mantém o servidor em execução
ENTRYPOINT ["/usr/local/apache2/bin/apachectl", "-D", "FOREGROUND"]

