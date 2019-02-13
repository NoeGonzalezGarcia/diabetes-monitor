def get_creds():
    with(open('credentials.txt', 'w')) as creds:
        username = ''
        password = ''
        while username == '':
            username = input("What is the db username? (Can't be empty)\n")
        while password == '':
            password = input("What is the db password? (Can't be empty\n")
        creds.write(username + "\n" + password)


get_creds()
