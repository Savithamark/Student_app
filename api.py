from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename
from flask_cors import CORS
app = Flask(__name__)

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/login/', methods=['POST'])
def LoginAPI():
    if request.method == 'POST':
        data = request.get_json(True)
        # print(data)
        # UserName = data['username']
        # print(UserName)
        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                # cur.execute('SELECT * FROM users')
                cur.execute('SELECT * FROM  users WHERE username=? and password=?', (data['username'],data['password']))
                # cur.execute('SELECT * FROM users WHERE username="data['username']"')
                rst = cur.fetchone()
                print(rst)
                if not rst:
                    return jsonify({"message": "Email has not yet been registered"}), 401
                else:
                    status = rst[1]
                    msg = "Login Successfully"
                    return jsonify({"message": "logged in successfully", "data": rst[3]}), 200
                con.commit()
                msg = "Logged in Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return msg

@app.route('/registerAPI/', methods=['POST'])
def registerAPI():
    if request.method == 'POST':
        data = request.get_json(True)
        print(data)
        password = data['password']
        username = data['username']
        firstName = data['firstName']
        lastName = data['lastName']
        with sqlite3.connect('database.db') as con:
            # try:
            cur = con.cursor()
            cur.execute('SELECT * FROM  users WHERE username=?', (data['username'],))
            rst = cur.fetchone()
            if not rst:
                cur.execute('INSERT INTO users (password, username, firstName, lastName) VALUES (?, ?, ?, ?)', (password, username, firstName, lastName))
                return jsonify({"message": "Registeration in successfully"}), 200
            else:
                return jsonify({"message": "User already Registered"}), 401
            con.commit()
            # except:
            #     con.rollback()
            #     msg = "Error occured"
        con.close()
        return msg

@app.route('/registerGETAPI/', methods=['GET'])
def registerGETAPI():
    if request.method == 'GET':
        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('SELECT * FROM users')
                # con.row  = sqlite3.row
                rst = cur.fetchall()
                organisationsList = [
                    {
                        "userId":userId,
                        "password":password,
                        "username":username,
                        "firstName":firstName,
                        "lastName":lastName,
                        
                    } for userId, password, username, firstName, lastName  in rst
                ]
                
                print(rst)
                con.commit()
                msg = "Get All Rgistered Data"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return json.dumps(organisationsList)


@app.route('/Lectures/', methods=['POST'])
def LecturesPOSTAPI():
    if request.method == 'POST':
        data = request.get_json(True)
        print(data)
        first_name = data['first_name']
        last_name = data['last_name']
        gender = data['gender']
        Qualification = data['Qualification']
        Experience = data['Experience']
        About = data['About']
        DOMAIN = data['DOMAIN']
        with sqlite3.connect('database.db') as con:
            # try:
            cur = con.cursor()
            cur.execute('SELECT * FROM  Lectures WHERE first_name=?', (data['first_name'],))
            rst = cur.fetchone()
            if not rst:
                cur.execute('INSERT INTO Lectures (first_name, last_name, gender, Qualification,Experience,About,DOMAIN) VALUES (?, ?, ?, ?, ?, ?, ?)', (first_name, last_name, gender, Qualification,Experience,About,DOMAIN))
                return jsonify({"message": "lecture Registeration in successfully"}), 200
            else:
                return jsonify({"message": "lecture already Registered"}), 401
            con.commit()
        con.close()
        return msg

@app.route('/LecturesGETAPI/', methods=['GET'])
def LecturesGETAPI():
    if request.method == 'GET':
        with sqlite3.connect('database.db') as con:
            try:
                cur = con.cursor()
                cur.execute('SELECT * FROM Lectures')
                # con.row  = sqlite3.row
                rst = cur.fetchall()
                lecturerList = [
                    {
                        "Lecture_Id":Lecture_Id,
                        "first_name":first_name,
                        "last_name":last_name,
                        "gender":gender,
                        "Qualification":Qualification,
                        "Experience":Experience,
                        "About":About,
                        "DOMAIN":DOMAIN
                    } for Lecture_Id, first_name, last_name, gender, Qualification,Experience,About,DOMAIN  in rst
                ]
                
                print(rst)
                con.commit()
                msg = "Get All Rgistered Data"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return json.dumps(lecturerList)


if __name__ == '__main__':
    app.run(debug=True)


                    # if not rst:
                #     return jsonify({"message": "Email has not yet been registered"}), 401
                # else:
                #     status = rst[1]
                #     msg = "Login Successfully"
                #     return jsonify({"message": "logged in successfully", "data": rst[1]}), 200


                                # query_string = "SELECT * FROM users WHERE username = %s"
                # print(query_string)
                # cur.execute(query_string, (username,))
                                # cur.execute('SELECT * FROM users WHERE  username = %s',[username])