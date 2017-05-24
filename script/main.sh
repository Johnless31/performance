#########################################################################
# File Name: main.sh
# Author: ljz
# mail: 18810541175@163.com
# Created Time: Wed 24 May 2017 11:12:13 PM CST
#########################################################################
#!/bin/bash
sed '1,7d' ./output.csv > ./result.csv && python ./main.py
