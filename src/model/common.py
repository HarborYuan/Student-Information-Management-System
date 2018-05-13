import sqlite3
import os
import hashlib
dirname, filename = os.path.split(os.path.abspath(__file__))


def getStudentList():
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    cursor = c.execute("SELECT ID  from STUIDC")
    StudentList = []
    for row in cursor:
        StudentList.append(str(row[0]))
    conn.close()
    return StudentList


def judgeStudent(stuid, stuidc):
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    try:
        cursor = c.execute("SELECT IDC from STUIDC WHERE ID==" + stuid)
    except sqlite3.OperationalError:
        conn.close()
        return "no such student"
    for i in cursor:
        if (i[0] == hashlib.sha3_512(stuidc.encode()).hexdigest()):
            conn.close()
            return "pass"
        conn.close()
        return "error"
    conn.close()
    return "no such student"


def getMajorList():
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    cursor = c.execute("SELECT id,name  from MAJORS")
    MajorList = []
    for row in cursor:
        MajorList.append((row[0], row[1]))
    conn.close()
    return MajorList


def userExist(id):
    conn = sqlite3.connect(dirname + '/../data/hongyi.db')
    c = conn.cursor()
    try:
        cursor = c.execute("SELECT id from USERS WHERE id==" + id)
    except sqlite3.OperationalError:
        conn.close()
        return False
    for i in cursor:
        if (str(i[0]) == id):
            conn.close()
            return True
    conn.close()
    return False
