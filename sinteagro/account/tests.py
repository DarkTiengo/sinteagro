
from .models import User

def is_user(email):
    try:
        User.objects.get(email=email)
        return True
    except:
        return False