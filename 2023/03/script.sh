#!/bin/bash

file="list.txt"
> file.txt

echo '<!DOCTYPE html>
<html>
<head>

    <link rel="stylesheet" href="../styles.css">

</head>
<body>
<dl>
' >>file.txt

while read line; do
	name=$(echo "$line" | sed -n 's/^\(.*\)\March.*/\1/p')
	date=$(echo "$line" | sed -n 's/.*\March\(.*\)/March\1/p')
        day=$(echo "$date" | sed -n 's/.* \([0-9]*\),.*/\1/p')
	echo "<dt> The fish of the day $date </dt>">> file.txt
	echo "<dd> $name </dd>" >> file.txt
	echo "<dd> <img src=$day.jpg> </dd> " >> file.txt
	echo "<br>" >>file.txt 
 done <"$file" 


 echo '</dl>
<a href=../../index.html>Home</a>
</body>
' >>file.txt
