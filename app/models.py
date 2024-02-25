# app/models.py

from app import mysql
import MySQLdb

def create_user(username, password, email):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    mysql.connection.commit()
    cur.close()

def get_user(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    return user

def create_post(user_id, content):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO posts (user_id, content) VALUES (%s, %s)", (user_id, content))
    mysql.connection.commit()
    cur.close()

def get_posts(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE user_id = %s", (user_id,))
    posts = cur.fetchall()
    cur.close()
    return posts

def update_user_profile(user_id, phone_number, bio):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET phone_number = %s, bio = %s WHERE id = %s", (phone_number, bio, user_id))
    mysql.connection.commit()
    cur.close()

def get_user_info(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT username, email, phone_number, bio FROM users WHERE id = %s", (user_id,))
    user_info = cur.fetchone()  # Fetch the first row
    cur.close()
    if user_info:
        # Convert the tuple to a dictionary with keys
        user_info_dict = {
            'username': user_info[0],
            'email': user_info[1],
            'phone_number': user_info[2],
            'bio': user_info[3]
        }
        return user_info_dict
    else:
        return None

def get_posts_except_user_with_username(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT posts.*, users.username FROM posts INNER JOIN users ON posts.user_id = users.id WHERE posts.user_id != %s", (user_id,))
    posts = cur.fetchall()
    cur.close()
    return posts
def perform_user_search(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT users.*, GROUP_CONCAT(posts.content SEPARATOR ' ') AS all_posts FROM users LEFT JOIN posts ON users.id = posts.user_id WHERE username LIKE %s GROUP BY users.id", ('%' + username + '%',))
    users_data = cur.fetchall()
    cur.close()
    return users_data






