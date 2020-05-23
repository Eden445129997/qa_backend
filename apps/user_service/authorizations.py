import jwt
from datetime import datetime,timedelta
from django.conf import settings


def generate_jwt(user):
    expire_time = datetime.now() + timedelta(days=7)
    return jwt.encode({"userid":user.pk,"exp":expire_time},key=settings.SECRET_KEY).decode('utf-8')

# def JWTAuthentication()