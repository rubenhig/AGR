FROM ubuntu:22.04

RUN apt-get update && apt-get install -y iputils-ping && apt-get install -y iproute2 coreutils iptables nodejs npm syslog-ng
RUN apt-get install git -y

COPY bootstrap.sh /scripts/bootstrap.sh
RUN chmod +x /scripts/bootstrap.sh

CMD [ "/bin/bash" ]