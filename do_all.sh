#!/bin/bash
for v in $(cat candidate.txt)
do
  echo "#" $v;
  echo python3 -m pip install opencv-python==$v;
  echo python3 circular.py $v;
done