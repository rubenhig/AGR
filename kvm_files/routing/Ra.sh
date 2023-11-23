vtysh << EOF
configure terminal
ip route 0.0.0.0/0 10.1.0.1
exit
EOF