#!/bin/bash

# Start the pulseaudio server
echo "pulseaudio -D --exit-idle-time=-1"
pulseaudio -D --exit-idle-time=-1

# Load the virtual sink and set it as default
pacmd load-module module-virtual-sink sink_name=v1
pacmd set-default-sink v1

# set the monitor of v1 sink to be the default source
pacmd set-default-source v1.monitor

cd /usr/src/app

# install python requirements
echo "python requirements"
pip install -r requirements.txt -i https://pypi.douban.com/simple/

# start python
echo "python3 run.py"
python3 run.py
