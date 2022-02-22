import json

def register(username,email,password):
    user_obj = {
        'username':username,
        'email':email,
        'password':password
    }

    user_json = json.dumps(user_obj)#tuka mi go dava kato stringov dict
    with open('users.txt','r+') as file:
        for user_line in file:#Validating if the user is in the user  if not add else not
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username:
                return False

        file.write(user_json + '\n')
        return True

def login(username,password):

    with open('users.txt','r+') as file:
        for user_line in file:
            existing_user = json.loads(user_line.strip())
            if existing_user['username'] == username and existing_user['password'] == password:
                return True
        return False






