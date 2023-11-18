FROM ubuntu:22.04

RUN apt-get update && apt-get install -y iputils-ping && apt-get install -y iproute2 iptables
RUN apt-get install net-tools -y && apt-get install iproute2 -y && apt-get install iputils-ping && apt-get install -y traceroute
COPY ./ip_route.sh /scripts/ip_route.sh
RUN chmod +x /scripts/ip_route.sh

CMD [ "/bin/bash" ]