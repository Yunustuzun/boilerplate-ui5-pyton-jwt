from werkzeug.exceptions import HTTPException
# ~/movie-bag/resources/errors.py


class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 500
    }
}
