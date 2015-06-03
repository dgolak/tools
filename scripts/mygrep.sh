#!/usr/bin/env bash

GREEN='\033[0;32m'
LIGHT_GREEN='\033[1;32m'
CYAN='\033[0;36m'

NC='\033[0m' # No Color

argc=("$#")
if [ $argc = 0 ]
then
    echo -e "usage ./mygrep <options>"
    echo -e "./mygrep <file.exe> - shows every predefined rules"
    echo -e "./mygrep <file.exe> <any_string> - search any_string and every rules"
    echo -e "./mygrep <file.exe> <any_string> <some_chars> - search and show only <any_string>\n"
    exit;
fi

if [ -a $1 ]
then

if [ $argc -lt 3  ]
 then
    clear;

    #search URL
    url=$(strings -a -e{b,l} $1|grep -i -E "[a-z0-9]+\.[a-z0-9]+\.[a-z]{2,3}" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"URL"$GREEN"...\t\t\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "[a-z0-9]+\.[a-z0-9]+\.[a-z]{2,3}" --color=always

    #search HTTP
    url=$(strings -a -e{b,l} $1|grep -i -E "http" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"HTTP"$GREEN"...\t\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "http" --color=always

    #search adress IP
    url=$(strings -a -e{b,l} $1|grep -i -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"ADDRESS IP"$GREEN"...\t\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" --color=always

    # search password
    url=$(strings -a -e{b,l} $1|grep -i -E "password" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"PASSWORD"$GREEN" strings...\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "password" --color=always

    #search pass
    url=$(strings -a -e{b,l} $1|grep -i -E "pass" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"PASS"$GREEN"'word strings...\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "pass" --color=always

    #search pass
    url=$(strings -a -e{b,l} $1|grep -i -E "user" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"USER"$GREEN" strings...\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "user" --color=always

    #search exe file
    url=$(strings -a -e{b,l} $1|grep -i -E "[a-zA-Z0-9]+\.exe" --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN"*.exe"$GREEN"'...\t\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E "[a-zA-Z0-9]+\.exe" --color=always
fi

    #search param2
    if [ $2 ]
    then
	url=$(strings -a -e{b,l} $1|grep -i -E $2 --color=always|wc -l)
    if [ $url -eq 0 ]
    then
	url="Not found";
    else
	url="Found "$url;
    fi
    echo -e "$LIGHT_GREEN[INFO]$GREEN Searching "$CYAN""$2""$GREEN" strings...\t\t["$url"]$NC"
    strings -a -e{b,l} $1|grep -i -E $2 --color=always
    fi
else
echo "No such file \""$1"\""
fi


