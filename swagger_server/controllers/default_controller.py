import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.service.student_service import *
from swagger_server import util


def add_student(body=None): # noqa: E501
    """Add a new student
    # noqa: E501
    Adds an item to the system # noqa: E501
    :param body: Student item to add
    :type body: dict | bytes
    :rtype: float
    """

    try:
        if not connexion.request.is_json():
            return {'error': "Invalid Request"}, 400

        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        response, status_code = add(body)
        return {"message": response}, status_code
    except Exception as e:
        return 500, f'error {e}'



def delete_student(student_id):  # noqa: E501
    """deletes a student

    delete a single student  # noqa: E501

    :param student_id: the uid
    :type student_id: float

    :rtype: object
    """

    try:
        response, status_code = delete(student_id)
        return {"message": response}, status_code
    except Exception as e:
        return 500, f'error {e}'


def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student # noqa: E501

    :param student_id: the uid
    :type student_id: 

    :rtype: Student
    """

    try:
        student, status_code = get(student_id)

        if status_code == 404:
            return {"error": "Student not found"}, status_code

        return student, 200
    except Exception as e:
        return 500, f'error {e}'
