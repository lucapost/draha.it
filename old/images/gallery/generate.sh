#!/bin/bash

mkdir thumbs

for a in full/*.jpg  ; do
	echo $a
	name=`echo $a |sed -e 's/.jpg//i;s/full\///'`
        convert -thumbnail !60x60 -unsharp 0x.5 $a thumbs/$name.jpg 
done


exec 3<&0
exec 0<data.txt

while read line; do

	name=`echo $line | cut -d: -f1`
	altit=`echo $line | cut -d: -f2`
	titleit=`echo $line | cut -d: -f3`

	echo "<li><a href=\"/images/gallery/full/$name\" title=\"$titleit\"><img src=\"/images/gallery/thumbs/$name\" alt=\"$altit\" title=\"$titleit\" /></a></li>"  >> tmp.txt

done

exec 0<&3

cat tmp.txt
rm tmp.txt
