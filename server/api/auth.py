from flask import render_template
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, decode_token
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.decorators import singleton
from database import operation
from errors import auth_error, system_error
from services.mail_service import send_email
from utils.helper import db_model_to_dict


@singleton
class User():
    def status(self, request):

        auth_header = request.headers.get('Authorization')

        print("Request Token Status : " + auth_header)

        try:
            auth_token = auth_header.split(' ')[1]
        except IndexError:
            raise auth_error.UserNotSigned

        if not auth_header:
            raise auth_error.UserNotSigned

        try:
            user_id = decode_token(auth_token)['identity']

        except ExpiredSignatureError:
            raise auth_error.ExpiredTokenError

        except (DecodeError, InvalidTokenError):
            raise auth_error.BadTokenError

        except Exception as e:
            print(e)
            raise system_error.InternalServerError

        user = operation.getUserFromId(user_id)
        if user is None:
            user = operation.getUserFromEmail(user_id)

        if user is None:
            raise auth_error.UserNotSigned

        login_token = create_access_token(str(user.UserID), 2)

        print("Generated Token Status : " + login_token)
        return {"token": login_token, 'info': db_model_to_dict(user)}

    def signup(self, request):

        auth_header = request.headers.get('Authorization')

        try:
            auth_token = auth_header.split(' ')[1]
        except IndexError:
            raise auth_error.BadTokenError

        if not auth_header:
            raise auth_error.UserNotSigned

    def login(self, data):

        user = operation.getUserFromId(data['UserID'])
        if user is None:
            user = operation.getUserFromEmail(data['UserID'])

        if user is None:
            raise auth_error.UserNameOrEmailCouldntFound

        if user.Password != data['Password']:
            raise auth_error.PasswordNotTrue

        login_token = create_access_token(str(user.UserID), 2)

        print("Generated Token Login : " + login_token)
        return {'token': login_token, 'info': db_model_to_dict(user)}

    def forget_password(self, data, url):

        try:
            email = data.get('Email')
            user = operation.getUserFromEmail(email)

            if not user:
                raise auth_error.EmailDoesnotExists

            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(str(user.UserID), expires_delta=expires)

            html = render_template('email/reset_password.html', url=url + reset_token)
            plain = render_template('email/reset_password.txt', url=url + reset_token)

            message = MIMEMultipart('alternative')
            message.attach(MIMEText(plain, 'plain'))
            message.attach(MIMEText(html, 'html'))
            send_email(email, message, 'Şifrenizi Sıfırlayın')
            return '', 200

        except auth_error.EmailDoesnotExists as e:
            raise auth_error.EmailDoesnotExists

    def reset_password(self, data):

        try:

            reset_token = data.get('reset_token')
            password = data.get('password')

            if not reset_token or not password:
                raise auth_error.SchemaValidationError

            user_id = decode_token(reset_token)['identity']
            user = operation.updateUserPassword(user_id, password)

            html = render_template('email/successful_reset.html')
            plain = render_template('email/successful_reset.txt')

            message = MIMEMultipart('alternative')
            message.attach(MIMEText(plain, 'plain'))
            message.attach(MIMEText(html, 'html'))

            send_email(user.Email, message, 'Şifrenizi Başarıyla sıfırlandı')

        # except SchemaValidationError:
        #     raise SchemaValidationError
        except ExpiredSignatureError:
            raise auth_error.ExpiredTokenError

        except (DecodeError, InvalidTokenError):
            raise auth_error.BadTokenError

        except Exception as e:
            raise auth_error.InternalServerError
