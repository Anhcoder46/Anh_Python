import os
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from dotenv import load_dotenv

# Tải biến môi trường
load_dotenv()

app = Flask(__name__)
CORS(app) # Cho phép Frontend gọi API

PORT = os.getenv("PORT", 5000)
DB_URL = os.getenv("DB_URL")
APP_NAME = os.getenv("APP_NAME", "DevOps_Python_Project")

# Hàm kết nối Database
def get_db_connection():
    return psycopg2.connect(DB_URL)

# 3.1 Trang thông tin cá nhân
@app.route('/about', methods=['GET'])
def about():
    return f"""
    <h2>Thông tin sinh viên</h2>
    <p><strong>Họ tên sinh viên:</strong> Đức Anh</p>
    <p><strong>Mã số sinh viên:</strong> 2251220096</p>
    <p><strong>Lớp:</strong> 22CT1</p>
    <p><strong>App Name:</strong> {APP_NAME}</p>
    """

# 3.2 Health Check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

# API 1: GET - Lấy danh sách users từ DB
@app.route('/api/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": row[0], "name": row[1]} for row in users])

# API 2: POST - Thêm user mới vào DB
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    if not name:
         return jsonify({"error": "Name is required"}), 400
         
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name) VALUES (%s) RETURNING id;', (name,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "name": name}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))