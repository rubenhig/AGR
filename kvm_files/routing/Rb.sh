vtysh << EOF
configure terminal
ip route 10.4.0.0/30 10.1.0.2
ip route 10.0.0.0/23 10.2.0.1
ip route 10.0.2.0/23 10.3.0.1
exit
EOF