from .models import User
from app import db


def getUserFromId(UserID):
    return (
        db.session.query(User)
        .filter(User.UserID == UserID)
        .one_or_none()
    )


def getUserFromEmail(Email):
    return (
        db.session.query(User)
        .filter(User.Email == Email)
        .one_or_none()
    )


def createUser(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return True


def updateUserPassword(UserID, Password):
    user = db.session.query(User).get(UserID)
    user.Password = Password
    db.session.commit()
    return user
