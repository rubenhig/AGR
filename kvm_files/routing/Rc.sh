vtysh << EOF
configure terminal
ip route 10.0.2.0/24 10.2.0.2
ip route 10.0.3.0/24 10.2.0.2
ip route 10.4.0.0/30 10.2.0.2
exit
EOF