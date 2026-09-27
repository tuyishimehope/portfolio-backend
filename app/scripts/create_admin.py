import argparse, getpass, sys
from sqlalchemy import select

from app.db.engine import SessionLocal
from app.db.models.user import User
from app.utils.security import hash_password


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True)
    email = parser.parse_args().email.strip().lower()

    password = getpass.getpass("Password: ")
    if len(password) < 12:
        sys.exit("Password must be 12+ characters")
    if password != getpass.getpass("Confirm: "):
        sys.exit("Passwords don't match")

    with SessionLocal() as db:
        exists = db.scalar(select(User).where(User.email == email))
        if exists:
            sys.exit(f"{email} already exists")
        db.add(User(email=email,
                    password_hash=hash_password(password)))
        db.commit()

    print(f"✅ Admin {email} created")

if __name__ == "__main__":
    main()