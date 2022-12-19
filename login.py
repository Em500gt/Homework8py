import users

def user_login():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    user = users.seach_users(login, password)
    if user != None:
        print(f'Привет {user[0]}')
    
    return user
    