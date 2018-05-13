import sqlite3
import os
import hashlib
dirname, filename = os.path.split(os.path.abspath(__file__))


def insertUser(data):
    id = data['username']
    pwd = hashlib.sha3_512(data['password1'].encode()).hexdigest()
    major = str(data['major'])
    email = data['email']
    phone = data['phone']
    isGirl = str(data['isGirl'])
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO USERS (id,pass,major,email,phone,isGirl) \
        VALUES (" + id + ",'" + pwd + "' , " + major + ", '" + email + "' ,'" +
                  phone + "','" + isGirl + "' )")
    except:
        conn.close()
        return False
    conn.commit()
    conn.close()
    return True


def userlogin(username, pwd):
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    try:
        cursor = c.execute("SELECT id,pass  from USERS where id=="+username)
    except:
        conn.close()
        return False
    for i in cursor:
        if (str(i[0]) == username
                and i[1] == hashlib.sha3_512(pwd.encode()).hexdigest()):
            conn.close()
            return True
    conn.close()
    return False
