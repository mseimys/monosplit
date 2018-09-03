from django.contrib.auth.models import User
from django.db import IntegrityError


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
ADMIN_EMAIL = 'admin@monosplit.com'

def get_admin():
    try:
        return User.objects.create_user(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
    except IntegrityError:
        return User.objects.get(username=ADMIN_USERNAME, email=ADMIN_EMAIL)
