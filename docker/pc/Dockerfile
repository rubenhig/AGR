FROM ubuntu:22.04

USER root
RUN apt update 
RUN apt install net-tools -y && apt install iproute2 -y && apt install iputils-ping

COPY ./ip_route.sh /scripts/ip_route.sh