from flask import Response, request, jsonify, render_template
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, decode_token
import json
import datetime
from errors import auth_error, system_error

from utils.helper import db_model_to_dict
from .auth import User


class UserStatus(Resource):
    def post(self):
        try:
            user = User()
            result = user.status(request)
            return result, 201
        except auth_error.UserNotSigned:
            raise auth_error.UserNotSigned
        except auth_error.ExpiredTokenError:
            raise auth_error.ExpiredTokenError
        except auth_error.BadTokenError:
            raise auth_error.BadTokenError
        except Exception:
            raise system_error.InternalServerError


class Signup(Resource):
    def post(self):
        user = User()
        result = user.signup(request.json)
        return result, 201


# class Signout(Resource):
#     def post(self):
#         user = User()
#         result = user.signout(request.json)
#         return result, 201


class Signin(Resource):
    def post(self):
        try:
            user = User()
            result = user.login(request.json)
            return result, 201
        except (auth_error.PasswordNotTrue):
            raise auth_error.PasswordNotTrue
        except auth_error.UserNameOrEmailCouldntFound:
            raise auth_error.UserNameOrEmailCouldntFound
        except Exception as e:
            print(e)
            raise system_error.InternalServerError
            # raise system_error.InternalServerError


class ForgotPassword(Resource):
    def post(self):
        try:
            user = User()
            url = request.host_url + 'reset/'
            user.forget_password(request.json, url)
            return '', 201
        except auth_error.EmailDoesnotExists:
            raise auth_error.EmailDoesnotExists


class ResetPassword(Resource):
    def post(self):
        try:
            user = User()
            result = user.reset_password(request.json)
            return result, 201
        except Exception:
            raise system_error.InternalServerError
