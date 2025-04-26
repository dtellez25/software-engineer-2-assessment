# database.py

import sqlite3

# Create a connection to the database (creates messages.db if it doesn't exist)
conn = sqlite3.connect('messages.db', check_same_thread=False)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the messages table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL
    )
''')

# Commit the changes
conn.commit()

# --- Helper functions ---

def get_all_messages():
    cursor.execute('SELECT * FROM messages')
    rows = cursor.fetchall()
    return [{"id": row[0], "message": row[1]} for row in rows]

def create_message(content):
    cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
    conn.commit()
    return cursor.lastrowid

def update_message(message_id, new_content):
    cursor.execute('UPDATE messages SET content = ? WHERE id = ?', (new_content, message_id))
    conn.commit()
    return cursor.rowcount  # number of rows updated

def delete_message(message_id):
    cursor.execute('DELETE FROM messages WHERE id = ?', (message_id,))
    conn.commit()
    return cursor.rowcount  # number of rows deleted
