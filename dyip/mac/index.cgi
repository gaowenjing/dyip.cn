#!/bin/ash

### header ###
#echo 'content-type: text/html; charset=utf8'
echo

mac=$QUERY_STRING

maca=${mac//[: .-]/}
macb=$( echo ${maca::6} | awk '{ print toupper($0) }' )

#echo $macb

sqlite3 oui.db "select cname from oui where mac = '$macb' limit 1;"

updatedb() {
  OUI_URL='https://standards.ieee.org/develop/regauth/oui/oui.csv'
  MAM_URL='https://standards.ieee.org/develop/regauth/oui28/mam.csv'
  OUI36_URL='https://standards.ieee.org/develop/regauth/oui36/oui36.csv'

  for url in $OUI_URL $MAM_URL $OUI36_URL ; do curl -k -LO $url ; done
}
