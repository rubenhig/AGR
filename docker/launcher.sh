#!/bin/bash

docker compose up -d
docker exec pc0 sh /scripts/ip_route.sh
docker exec pc1 sh /scripts/ip_route.sh
docker exec pc2 sh /scripts/ip_route.sh
docker exec pc3 sh /scripts/ip_route.sh