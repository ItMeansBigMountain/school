buddyboi = {
    "testing" : "123zp"
}



def login(userName:str,  password: str, data: dict):
    # Data holds (userName,password)
    if userName in data :
        if data[userName] == password:
            return "Login successful"
        else:
            return "The password was incorrect"
    else:
        return "The user name was not found"




print(login("tsting", "12zap", buddyboi))