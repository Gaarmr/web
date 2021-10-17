from getpass import getpass
import sys
from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    user_name = input('Enter user name: ')

    if User.query.filter(User.user_name == user_name).count():
        print('This user already exists')
        sys.exit(0)

    password = getpass('Enter password: ')
    password2 = getpass('Repeat password: ')
    
    if not password == password2:
        print('Password mismatch')
        sys.exit(0)

    new_user = User(user_name=user_name, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f'User with id {new_user.id} added')