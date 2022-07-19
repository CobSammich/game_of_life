#!/bin/bash

for file in images/*.pdf;
do
    base="$(basename -s .pdf $file)"
    echo pdftoppm -png -r 300 $file ./images/$base
    pdftoppm -png -r 300 $file ./images/$base
done

echo convert -delay 30 -loop 0 ./images/*.png life.gif
convert -delay 30 -loop 0 ./images/*.png life.gif
