#!/bin/ash

### header ###
echo 'content-type: text/html; charset=utf8'
echo

if [ "$QUERY_STRING" = "myip" ] ; then 
  echo $REMOTE_ADDR
else
  curl -kL 192.168.1.3/ip.php?$QUERY_STRING
fi
