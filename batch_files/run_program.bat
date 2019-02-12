ECHO OFF
set home=%CD%\..
cd %home%\batch_files
start backend.bat %home%
start frontend.bat %home%
start mysql.bat
start heartbeat.bat %home%