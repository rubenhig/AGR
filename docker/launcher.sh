#!/bin/bash


docker compose up -d

docker exec pc0 sh /scripts/ip_route.sh
#docker exec pc0 ip route add 10.0.0.0/8 via 10.0.0.1