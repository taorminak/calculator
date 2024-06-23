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

    def add(self, operand1: float, operand2: float) -> float:
        # Perform addition and return the result
        return operand1 + operand2

    def subtract(self, operand1: float, operand2: float) -> float:
        # Perform subtraction and return the result
        return operand1 - operand2
    
    def multiplicate(self, operand1: float, operand2: float) -> float:
        # Perform multiplication and return the result
        return operand1 * operand2
    
    def divide(self, operand1: float, operand2: float) -> float:
        # Perform division and return the result
        return operand1 / operand2
    
    def modulo(self, operand1: float, operand2: float) -> float:
        # Perform modulo operation and return the result
        return operand1 % operand2
    
    def exponentiate(self, operand1: float, operand2: float) -> float:
        # Perform exponentiation and return the result
        return operand1 ** operand2

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
