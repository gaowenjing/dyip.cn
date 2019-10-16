#!/bin/ash

### header ###
echo 'content-type: text/html; charset=utf8'
echo

mac=${QUERY_STRING##mac=}
### get post data
if [ "$REQUEST_METHOD" = "POST" ] ; then
  read -n $CONTENT_LENGTH POST_STRING
  mac=$(echo ${POST_STRING##mac=} | sed 's/%3A//g' )
fi

if [ "$mac" == "" ] ; then 
  cat <<EOF
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
<style>
body { background: black ; color: white; white-space:pre; font-family:monospace; } 
a { color: grey; }
#mac { background:black; color:white;}
</style>
<script>
function query() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("result").innerHTML = this.responseText;
     if (! this.responseText ) document.getElementById("result").innerHTML = "no result";
    }
  };
  var q =  document.getElementById("mac").value;
  xhttp.open("GET", "/mac/?"+q, true);
  xhttp.send();
}
</script>
</head>
<body>

<!--
<form method="post" action="./">
input mac address<textarea name=mac >00:11:22:33:44:55</textarea><input type=submit></input>
</form>
--!>
<textarea id=mac onclick="document.getElementById('mac').value='';">00:11:22:33:44:55</textarea>
<button onclick=query()>lookup mac address</button>
<div id=result></div>
</body></html>

EOF
fi

if [ "$mac" != "" ] ; then 
  maca=${mac//[: .-]/}
  macb=$( echo ${maca::6} | awk '{ print toupper($0) }' )

  sqlite3 mac/oui.db "select cname from oui where mac = '$macb' limit 1;"
fi
