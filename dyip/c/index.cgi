#!/bin/ash

. ../../dyip_login_pw
hash_login_pw()
{
   echo $login_pw$(date +%D%H%M) | md5sum | awk '{print $1}'
}

readcookie()
{
   echo $HTTP_COOKIE | awk -F'; ' '{
        for (i=1; i< NF; i++) {
           split( $i, a , "=" );
           if ( a[1] == "login" )
              print a[2];
        }
     }'
}


### header ###
echo 'content-type: text/html; charset=utf8'

### get post data
if [ "$REQUEST_METHOD" = "POST" ] ; then
  read -n $CONTENT_LENGTH POST_STRING
  ### logout ###
  if [ "$POST_STRING" = "code=logout" ] ; then
     echo 'set-cookie: login=;'
     echo 'refresh: 0'
  fi

  ### login ###
  if [ "$POST_STRING" = "code=$login_pw" ] ; then
     login_hash=$(hash_login_pw)
     echo "set-cookie: login=$login_hash; max-age=60"
     echo 'refresh: 0'
  fi
fi

echo

### html start ####
cat <<EOF
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
<title>download</title>
<style>
body { background: black ; color: white; white-space:pre; font-family:monospace; } 
a { color: grey; }
</style>
</head>
<body>
EOF


### verify cookie value and return content ###
if [ "$(readcookie)" = "$(hash_login_pw)" ]; then
  cat <<EOF
<form method="post" action="./">
<input type=hidden name=code value=logout></input><input type=submit value=logout></input>
</form>
EOF
  ls -lh | awk '{
                 name=$9;
                 for (col=10; col<=NF; ++col )
                    name=name" "$col;
                 printf("%s\t%s %s %s\t<a href=\"%s\">%s</a><br>", $5,$6,$7,$8,name,name)
           }'

### failed login ####
else
  cat <<EOF
<a href="/">/</a>
<form method="post" action="./">
code<input type=password name=code ></input><input type=submit value=login></input>
</form>
EOF
fi

echo '</body></html>

