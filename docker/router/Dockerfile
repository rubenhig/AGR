FROM ubuntu:22.04

USER root
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y net-tools &&  apt-get install -y iputils-ping \
    && apt-get install -y iproute2 coreutils iptables && apt-get install -y frr syslog-ng
RUN sysctl net.ipv4.ip_forward=1 && sysctl -p 

COPY entrypoints/router0_config.sh /scripts/router0_config.sh
COPY entrypoints/router1_config.sh /scripts/router1_config.sh
COPY entrypoints/router2_config.sh /scripts/router2_config.sh
COPY entrypoints/router3_config.sh /scripts/router3_config.sh

RUN chmod +x /scripts/router0_config.sh /scripts/router1_config.sh /scripts/router2_config.sh /scripts/router3_config.sh

CMD ["/bin/bash"]