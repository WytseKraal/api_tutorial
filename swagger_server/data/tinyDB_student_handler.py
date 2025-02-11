from tinydb import TinyDB, Query
from swagger_server.data.student_DAO import StudentDAO

class TinyDBStudentHandler(StudentDAO):
    def __init__(self, db_path: str = 'students.json'):
        self.db = TinyDB(db_path)
        self.table = self.db.table('students')

    def add(self, student: dict):
        student_id = student.get('student_id')
        _, status_code = self.get(student_id)

        if status_code == 200:
            return {"message": "student already exists"}, 409

        self.table.insert(student)
        return {"message": f"student sucessfully added, with id {student_id}"}, 201

    def delete(self, student_id):
        Student = Query()

        if not self.get(student_id):
            return {"error": f"student not found"}, 404
        self.table.remove(Student.student_id == student_id)
        return {"message": f"Student {student_id} deleted"}, 200

    def get(self, student_id):
        Student = Query()

        result = self.table.search(Student.student_id ==student_id)

        if result:
            return result, 200
        return {"message": "student not found"}, 404
