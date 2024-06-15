from models import User

class UserService:
    def create_user(self, user: User):
        # This function should handle the user creation logic
        return {"message": "User created", "user": user}
