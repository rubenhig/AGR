vtysh << EOF
configure terminal
ip route 10.0.0.0/24 10.1.0.1
ip route 10.0.1.0/24 10.1.0.1
ip route 10.0.2.0/24 10.1.0.1
ip route 10.0.3.0/24 10.1.0.1
exit
EOF