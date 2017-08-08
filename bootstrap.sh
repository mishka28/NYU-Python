#!/usr/bin/env bash








apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim wget git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install bpython --assume-yes

#pip for getting csv
apt-get install python3-pip --assume-yes
pip3 install --upgrade pip
pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
pip3 install pandas
pip3 install matplotlib
pip3 install numpy
pip3 install xlrd
