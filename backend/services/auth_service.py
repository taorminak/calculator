import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
import sqlite3
from sqlite3 import Error
import hashlib

# Secret key for JWT encoding
SECRET_KEY = "5E18C542027176768CA471B78518FE56011A09553D7522668EF30F7784324FC3"

class AuthService:
    def __init__(self, db_file='calculation.db', secret_key=SECRET_KEY):
        self.db_file = db_file
        self.secret_key = secret_key

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        conn = self.create_connection()
        if conn is None:
            return None
        
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT username, hashed_password, role FROM users WHERE username=?", (username,))
            user_record = cursor.fetchone()

            if user_record:
                _, hashed_password, _ = user_record
                if self.verify_password(password, hashed_password):
                    print(f"User authenticated")
                    return self._create_token(username)
                else:
                    print(f"Password verification failed for user")

            else:
                print(f"No user found with username: {username}")
            return None
        except Error as e:
            print(f"Database error: {e}")
            return None
        finally:
            conn.close()

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # Verify if the plain password matches the hashed password
        return hashed_password == hashlib.sha256(plain_password.encode('utf-8')).hexdigest()

    def _create_token(self, username: str) -> str:
        # Create a JWT token with an expiration time
        expiration = datetime.now(timezone.utc) + timedelta(hours=1)
        token = jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS256")
        return token 
