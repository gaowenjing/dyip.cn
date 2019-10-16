#ip nei | awk '/lladdr/{printf ( "%s # ", $0); system ( "curl -k https://dyip.cn/mac/?"$5 ) }'
ip nei | awk '/lladdr/{company = "no result" ; cmd = "curl -sk https://dyip.cn/mac/?"$5 ; cmd | getline company ; close(cmd) ; printf ( "%s # %s\n", $0, company); }'
