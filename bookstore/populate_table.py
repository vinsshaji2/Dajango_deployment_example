import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "bookstore.settings")

import django
django.setup()

import random
from books.models import UserLogin, FormRegister
from faker import Faker
import string

fakegen = Faker()

usernames = ['vins12@gmail.com', 'shaji12@yahoo.com', 'jins12@hotmail.com', 'prince12@outlook.com', 'anitha12@gmail.com']
char = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(char) for _ in range(8))


def add_user():
    for _ in range(5):
        t = UserLogin.objects.get_or_create(email=random.choice(usernames), password=password)[0]
        t.save()
        # return t

if __name__ == '__main__':
    print("Populating")
    add_user()
    print("Populating is completed")
