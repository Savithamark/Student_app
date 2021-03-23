import sqlite3

#Open database
conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY, 
		password TEXT,
		username TEXT,
		firstName TEXT,
		lastName TEXT 
		)''')
        
conn.execute('''CREATE TABLE Lectures
(
    Lecture_Id INTEGER PRIMARY KEY,
    first_name  TEXT NOT NULL,
    last_name   TEXT NOT NULL,
    gender TEXT NOT NULL,
    Qualification TEXT,    
    Experience INT NOT NULL,
    About TEXT,
    DOMAIN TEXT NOT NULL
)''')
        
conn.close()

