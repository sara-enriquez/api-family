"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
member1={
    "id":jackson_family._generateId(),
    "name": "John",
    "age": 33,
    "lucky_numbers": [7,13,22]
}
jackson_family.add_member(member1)

member2={
    "id":jackson_family._generateId(),
    "name": "Jane",
    "age": 35,
    "lucky_numbers": [10,14,3]
}
jackson_family.add_member(member2)

member3={
    "id":jackson_family._generateId(),
    "name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
}
jackson_family.add_member(member3)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['POST'])
def add_people():
    data = request.get_json() 
    new_member = jackson_family.add_member(data)
    return jsonify({"msg":"new member succesfully added"}),200

@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    persona=jackson_family.get_member(id)
    if persona is None: 
        return  jsonify({"msg":"Member not found"}),404
    return jsonify(persona),200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    personas=jackson_family.delete_member(id)
    if personas is None: 
        return  jsonify({"msg":"Member not found"}),404
    return jsonify({"done":True}),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)