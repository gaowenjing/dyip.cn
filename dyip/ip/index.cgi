#!/bin/ash

### header ###
echo 'content-type: text/html; charset=utf8'
echo

curl 192.168.1.3/?$QUERY_STRING
