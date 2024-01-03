#!/bin/sh

fluentd -c fluentd/etc/fluent.conf &

ip route change default via 10.100.0.1 

sleep infinity