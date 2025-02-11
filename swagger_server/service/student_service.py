from swagger_server.data.tinyDB_student_handler import TinyDBStudentHandler
from swagger_server.data.mongdb_student_handler import MongoDBStudentHandler
# studentDAO = TinyDBStudentHandler()
studentDAO = MongoDBStudentHandler()

def add(body):
    return studentDAO.add(body)

def delete(student_id):
    return studentDAO.delete(student_id)

def get(student_id):
    return studentDAO.get(student_id)