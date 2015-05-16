#!/bin/bash
    curl -s --cookie-jar cookie.txt 'http://example.com/programmation/ch8/' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: pl,en-US;q=0.7,en;q=0.3' -H 'Connection: keep-alive' -H 'Host: challenge01.example.com' -H 'Referer: http://challenge01.example.com/programmation/ch8/' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'  --data 'cametu=asd' > zz.gz;
    r=$(zcat zz.gz|sed -e 's/image\/png;base64,/\n###/g'|grep "###")
    echo $r |sed -e 's/" \/>/\nAAAAAAAAAAAAAAAAa/g'|grep -v AAAAAAA |sed -e 's/###//g' |base64 -d > captcha.png

function kapcia(){
    gocr -i captcha.png > output.txt
    captcha=$(cat output.txt|awk '{print $0}')
#    echo "OLD   "$captcha

    curl -s --cookie-jar cookie.txt -X POST 'http://challenge01.example.com/programmation/ch8/' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: pl,en-US;q=0.7,en;q=0.3' -H 'Connection: keep-alive' -H 'Host: challenge01.example.com' -H 'Referer: http://challenge01.example.com/programmation/ch8/' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'  --data "cametu=$captcha" > odp.gz;
    L=$(zcat odp.gz |grep Failed|wc -l)

    if [ $L == "0" ]
	then
	    echo "-------------------------   JEST OK!!!!!!!! " $(zcat odp.gz)
	    exit;
	else
	    r=$(zcat odp.gz|sed -e 's/image\/png;base64,/\n###/g'|grep "###")
	    echo $r |sed -e 's/" \/>/\nAAAAAAAAAAAAAAAAa/g'|grep -v AAAAAAA |sed -e 's/###//g' |base64 -d > captcha.png
	    echo "$1:" $captcha
    fi;
}

COUNTER=0
while [  $COUNTER -lt 10000000 ]; do
    kapcia $COUNTER
    let COUNTER=COUNTER+1
done;



