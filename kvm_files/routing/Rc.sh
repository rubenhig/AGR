vtysh << EOF
configure terminal
ip route 0.0.0.0/0 10.2.0.2
exit
EOF