from flask import Flask
from flask import jsonify
from flask import request
import sql

# This file I took from my HW2 submission, and i modified it to work with cryptocurrency
app = Flask(__name__)
app.config["DEBUG"] = True

# Initalize Database
sql.initializeDatabase()

# Create hardcoded user
user = {
    'username': 'admin',
    'password': 'password'
}


# Create reusable authentication method
def authenticate(username, password):
    if user['username'] == username and user['password'] == password:
        return True
    else:
        return False


@app.route('/api/auth', methods=['POST'])
def check_authentication():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    else:
        return 'Authentication successful!'


# All CRUD endpoints for facility
@app.route('/api/facility', methods=['GET'])
def get_facility():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'
    results = sql.getFacility(id)
    return jsonify(results)


@app.route('/api/facility', methods=['POST'])
def create_facility():
    print(request.values)
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    name = request.values.get('name', False)

    # We want to make sure the request supplied all needed variables
    if name is None:
        return 'No name variable in the parameters!'

    sql.createFacility(name)
    return 'Facility successfully added!'


@app.route('/api/facility', methods=['PUT'])
def update_facility():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    id = request.args['id']
    name = request.args['name']

    # We want to make sure the request supplied all needed variables
    if name is None:
        return 'No name variable in the parameters!'

    sql.updateFacility(id, name)
    return 'Facility successfully updated!'


@app.route('/api/facility', methods=['DELETE'])
def delete_facility():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'
    sql.deleteFacility(id)
    return 'Facility successfully deleted!'


# All CRUD endpoints for classroom
@app.route('/api/classroom', methods=['GET'])
def get_classroom():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'
    results = sql.getClassroom(id)
    return jsonify(results)


@app.route('/api/classroom', methods=['POST'])
def create_classroom():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    capacity = request.values.get('capacity', False)
    name = request.values.get('name', False)
    facility = request.values.get('facility', False)

    # We want to make sure the request supplied all needed variables
    if capacity is None:
        return 'No capacity variable in the parameters!'
    if name is None:
        return 'No name variable in the parameters!'
    if facility is None:
        return 'No facility variable in the parameters!'

    sql.createClassroom(capacity, name, facility)
    return 'Classroom successfully added!'


@app.route('/api/classroom', methods=['PUT'])
def update_classroom():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    id = request.args['id']
    capacity = request.args['capacity']
    name = request.args['name']
    facility = request.args['facility']

    # We want to make sure the request supplied all needed variables
    if id is None:
        return 'No id variable in the parameters!'
    if capacity is None:
        return 'No capacity variable in the parameters!'
    if name is None:
        return 'No name variable in the parameters!'
    if facility is None:
        return 'No facility variable in the parameters!'

    sql.updateClassroom(id, capacity, name, facility)
    return 'Classroom successfully updated!'


@app.route('/api/classroom', methods=['DELETE'])
def delete_classroom():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'

    sql.deleteClassroom(id)
    return 'Classroom successfully deleted!'


# All CRUD endpoints for teacher
@app.route('/api/teacher', methods=['GET'])
def get_teacher():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'

    results = sql.getTeacher(id)
    return jsonify(results)


@app.route('/api/teacher', methods=['POST'])
def create_teacher():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    firstname = request.values.get('firstname', False)
    lastname = request.values.get('lastname', False)
    room = request.values.get('room', False)

    # We want to make sure the request supplied all needed variables
    if firstname is None:
        return 'No firstname variable in the parameters!'
    if lastname is None:
        return 'No lastname variable in the parameters!'
    if room is None:
        return 'No room variable in the parameters!'

    sql.createTeacher(firstname, lastname, room)
    return 'Teacher successfully added!'


@app.route('/api/teacher', methods=['PUT'])
def update_teacher():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    id = request.args['id']
    firstname = request.args['firstname']
    lastname = request.args['lastname']
    room = request.args['room']

    # We want to make sure the request supplied all needed variables
    if id is None:
        return 'No id variable in the parameters!'
    if firstname is None:
        return 'No firstname variable in the parameters!'
    if lastname is None:
        return 'No lastname variable in the parameters!'
    if room is None:
        return 'No room variable in the parameters!'

    sql.updateTeacher(id, firstname, lastname, room)
    return 'Teacher successfully updated!'


