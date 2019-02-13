ECHO OFF
cd %1\backend\heartbeatserver
call conda create -n heartbeater
call conda activate heartbeater
call pip install -r requirements.txt
call pip install --user --upgrade twilio
call python main.py
PAUSE