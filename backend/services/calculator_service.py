from sqlite3 import Error
import sqlite3

class CalculatorService:
    def __init__(self, db_file='calculation.db',):
        self.db_file = db_file

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def save_calculation(self, user_id: int, operand1: float, operand2: float, result: float, calculation_type: str):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO calculations (user_id, operand1, operand2, result, calculation_type)
                    VALUES (?, ?, ?, ?, ?)
                """, (user_id, operand1, operand2, result, calculation_type))
                conn.commit()
                conn.close()
            except Error as e:
                print(e)

    def add(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform addition and return the result
        result = operand1 + operand2
        self.save_calculation(user_id, operand1, operand2, result, 'addition')
        return result

    def subtract(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform subtraction and return the result
        result = operand1 - operand2
        self.save_calculation(user_id, operand1, operand2, result, 'subtraction')
        return result
    
    def multiplicate(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform multiplication and return the result
        result = operand1 * operand2
        self.save_calculation(user_id, operand1, operand2, result, 'multiplication')
        return result
    
    def divide(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform division and return the result
        result = operand1 / operand2
        self.save_calculation(user_id, operand1, operand2, result, 'division')
        return result
    
    def modulo(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform modulo operation and return the result
        result = operand1 % operand2
        self.save_calculation(user_id, operand1, operand2, result, 'modulo')
        return result
    
    def exponentiate(self, user_id: int, operand1: float, operand2: float) -> float:
        # Perform exponentiation and return the result
        result = operand1 ** operand2
        self.save_calculation(user_id, operand1, operand2, result, 'exponentiation')
        return result

    def get_calculations(self):
        conn = self.create_connection()
        if conn is None:
            return {"error": "Failed to connect to database."}

        query = """
            SELECT operand1, operand2, result, calculation_type
            FROM calculations
        """
        cursor = conn.cursor()
        cursor.execute(query)
        calculations = cursor.fetchall()
        return calculations
