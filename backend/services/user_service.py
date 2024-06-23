from models import User
from models import CreateUserRequest
import sqlite3
from sqlite3 import Error
import hashlib

class UserService:
    def __init__(self, db_file='calculation.db'):
        self.db_file = db_file

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn
    

    def validate_user_data(self, create_request: CreateUserRequest):
        if not isinstance(create_request, CreateUserRequest):
            return False, "Invalid user format. Expected a CreateUserRequest object."
            
        if not isinstance(create_request.username, str):
            return False, "Invalid data type for username. Expected string."
            
        if not isinstance(create_request.password, str):
            return False, "Invalid data type for password. Expected string."
            
        if create_request.role not in ["scientist", "student"]:
            return False, "Invalid role. Expected 'scientist' or 'student'."
            
        if len(create_request.password) < 8:
            return False, "Password must be at least 8 characters long."
        if not any(char.isupper() for char in create_request.password):
            return False, "Password must contain at least one uppercase letter."
        if not any(char.islower() for char in create_request.password):
            return False, "Password must contain at least one lowercase letter."
        if not any(char.isdigit() for char in create_request.password):
            return False, "Password must contain at least one number."
        

        return True, "User is valid."
            

    def create_user(self, create_request: CreateUserRequest):
        # This function should handle the user creation logic
        print(f"Received user in create_user: {create_request.model_dump()}")

        is_valid, message = self.validate_user_data(create_request)
        if not is_valid:
            return {"error": message} 
        
        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(create_request.password.encode('utf-8')).hexdigest()

        
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO users (username, hashed_password, role)
                    VALUES (?, ?, ?)
                """, (create_request.username, hashed_password, create_request.role))
                conn.commit()
                return {"message": "User created", "user": create_request.username}
            except Error as e:
                print(e)
                return {"error": e}
            finally:
                conn.close()
        return {"error": "Database connection failed."}

    def get_user_role(self, username: str) -> str:
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT role FROM users WHERE username = ?", (username,))
                row = cursor.fetchone()
                if row:
                    return row[0] 
                else:
                    return "unknown" 
            except Error as e:
                print(e)
                return "error"
            finally:
                conn.close()
        return "error"
