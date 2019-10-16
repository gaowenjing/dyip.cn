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
<title>ip and mac address lookup tool</title>
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

function query_ip() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("result").innerHTML = this.responseText;
     if (! this.responseText ) document.getElementById("result").innerHTML = "no result";
    }
  };
  var q =  document.getElementById("ip").value;
  xhttp.open("GET", "/ip/?"+q, true);
  xhttp.send();
}
</script>
</head>
<body>

<input id=ip value='1.1.1.1'></input>

<textarea id=mac onclick="document.getElementById('mac').value='';">00:11:22:33:44:55</textarea>
<button id="btn" onclick=query()>lookup mac address</button>
<div id=result></div>

<script>
// Get the input field
var input = document.getElementById("ip");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    //document.getElementById("btn").click();
    query_ip();
  }
});
</script>
</body></html>

EOF
fi

if [ "$mac" != "" ] ; then 
  maca=${mac//[: .-]/}
  macb=$( echo ${maca::6} | awk '{ print toupper($0) }' )

  sqlite3 mac/oui.db "select cname from oui where mac = '$macb' limit 1;"
fi
