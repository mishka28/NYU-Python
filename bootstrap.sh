#!/usr/bin/env bash

apt-get install build-essential gcc --assume-yes
apt-get update --fix-missing
apt-get install vim wget git zlib1g-dev --assume-yes
apt-get install python3 --assume-yes
apt-get install python3-venv --assume-yes
apt-get install bpython --assume-yes
apt-get install python3-tk --assume-yes
# apt-get install virtualenv --assume-yes

#pip for getting csv
apt-get install python3-pip --assume-yes
pip3 install --upgrade pip
pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
pip3 install pandas
pip3 install matplotlib
pip3 install numpy
pip3 install xlrd
pip3 install plotly
pip3 install pandas-datareader
pip3 install scipy
pip3 install Flask-FlatPages
pip3 install Frozen-Flask
pip3 install Flask-Markdown
pip3 install micawber
pip3 install peewee




export RUN_USER="ubuntu"
export RUNUSER_PROG="/sbin/runuser"

export COMMAND=$(cat <<-'HERE1a'
    echo "\"echo \"in .profile\" >> $HOME/.profile\""
    echo "\"echo \"in .bashrc\" >> $HOME/.bashrc\""
HERE1a
)

${RUNUSER_PROG} -l ${RUN_USER} -c "${COMMAND}"

