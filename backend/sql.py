import mysql.connector
import creds

credidentials = creds.creds()

def create_connection(host, username, password, database):
    return mysql.connector.connect(
        host = host,
        user = username,
        password = password,
        database = database
    )

def initializeDatabase():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS facility (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(128))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS classroom (id INT PRIMARY KEY AUTO_INCREMENT, capacity INT, name VARCHAR(128), facility INT, FOREIGN KEY(facility) REFERENCES facility(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS teacher (id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(128), lastname VARCHAR(128), room INT, FOREIGN KEY(room) REFERENCES classroom(id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS child (id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(128), lastname VARCHAR(128), age INT, room INT, FOREIGN KEY(room) REFERENCES classroom(id))")

def resetDatabase():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE child")
    mycursor.execute("DROP TABLE teacher")
    mycursor.execute("DROP TABLE classroom")
    mycursor.execute("DROP TABLE facility")


# Facility CRUD
def getFacility(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from facility WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def createFacility(name):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'INSERT INTO facility(name) VALUES (%s)'
    values = [name]
    mycursor.execute(sql, values)
    mydb.commit()

def updateFacility(id, name):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'UPDATE facility SET name = %s WHERE id = %s'
    values = [name, id]
    mycursor.execute(sql, values)
    mydb.commit()

def deleteFacility(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'DELETE from facility WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    mydb.commit()

def getAllFacilities():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from facility'
    mycursor.execute(sql)
    return mycursor.fetchall()

# Classroom CRUD
def getClassroom(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from classroom WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def createClassroom(capacity, name, facility):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'INSERT INTO classroom(capacity, name, facility) VALUES (%s, %s, %s)'
    values = (capacity, name, facility)
    mycursor.execute(sql, values)
    mydb.commit()

def updateClassroom(id, capacity, name, facility):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'UPDATE classroom SET capacity = %s, name = %s, facility = %s WHERE id = %s'
    values = (capacity, name, facility, id)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteClassroom(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'DELETE from classroom WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    mydb.commit()

def getAllClassrooms():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from classroom'
    mycursor.execute(sql)
    return mycursor.fetchall()

# Teacher CRUD
def getTeacher(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from teacher WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def createTeacher(firstname, lastname, room):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'INSERT INTO teacher(firstname, lastname, room) VALUES (%s, %s, %s)'
    values = (firstname, lastname, room)
    mycursor.execute(sql, values)
    mydb.commit()

def updateTeacher(id, firstname, lastname, room):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'UPDATE teacher SET firstname = %s, lastname = %s, room = %s WHERE id = %s'
    values = (firstname, lastname, room, id)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteTeacher(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'DELETE from teacher WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    mydb.commit()

def getAllTeachers():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from teacher'
    mycursor.execute(sql)
    return mycursor.fetchall()

# Child CRUD
def getChild(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from child WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def createChild(firstname, lastname, age, room):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'INSERT INTO child(firstname, lastname, age, room) VALUES (%s, %s, %s, %s)'
    values = (firstname, lastname, age, room)
    mycursor.execute(sql, values)
    mydb.commit()

def updateChild(id, firstname, lastname, age, room):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'UPDATE child SET firstname = %s, lastname = %s, age = %s, room = %s WHERE id = %s'
    values = (firstname, lastname, age, room, id)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteChild(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'DELETE from child WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    mydb.commit()

def getAllChildren():
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT * from child'
    mycursor.execute(sql)
    return mycursor.fetchall()

# Helper methods we can use for validations
def getCapacityForClassroom(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT capacity from classroom WHERE id = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def getTeacherCountForClassroom(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT COUNT(*) from teacher WHERE room = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()

def getChildCountForClassroom(id):
    mydb = create_connection(credidentials.host, credidentials.username, credidentials.password, credidentials.database)
    mycursor = mydb.cursor()

    sql = 'SELECT COUNT(*) from child WHERE room = \'%s\'' % (id)
    mycursor.execute(sql)
    return mycursor.fetchall()