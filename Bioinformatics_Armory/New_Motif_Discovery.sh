#!/bin/bash

meme $1 
line_number=$(awk '/regular expression/{print NR}' meme_out/meme.txt)
echo $(sed -n "$((line_number + 2))p" meme_out/meme.txt)
