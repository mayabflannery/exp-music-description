#!/bin/bash

mkdir output

for i in *.mp3; do ffmpeg -ss 0 -to 10 -i "$i" -af "afade=t=in:ss=0:d=1, afade=t=out:st=9:d=1" "output/${i%.*}.mp3" -y; done

