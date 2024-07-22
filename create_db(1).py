"""
Name = Sneha Malhotra
Student ID = 10330536
Group = Sneha Malhotra , Nisharg Patel , Mahenur Master , Siddharth Patel

Description:
 Creates the people table in the  database and populates it with 200 fake people.

Usage:
 python create_db.py 
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')
con = sqlite3.connect(db_path)
# Get a Cursor object that can be used to run SQL queries on the database.
cur = con.cursor()

def main():
    create_people_table()
    populate_people_table()
    con.close()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"

    create_ppl_tbl_query = """
        CREATE TABLE IF NOT EXISTS people
        (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            province TEXT NOT NULL,
            bio TEXT,
            age INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
        );
    """
    cur.execute(create_ppl_tbl_query)
    con.commit()    
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    add_person_query = """
        INSERT INTO people
        (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """


    fake = Faker("en_CA")

    for _ in range(200):
        new_person = (
        fake.name(),
        fake.email(),
        fake.address(),
        fake.city(),
        fake.administrative_unit(),
        fake.text(max_nb_chars=200),
        fake.random_int(min=1, max=100),
        datetime.now(),
        datetime.now()) 
        cur.execute(add_person_query, new_person)
    
    con.commit()    
    return

if __name__ == '__main__':
   main()


