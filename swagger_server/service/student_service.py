from swagger_server.data.tinyDB_student_handler import TinyDBStudentHandler

studentDAO = TinyDBStudentHandler()
def add(body):
    return studentDAO.add(body)

def delete(student_id):
    return studentDAO.delete(student_id)

def get(student_id):
    return studentDAO.get(student_id)