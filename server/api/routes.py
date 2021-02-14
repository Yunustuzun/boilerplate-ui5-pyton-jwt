from .resources import Signup, Signin, ForgotPassword, ResetPassword, UserStatus


def initialize_routes(api):
    api.add_resource(UserStatus, '/api/auth/status')
    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(Signin, '/api/auth/signin')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
