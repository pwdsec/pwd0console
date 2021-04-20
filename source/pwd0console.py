import auth


php = input("[PHPSESSID]: ")
cookies = auth.LoginHandler.Login(php)

print(auth.LoginHandler.Get_User_data(php, cookies))