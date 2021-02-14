
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from errors.auth_error import errors as e1
from errors.system_error import errors as e2

from config import Config


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config.from_object(Config)

mail = Mail(app)


e1.update(e2)

api = Api(app, errors=e1)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)


from api.routes import initialize_routes
initialize_routes(api)
