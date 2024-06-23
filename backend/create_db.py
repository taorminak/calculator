import sqlite3
from faker import Faker
import hashlib
from constants import ROLE_STUDENT, ROLE_SCIENTIST

conn = sqlite3.connect("calculation.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role TEXT NOT NULL
)
"""
)

num_users = 10

fake = Faker()

for _ in range(num_users):
    username = fake.user_name()
    hashed_password = hashlib.sha256(fake.password().encode("utf-8")).hexdigest()
    created_at = fake.date_time_this_decade()
    role = fake.random_element(elements=(ROLE_STUDENT, ROLE_SCIENTIST))

    cursor.execute(
        """
    INSERT INTO users (username, hashed_password, created_at, role)
    VALUES (?, ?, ?, ?)
    """,
        (username, hashed_password, created_at, role),
    )


cursor.execute(
    """
CREATE TABLE IF NOT EXISTS calculations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    operand1 REAL NOT NULL,
    operand2 REAL NOT NULL,
    result REAL NOT NULL,
    calculation_type TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
"""
)

calculations_data = [
    (1, 10.5, 5.2, 15.7, "addition"),
    (1, 8.3, 2.1, 6.2, "subtraction"),
    (2, 3.5, 2.5, 8.75, "multiplication"),
    (2, 9.5, 4.0, 2.375, "division"),
]

for data in calculations_data:
    user_id, operand1, operand2, result, calculation_type = data
    cursor.execute(
        """
    INSERT INTO calculations (user_id, operand1, operand2, result, calculation_type)
    VALUES (?, ?, ?, ?, ?)
    """,
        (user_id, operand1, operand2, result, calculation_type),
    )

conn.commit()
conn.close()

print(f"Successfully inserted calculations into the calculations table.")
