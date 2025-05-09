#!/bin/bash

FISH="$1"
PICTURE="$2"
DATE="$3"

FILE="/home/rybokot/Desktop/northernpikee.github.io/index.html"
cp "$FILE" "/home/rybokot/Desktop/northernpikee.github.io/prv.html"
N=$(grep -n "</dl>" "$FILE" || cut -d: -f1 )
TEXT="            <dt> fish of the day $DATE </dt> 
                  <dd> $FISH </dd> 
                  <dd> <img src=\"$PICTURE\" alt=\"fish\" width=\"60%\"></dd> 
                  <br> "

awk -v text="$TEXT" ' \
/<dl>/ {print; print text; next} \
{print} \
' "$FILE" > "$FILE.tmp"
mv "$FILE.tmp" "$FILE"

echo "$FISH", "$DATE"  >> "/home/rybokot/Desktop/northernpikee.github.io/sortedfish.txt"

firefox "$FILE"
