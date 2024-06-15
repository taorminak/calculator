import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional

# Secret key for JWT encoding
SECRET_KEY = "your_secret_key"

class AuthService:
    def authenticate_user(self, username: str, password: str) -> Optional[str]:
        # This function should verify username and password with your data source.
        # If valid, return a JWT token.
        if username == "test" and password == "password":
            return self._create_token(username)
        return None

    def _create_token(self, username: str) -> str:
        # Create a JWT token with an expiration time
        expiration = datetime.now(timezone.utc) + timedelta(hours=1)
        token = jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS256")
        return token
