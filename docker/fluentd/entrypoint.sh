#!/bin/sh

fluentd -c fluentd/etc/fluent.conf &

ip route add default via 10.100.0.1

sleep infinity