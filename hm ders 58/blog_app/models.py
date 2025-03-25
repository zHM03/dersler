import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def save(self):
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
        (self.title, self.content))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        conn.close()
        return posts
    
    @staticmethod
    def get_by_id(post_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post = cursor.fetchone()
        conn.close()
        return post
    
    @staticmethod
    def update(post_id, title, content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?",
        (title, content, post_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(post_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def create_table():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
        )
        ''')
        conn.commit()
        conn.close()