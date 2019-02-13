# Diabetes Monitor
Software Architecture Skeletal Diagram

TO RUN THE PROGRAM:

1. Install the following software packages:
    * Note the following things
    * Anaconda needs the SYSTEM PATH included
    * Anaconda needs the file location to be set a different folder
    * TODO: Navigate to batch_files folder, then run install.bat
    
2. Create a new database user
    * open MySQL Workbench
    * Click on the Local Instance
    * Replace the yourusername and yourpassword, and run the command "ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';" by pressing the lightning button..
    * Close MySQL Workbench
    
3. Set database credentials
    * Navigate to batch_files, and run set_up_creds.bat
    * Enter the username from step 2 and press enter
    * Enter the password from step 2 and press enter
    
4. Start all of the services.
    * Navigate to batch_files, and run run_program.bat
        
