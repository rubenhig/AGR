FROM ubuntu:22.04

USER root
RUN apt update 
RUN apt install net-tools && apt install -y iputils-ping && apt install -y iproute2 coreutils iptables

RUN sysctl net.ipv4.ip_forward=1