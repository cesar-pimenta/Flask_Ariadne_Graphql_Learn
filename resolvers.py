import uuid

DB = {
    "students": [],
    "classes": [],
    "users": [],
}


class User:
    def __init__(self, name, idade):
        self.name = name
        self.age = age 
        self.id = uuid.uuid4().__str__()

    def response(self):
        temp = {
            "name": self.name,
            "age": self.age,
            "id": self.id
        }
        return temp

class Student:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4().__str__()

    def response(self):
        temp = {
            "name": self.name,
            "id": self.id
        }
        return temp


class Class:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4().__str__()
        self.students = []

    def response(self):
        return {
            "name": self.name,
            "id": self.id,
            "students": self.students
        }

def resolve_student_create(_, info, name):
    student = Student(name).response()
    DB['students'].append(student)
    return student


def resolve_student_by_id(_, info, _id):
    for student in DB['students']:
        if student['id'] == _id:
            return student


def resolve_students(_, info):
    return DB['students']


def resolve_user_create(_, info, name, age):
    user= User(name, age).response()
    DB['users'].append(user)
    return user

def resolve_users(_, info):
    return DB['users']


def resolve_class_create(_, info, name):
    class_object = Class(name).response()
    DB['classes'].append(class_object)
    return class_object


def resolve_class_by_id(_, info, _id):
    for class_object in DB['classes']:
        if class_object['id'] == _id:
            return class_object


def resolve_classes(_, info):
    return DB['classes']


def resolve_add_student_to_class(_, info, class_id, student_id):
    print(class_id + " " + student_id)
    for index, class_object in enumerate(DB['classes']):
        if class_object['id'] == class_id:
            for student in DB['students']:
                if student['id'] == student_id:
                    DB['classes'][index]['students'].append(student)
                    return DB['classes'][index]


def resolve_students_in_classes(class_object, info):
    return class_object['students']