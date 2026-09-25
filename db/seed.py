import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.auth import hash_password
from app.database import Base, SessionLocal, engine
from app.models import User

SEED_USERS = [
    {"email": "john.doe@example.com", "password": "Password123!", "first_name": "John", "last_name": "Doe"},
    {"email": "jane.smith@example.com", "password": "Password123!", "first_name": "Jane", "last_name": "Smith"},
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(User).count() > 0:
            print("Users already exist, skipping seed.")
            return

        for data in SEED_USERS:
            user = User(
                email=data["email"],
                password_hash=hash_password(data["password"]),
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            db.add(user)
        db.commit()
        print(f"Seeded {len(SEED_USERS)} users.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
