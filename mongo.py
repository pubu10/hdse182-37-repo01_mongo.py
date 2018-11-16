
#from passlib.hash import pbkdf2_sha256
	
import hashlib
from pymongo import MongoClient


username = input("Enter Your Username")
password = input("Enter Your password")
sign = input("press 2 for create account")

if sign !=2:
#hash_object = hashlib.md5(password)
hash_object = hashlib.md5(password.encode())
password2 = hash_object.hexdigest()
print('The string to store in the db is: ' + password2)

Client = MongoClient()
db = Client["Login"]
collection = db["user"]
user ={}
user['userName'] = unam
user['userPassword'] =upas
if user['userName'] == username and user['userPassword'] == password2:
    print("welcome")
   elif sign == 2:
       user ["userName"] = username
user ["userPassword"] = password2
collection.insert(user)
else:
     print("try agin")
     else
     print("???????")


#print(user)
#hash = pbkdf2_sha256.hash("toomanysecrets")
#print(hash);
#Client = Mongoclient()
#db = Client["Library"]
#collection = db["books"]
#book={}
#book["title"]
#book["name"]
#collection.insert(book)
#print(book)
#'$pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'

#>>> # verifying the password
#>>> pbkdf2_sha256.verify("toomanysecrets", hash)
#rue
#>> pbkdf2_sha256.verify("joshua", hash)
#False
