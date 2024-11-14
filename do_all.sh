#!/bin/bash
echo "python3 -m pip install --upgrade pip"
echo "python3 -m pip uninstall opencv-contrib-python opencv-contrib-python-headless"
for v in $(cat candidate.txt)
do
  echo "#" $v;
  echo "python3 -m pip uninstall opencv-python opencv-python-headless"
  echo "rm -r venv/lib/python3.8/site-packages/__pycache__/"
  echo "python3 -m pip install opencv-python==$v && python3 circular.py $v" ;
done
