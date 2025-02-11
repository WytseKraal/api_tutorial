from abc import ABC, abstractmethod

class StudentDAO(ABC):
    @abstractmethod
    def add(self, student: dict):
        "Add student to database"
        pass

    @abstractmethod
    def delete(self, student_id):
        "Delete student by ID"
        pass

    def get(self, student_id):
        "Get student by ID"
        pass
