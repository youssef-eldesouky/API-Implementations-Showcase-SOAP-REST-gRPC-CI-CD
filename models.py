import sqlite3

# Database setup function
def initialize_database():
    # Connect to SQLite database (it creates 'tasks.db' if it doesn't exist)
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    # Create a table for tasks if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()  # Save changes
    conn.close()   # Close the connection

# Function to add a new task to the database
def add_task(task_name, status='incomplete'):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task_name, status) VALUES (?, ?)', (task_name, status))
    conn.commit()
    conn.close()

# Function to retrieve all tasks
def get_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Function to update a task's status
def update_task_status(task_id, status):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
    conn.commit()
    conn.close()

# Function to delete a task
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

from models import add_task, get_all_tasks

# Add some tasks
add_task("Buy groceries")
add_task("Complete software architecture assignment")

# Retrieve and print all tasks
tasks = get_all_tasks()
print("Tasks in the database:")
for task in tasks:
    print(task)
