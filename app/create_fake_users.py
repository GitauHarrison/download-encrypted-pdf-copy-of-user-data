from faker import Faker
from app import db
from random import randint
from app.models import User


def fake_users(n):
    fake = Faker()
    for i in range(n):
        user = User(
            name=fake.name(),
            age=randint(18, 65),
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email())
        db.session.add(user)
    db.session.commit()
