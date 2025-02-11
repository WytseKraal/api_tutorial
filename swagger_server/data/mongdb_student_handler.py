import os
from pymongo import MongoClient
from swagger_server.data.student_DAO import StudentDAO

class MongoDBStudentHandler(StudentDAO):
    def __init__(self, uri=None, db_name="students_db", collection_name="students"):
        if not uri:
            uri = os.environ.get('MONGO_URI', "mongodb://localhost:27017")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add(self, student:dict):
        student_id = student.get("student_id")
        record = self.collection.find_one({"student_id": student_id})
        if record:
            return {"error": "Student already exists"}, 409
        try:
            self.collection.insert_one(student)
            return student, 200
        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, student_id):
        result = self.collection.delete_one({"student_id": student_id})
        if result.deleted_count == 0:
            return {"error": "student not found"}, 404
        return {"message": f"student {student_id} deleted"}, 200

    def get(self, student_id):
        record = self.collection.find_one({"student_id": student_id})
        if not record:
            return {"message": "student not found"}, 404

        record["_id"] = str(record["_id"])
        return record, 200
