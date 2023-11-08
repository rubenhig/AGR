FROM ubuntu:22.04

USER root
RUN apt update 
RUN apt-get update && aptget install net-tools && apt-get install -y iputils-ping && apt-get install -y iproute2 coreutils iptables

RUN sysctl net.ipv4.ip_forward=1