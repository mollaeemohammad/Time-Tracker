from werkzeug.exceptions import HTTPException, BadRequest


class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class AlreadyExistsError(HTTPException):
    pass


class UpdatingError(HTTPException):
    pass


class DeletingError(HTTPException):
    pass


class NotExistsError(HTTPException):
    pass


class EmailAlreadyExistsError(HTTPException):
    pass


class UnauthorizedError(HTTPException):
    pass


class InvalidArgumentsError(HTTPException):
    pass


class DatabaseConnectionError(HTTPException):
    pass


class NotMatchPasswordWithConfirmError(HTTPException):
    pass


class AlreadyIsLoggedInError(HTTPException):
    pass


class UnableToAddToDataBase(HTTPException):
    pass


class NotAllowedToDoThis(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 503
    },
    "DatabaseConnectionError": {
        "message": "Connection with database could not be established",
        "status": 502
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "AlreadyExistsError": {
        "message": "Object with given name already exists",
        "status": 400
    },
    "UpdatingError": {
        "message": "Invalid field(s) or parameters provided",
        "status": 400
    },
    "DeletingError": {
        "message": "Deleting movie added by other is forbidden",
        "status": 403
    },
    "NotExistsError": {
        "message": "Object with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "InvalidArgumentsError": {
        "message": "Invalid type or format of arguments",
        "status": 400
    },
    "NotMatchPasswordWithConfirmError": {
        "message": "Entered password is not matched with confirm password",
        "status": 400
    },
    "AlreadyIsLoggedInError": {
        "message": "When you are logged in, you cannot do it again.",
        "status": 400
    },
    "UnableToAddToDataBase": {
        "message": "Unable to add sent information to data base.",
        "status": 400
    },
    "NotAllowedToDoThis": {
        "message": "Not allowed to do this work.",
        "status": 400
    }
}
