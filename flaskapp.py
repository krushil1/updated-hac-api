from tokenize import triple_quoted
from flask import Flask, request
from flask_cors import CORS
from index import (getInfo, getCurrentClasses, getPast, getStudentSchedule)
from fakeData import *

import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

import random, string

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

# @app.route("/students/pastassignments", methods=["GET"])
# def pastAssignments():
#     username = request.args.get("username")
#     password = request.args.get("password")
#     quarter = request.args.get("quarter")

#     if(username.lower() == "john" and password.lower() == "doe"):
#         if(quarter == "1"):
#             return firstQuarter
#         elif (quarter == "2"):
#             return secondQuarter
#         elif (quarter == "3"):
#             return thirdQuarter
#         elif (quarter == "4"):
#             return fourthQuarter

#     courses = []

#     classes = getPast(username, password, quarter)

#     for course in classes:
#         courses.append(
#             {
#                 "name": course.name,
#                 "grade": course.grade,
#                 "Last Updated": course.updateDate,
#                 "assignments": course.assignments
#             }
#         )

#     return {"currentClasses": courses}

# @app.route("/students/info", methods=["GET"])
# def sendInfo():
#     username = request.args.get("username")
#     password = request.args.get("password")

#     if(username.lower() == "john" and password.lower() == "doe"):
#         return studentData

#     return getInfo(username, password)


@app.route("/students/schedule", methods=["GET"])
def sendSchedule():
    username = request.args.get("username")
    password = request.args.get("password")
  
    encryptedUsername = request.args.get("username")
    encryptedPassword = request.args.get("password")
  
    key = 'AAAAAAAAAAAAAAAA' #Must Be 16 char for AES128
    def decrypt(enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc),16)
    # encryptedUsername = username
    username = decrypt(encryptedUsername)
    # encryptedPassword = password
    password = decrypt(encryptedPassword)
    
    username = username.decode("utf-8", "ignore")
    password = password.decode("utf-8", "ignore") 

    if(username.lower() == "john" and password.lower() == "doe"):
        return schedule

    return {"schedule": getStudentSchedule(username, password)}


# @app.route("/students/currentclasses", methods=["GET"])
# def sendCurrentClasses():

#     username = request.args.get("username")
#     password = request.args.get("password")
  
#     encryptedUsername = request.args.get("username")
#     encryptedPassword = request.args.get("password")
  
#     key = 'AAAAAAAAAAAAAAAA' #Must Be 16 char for AES128
#     def decrypt(enc):
#         enc = base64.b64decode(enc)
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#         return unpad(cipher.decrypt(enc),16)
#     # encryptedUsername = username
#     username = decrypt(encryptedUsername)
#     # encryptedPassword = password
#     password = decrypt(encryptedPassword)
    
#     username = username.decode("utf-8", "ignore")
#     password = password.decode("utf-8", "ignore")  

#     if(username.lower() == "john" and password.lower() == "doe"):
#         return currentClasses

#     courses = []

#     classes = getCurrentClasses(username, password)

#     for course in classes:
#         courses.append(
#             {
#                 "name": course.name,
#                 "grade": course.grade,
#                 "Last Updated": course.updateDate,
#                 "assignments": course.assignments
#             }
#         )

#     return {"currentClasses": courses}

if __name__ == "main__":
    app.run()
