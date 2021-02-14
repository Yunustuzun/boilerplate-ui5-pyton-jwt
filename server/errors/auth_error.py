from werkzeug.exceptions import HTTPException
# ~/movie-bag/resources/errors.py


class EmailAlreadyExistsError(HTTPException):
    pass


class EmailDoesnotExists(HTTPException):
    pass


class UserNameAlreadyExist(HTTPException):
    pass


class UserNameOrEmailCouldntFound(HTTPException):
    pass


class PasswordNotTrue(HTTPException):
    pass


class BadTokenError(HTTPException):
    pass


class ExpiredTokenError(HTTPException):
    pass


class UserNotSigned(HTTPException):
    pass


# 403 popup error
errors = {
    "EmailAlreadyExistsError": {
        "message": "Email adresi daha önceden kaydedilmiştir.",
        "status": 403
    },
    "EmailDoesnotExists": {
        "message": "Giriş yaptığınız email adresi bulunamadı.",
        "status": 403
    },
    "UserNameAlreadyExist": {
        "message": "Kullanıcı adı sistemde tanımlı. Farklı bir kullanıcı adı tanımlayınız.",
        "status": 403
    },
    "UserNameOrEmailCouldntFound": {
        "message": "Kullanıcı Adı sistemde bulunamadı.",
        "status": 403
    },
    "PasswordNotTrue": {
        "message": "Şifrenizi kontrol ediniz.",
        "status": 403
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 401
    },
    "ExpiredTokenError": {
        "message": "Expired token",
        "status": 401
    },
    "UserNotSigned": {
        "message": "User not signed",
        "status": 401
    },
}
