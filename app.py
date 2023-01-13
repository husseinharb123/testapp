from flask import Flask, jsonify,request 
import os
from google.cloud import firestore
db = firestore.Client()
app = Flask(__name__)



@app.route('/')
def home():
    return "hello"
@app.route('/adduser',methods = ["POST"])
def adduser():
    data = request.get_json()
    doc = db.collection('users').document().set(data)
    return "done"

@app.route('/users')
def getusers():
    items = []
    docs = db.collection('users').stream()
    for doc in docs:
        items.append(doc.to_dict())
    return jsonify(items)



if __name__ == '__main__':
    app.run(port=os.environ.get("port",5000),host="0.0.0.0")