ECHO OFF
cd %cd%\install
curl https://repo.anaconda.com/archive/Anaconda3-2018.12-Windows-x86_64.exe -O anaconda_installer.exe
curl https://nodejs.org/dist/v10.15.1/node-v10.15.1-x64.msi -O node_installer.exe
curl https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe -O python_installer.exe
curl https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.15.0.msi -O mysql_installer.exe
for /r %%i in (*) do call %%i
PAUSE