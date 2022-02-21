import json

def register(username,email,password):
    user_obj = {
        'username':username,
        'email':email,
        'password':password
    }

    result = json.dumps(user_obj)