@app.route('/api/teacher', methods=['DELETE'])
def delete_teacher():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'

    sql.deleteTeacher(id)
    return 'Teacher successfully deleted!'


# All CRUD endpoints for child
@app.route('/api/child', methods=['GET'])
def get_child():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'

    results = sql.getChild(id)
    return jsonify(results)


@app.route('/api/child', methods=['POST'])
def create_child():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    firstname = request.values.get('firstname', False)
    lastname = request.values.get('lastname', False)
    age = request.values.get('age', False)
    room = request.values.get('room', False)

    # We want to make sure the request supplied all needed variables
    if firstname is None:
        return 'No firstname variable in the parameters!'
    if lastname is None:
        return 'No lastname variable in the parameters!'
    if age is None:
        return 'No age variable in the parameters!'
    if room is None:
        return 'No room variable in the parameters!'

    roomCapacity = sql.getCapacityForClassroom(room)[0][0]
    teacherCapacity = sql.getTeacherCountForClassroom(room)[0][0] * 10
    currentStudents = sql.getChildCountForClassroom(room)[0][0]

    if (currentStudents + 1 > roomCapacity):
        return 'This classroom doesnt have enough capacity to take the student.'
    if (currentStudents + 1 > teacherCapacity):
        return 'This classroom doesnt have enough teachers to take the student.'

    sql.createChild(firstname, lastname, age, room)
    return 'Child successfully added!'


@app.route('/api/child', methods=['PUT'])
def update_child():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    id = request.args['id']
    firstname = request.args['firstname']
    lastname = request.args['lastname']
    age = request.args['age']
    room = request.args['room']

    # We want to make sure the request supplied all needed variables
    if id is None:
        return 'No id variable in the parameters!'
    if firstname is None:
        return 'No firstname variable in the parameters!'
    if lastname is None:
        return 'No lastname variable in the parameters!'
    if age is None:
        return 'No age variable in the parameters!'
    if room is None:
        return 'No room variable in the parameters!'

    roomCapacity = sql.getCapacityForClassroom(room)[0][0]
    teacherCapacity = sql.getTeacherCountForClassroom(room)[0][0] * 10
    currentStudents = sql.getChildCountForClassroom(room)[0][0]

    if (currentStudents + 1 > roomCapacity):
        return 'This classroom doesnt have enough capacity to take the student.'
    if (currentStudents + 1 > teacherCapacity):
        return 'This classroom doesnt have enough teachers to take the student.'

    sql.updateChild(id, firstname, lastname, age, room)
    return 'Child successfully updated!'


@app.route('/api/child', methods=['DELETE'])
def delete_child():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'

    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error, no id was provided!'

    sql.deleteChild(id)
    return 'Child successfully deleted!'


# Extra functions for each entity to get all of them
@app.route('/api/facility/all', methods=['GET'])
def get_all_facility():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    results = sql.getAllFacilities()
    return jsonify(results)


@app.route('/api/classroom/all', methods=['GET'])
def get_all_classroom():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    results = sql.getAllClassrooms()
    return jsonify(results)


@app.route('/api/teacher/all', methods=['GET'])
def get_all_teacher():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    results = sql.getAllTeachers()
    return jsonify(results)


@app.route('/api/child/all', methods=['GET'])
def get_all_child():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    results = sql.getAllChildren()
    return jsonify(results)


# This is just a reset DB function so I know its fresh for grading
@app.route('/api/reset', methods=['PUT'])
def reset():
    if not authenticate(request.values.get("username", False), request.values.get("password", False)):
        return 'User could not be authenticated!'
    sql.resetDatabase()
    sql.initializeDatabase()
    return 'Database successfully reset!'

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# Run app to listen for request
app.run()