#!/bin/ash

### header ###
echo 'content-type: text/html; charset=utf8'
echo

#### html start ####
cat <<EOF
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
<title>ip and mac address lookup tool</title>
<style>
li, body, textarea {
  background: black;
  color: white;
  font-family:monospace;
  display: inline;
} 
a {
  color: #bbb;
}
li {
  padding: 10px;
}
ul {
  padding: 0 10px;
}
</style>
<script>
function query(mode) {
  var result = document.getElementById('result');
  var btn = document.getElementById('btn');
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     btn.innerHTML = 'lookup';
     btn.removeAttribute('disabled');
     result.innerHTML = this.responseText + '<br>' + result.innerHTML;
     if (! this.responseText ) result.innerHTML = 'no result!' + '<br>' + result.innerHTML;
    } else {
     btn.innerHTML = 'loading';
     btn.setAttribute('disabled', '');
    }
  };
  if (mode == 'mac'){
    var q =  document.getElementById("mac").value;
    xhttp.open("GET", "/mac/?"+q, true);
  }
  if (mode == 'ip') {
    var q =  document.getElementById("ip").value;
    xhttp.open("GET", "/ip/?"+q, true);
  }
  xhttp.send();
}
</script>
</head>

<body>

<div class="banner">
<ul>
<li><a href="/cmd/">/cmd</a></li>
<li><a href="/d/">/d</a></li>
<li><a href="/c/">/c</a></li>
<li><a href="/pac/">/pac</a></li>
<li><a href="/android/">/android</a></li>
<li><a href="/script/">/script</a></li>
</ul>
</div>

<input id=ip></input>
<br>
<textarea id=mac onclick="document.getElementById('mac').value='';">00:11:22:33:44:55</textarea>
<br>
<button id="btn" onclick=query('mac')>lookup</button>
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
    query('ip');
  }
});
function yourip() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("ip").value = this.responseText;
    }
  };
  xhttp.open("GET", "/ip/?myip", true);
  xhttp.send();
}
yourip();
</script>
</body></html>
EOF
