from flask import Flask 
import os
app = Flask(__name__)


@app.route('/')
def home():
    return "hello"

if __name__ == '__main__':
    app.run(port=os.environ.get("port",5000),host="0.0.0.0")