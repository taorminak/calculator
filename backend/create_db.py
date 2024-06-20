import sqlite3
from faker import Faker
import hashlib

conn = sqlite3.connect('calculation.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role TEXT NOT NULL
)
''')


num_users = 10

fake = Faker()

for _ in range(num_users):
    username = fake.user_name()
    email = fake.email()
    hashed_password = hashlib.sha256(fake.password().encode('utf-8')).hexdigest()
    created_at = fake.date_time_this_decade()
    role = fake.random_element(elements=('scientist', 'student'))

    cursor.execute('''
    INSERT INTO users (username, email, hashed_password, created_at, role)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, email, hashed_password, created_at, role))


conn.commit()

conn.close()

print(f"Successfully populated {num_users} users.")
