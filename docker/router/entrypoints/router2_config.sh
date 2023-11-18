#!/bin/bash

# Pagina para hacer troubleshooting de frr: https://docs.frrouting.org/en/stable-9.0/setup.html#crash-logs
service frr start


vtysh << EOF
conf t 
ip route 10.0.0.0/8 10.2.0.2
end
EOF



/bin/sleep infinity