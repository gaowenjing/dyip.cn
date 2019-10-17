#!/bin/ash

echo
parse_qs (){
  eval $( echo $1 | awk -F'&' '{ for (i =1; i<=NF; i++) printf("%s\n", $i) ; }')
}
parse_qs "$QUERY_STRING"

#pw
. ../../dyip_login_pw

if [ "$ping" = "pc" ] ; then
    [ "$code" = "$pw" ] && ping -w 1 -c 1 192.168.199.206 && echo "<p>it's on.</p>" || echo "<p>It's off.</p>"
    exit
fi
if [ "$ping" = "ssd" ] ; then
   [ "$code" = "$pw" ] && ping -w 1 -c 1 192.168.199.206 && echo "<p>it's on.</p>" || echo "<p>It's off.</p>"
    exit
fi

if [ "$wol" = "pc" ] ; then
    [ "$code" = "$pw" ] && etherwake -v -i br-lan -b 50:e5:49:b2:50:c6 && echo "<p>Packet Send.</p>  $(date)"
    exit
fi
if [ "$wol" = "ssd" && "$code" = "$pw" ] ; then
    [ "$code" = "$pw" ] && etherwake -v -i br-lan 70:4d:7b:2f:c4:dd && echo "<p>Packet Send.</p>  $(date)"
    exit
fi

##### html start #####

cat <<EOF
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
<title>wol</title>
<style>
body,#code { background: black ; color: white; white-space:pre; font-family:monospace; }
a { color: grey; }
p { font-size:120%; }

</style>
<script>
var host, code, thevar;
function wakeup(host) {
  var xhttp = new XMLHttpRequest();
  code = document.getElementById("code").value;
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("result").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "?wol="+host+"&code="+code, true);
  xhttp.send();
}
function ping(host) {
  var xhttp = new XMLHttpRequest();
  code = document.getElementById("code").value;
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("ping_result").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "?ping="+host+"&code="+code, true);
  xhttp.send();
}
function reping(host) {
  wakeup(host);
  clearInterval(thevar);
  thevar = setInterval(function(){ ping( host ); }, 1000) ;
}
</script>
</head>
<body>
<input id="code"></input>
<script>
</script>
<button onclick="reping('pc')">wakeup pc</button> <button onclick="reping('ssd')">wakeup ssd</button>
<div id="result"></div>
<div id="ping_result"></div>
</body>
</html>
EOF
