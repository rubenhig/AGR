vtysh << EOF
configure terminal
ip route 10.0.0.0/24 10.3.0.2
ip route 10.0.1.0/24 10.3.0.2
ip route 10.4.0.0/30 10.3.0.2
ip route 0.0.0.0/0 10.3.0.2
exit
EOF