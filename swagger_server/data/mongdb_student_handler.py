import os
from pymongo import MongoClient
import random

from swagger_server.data.student_DAO import StudentDAO

class MongoDBStudentHandler(StudentDAO):
    def __init__(self, uri=None, db_name="students_db", collection_name="students"):
        if not uri:
            uri = os.environ.get('MONGO_URI', "mongodb://localhost:2701")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def _generate_student_id(self):
        # A simple example—ideally, use a more robust method
        return random.randint(1, 1000000)

    def add(self, student: dict):
        # Generate an ID if none is provided:
        student_id = student.get("student_id") or self._generate_student_id()
        student["student_id"] = student_id  # ensure the student dict contains the id
        record = self.collection.find_one({"student_id": student_id})
        if record:
            return {"error": "Student already exists"}, 409
        try:
            self.collection.insert_one(student)
            return {
                "student_id": student_id,
                "first_name": student["first_name"],
                "last_name": student["last_name"],
                "grade_records": student.get("grade_records", [])
            }, 200
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

        # record["_id"] = str(record["_id"])
        return {"student_id": student_id, "first_name": record["first_name"], "last_name": record["last_name"], "grade_records": record.get("grade_records", [])}, 200
