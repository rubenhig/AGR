#!/bin/bash

ip route change default via ${R_GATEWAY}

/bin/sleep infinity