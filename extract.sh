#!/bin/bash

url=$(readlink -f $1)

data=$(date)

mkdir images/"$data"
cd images/"$data"
pdfimages $url skan
mogrify -format png *
find -type f -iname '*.ppm' -delete
touch ../new
echo $data > ../new
rm $url
