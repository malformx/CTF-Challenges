FROM ubuntu

# Installations
ENV http_proxy=http://192.168.100.100:3128
ENV https_proxy=http://192.168.100.100:3128


RUN apt update && apt install vsftpd -yy

RUN mkdir -p /var/run/vsftpd/empty
RUN mkdir -p /opt/flag
RUN echo "ZCTF2023{A_P0tato_Flaggg!}" > /opt/flag/flag124455212.txt

COPY vsftpd.conf /etc/vsftpd.conf


ENV http_proxy=""
ENV https_proxy=""

EXPOSE 21

CMD ["vsftpd"]
