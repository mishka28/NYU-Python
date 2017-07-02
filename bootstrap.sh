#!/usr/bin/env bash








apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim wget git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install python3-numpy --assume-yes
apt-get install bpython --assume-yes

#pip for getting csv
apt-get install python3-pip --assume-yes
pip3 install --upgrade pip
