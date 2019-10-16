#!/bin/ash

if [ "$QUERY_STRING" = "autorefresh=on" ] ; then
:echo 'refresh: 1;'
fi
echo

cat <<EOF
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
<style>
body { background: black ; color: white; white-space:pre; font-family:monospace; }
a { color: grey; }
p { font-size:200%; }
</style>
<script>
var xmlhttp;
if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/", false);
    xmlhttp.send(null);
}
</script>
</head>
<body><form action="./" ><input type=text  name="wol" value="pc"></input><input type=submit value="wol"></input></form>
<form action="./" ><input type=text  name="wol" value="ssd"></input><input type=submit value="wol"></input></form>
EOF
if [ "$QUERY_STRING" = "autorefresh=on" ] ; then
cat <<EOF
<form><input type=hidden name=autorefresh value=off></input><input type=button value="refresh off" onclick="submit();"></input></form>
EOF
else
cat <<EOF
<form><input type=hidden name=autorefresh value=on></input><input type=button value="refresh on" onclick="submit();"></input></form>
EOF
fi
if [ "$QUERY_STRING" = "wol=pc" ] ; then
    etherwake -v -i br-lan -b 50:e5:49:b2:50:c6 && echo "<p>Packet Send.</p>"
fi
if [ "$QUERY_STRING" = "wol=ssd" ] ; then
    etherwake -v -i br-lan 70:4d:7b:2f:c4:dd && echo "<p>Packet Send.</p>"
fi

ping -w 1 -c 1 192.168.199.206 && echo "<p>it's on.</p>" || echo "<p>It's off.</p>"


cat <<EOF
</body>
</html>
EOF
