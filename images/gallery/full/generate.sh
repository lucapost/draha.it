#!/bin/bash

#sed '/^$/d' $1/data.txt > tmp.txt

#exec 3<&0
#exec 0<tmp.txt

#while read line; do

for i in *.jpg ; do

	name=$i

	name=`echo $line | cut -d: -f1`
	altit=`echo $line | cut -d: -f2`
	titleit=`echo $line | cut -d: -f3`

	echo "<li><a href=\"/images/gallery/full/$i\" title=\"$titleit\"><img src=\"/images/gallery/thumbs/$i\" alt=\"$altit\" title=\"$titleit\" /></a></li>"  >> it.txt

done

#exec 0<&3

cat it.txt
