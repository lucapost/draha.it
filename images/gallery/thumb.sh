#!/bin/bash

mkdir fullscreen thumbnails

for a in *.jpg  ; do
	name=`echo $a |sed s'/.jpg//'`
	echo $name
#	mogrify -resize 600x -auto-orient -format png $a -path fullscreen $name.png
#        mogrify -resize !60x60 -gravity Center -crop 60x60+0+0 -format png $a -path thumbnails $name.png
        mogrify -thumbnail 60 -unsharp 0x.5 $a -path thumbnails $name.jpg 
#	mogrify -resize 60x60 -auto-orient -background transparent -gravity center -extent 60x60 -format jpg tmp.jpg -path thumbnails $name.jpg
done
