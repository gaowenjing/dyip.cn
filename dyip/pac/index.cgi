#!/bin/sh
echo
pacfile="gfwlist.pac"
head -4 $pacfile
cat custom.txt
awk '{ if (NR > 4) { sub("PROXY", "'"PROXY $QUERY_STRING;"'"); print }}' $pacfile
