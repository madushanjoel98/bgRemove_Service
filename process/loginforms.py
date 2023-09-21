# User database (you can replace this with a database or file storage for a real application)
import hashlib
import datetime
class User:
    def __init__(self):
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%Y%d%m")
        pasw="bjUI,a/DMX62,Md"+formatted_date
        print(formatted_date)
        self.user_database = user_database = {"madusPy@19985$": pasw}

    def is_valid_credentials(self,username, password):
        if username in self.user_database and self.user_database[username] == password:
            return True
        else:
            return False
        

Us=User()
nm=Us.is_valid_credentials("madusPy@19985$","bjUI,a/DMX62,Md20231909")
print(nm)