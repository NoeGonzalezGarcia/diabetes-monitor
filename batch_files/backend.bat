ECHO OFF
cd %1/backend
call conda create -n batch_test
call conda activate batch_test
call pip install -r requirements.txt
call python main.py
PAUSE