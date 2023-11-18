#!/bin/bash

# Pagina para hacer troubleshooting de frr: https://docs.frrouting.org/en/stable-9.0/setup.html#crash-logs
service frr start


vtysh << EOF
conf t 
ip route 10.5.0.0/29 10.1.0.2
ip route 10.0.0.0/23 10.2.0.1
ip route 10.0.2.0/23 10.3.0.1
end
EOF



/bin/sleep infinity