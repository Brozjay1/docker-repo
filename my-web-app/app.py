from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = psycopg2.connect(
        host='db',
        dbname='postgres',
        user='postgres',
        password='postgres'
    )
    return 'Hello, Docker with PostgreSQL!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
