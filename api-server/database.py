import sqlite3

# Connect to the SQLite3 database.
# If 'messages.db' does not exist, it will be created automatically.
# check_same_thread=False allows usage across different threads (important for FastAPI's async behavior).
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

"""
    Retrieve all messages from the database.
    Returns:
    List of dictionaries, each containing 'id' and 'message' keys.
"""
def get_all_messages():
    cursor.execute('SELECT * FROM messages')
    rows = cursor.fetchall()
    return [{"id": row[0], "message": row[1]} for row in rows]


"""
    Insert a new message into the database.
    Args:
        content (str): The message content.
    Returns:
        The ID of the newly inserted message.
"""
def create_message(content):
    cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
    conn.commit()
    return cursor.lastrowid


"""
    Update the content of an existing message.
    Args:
        message_id (int): ID of the message to update.
        new_content (str): New content for the message.
    Returns:
        Number of rows updated (0 if not found).
"""
def update_message(message_id, new_content):
    cursor.execute('UPDATE messages SET content = ? WHERE id = ?', (new_content, message_id))
    conn.commit()
    return cursor.rowcount  # number of rows updated


"""
    Delete a message from the database.
    Args:
        message_id (int): ID of the message to delete.
    Returns:
        Number of rows deleted (0 if not found).
"""
def delete_message(message_id):
    cursor.execute('DELETE FROM messages WHERE id = ?', (message_id,))
    conn.commit()
    return cursor.rowcount  # number of rows deleted
