from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    conn = pymysql.connect(
    host="172.17.0.1",
    user="flaskuser",
    password="password123",
    database="projectdb"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    output = ""

    for row in rows:
        output += f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}<br>"

    conn.close()

    return output

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)