from flask import request, jsonify
from bson.objectid import ObjectId
from . import app, mongo
from .models import User, UserPreferences
from datetime import datetime

def parse_roles(data):
    roles = []
    if data.get('is_user_admin'):
        roles.append('admin')
    if data.get('is_user_manager'):
        roles.append('manager')
    if data.get('is_user_tester'):
        roles.append('tester')
    return roles

def format_user(user):
    return {
        "user": user["username"],
        "password": user["password"],
        "is_user_admin": "admin" in user["roles"],
        "is_user_manager": "manager" in user["roles"],
        "is_user_tester": "tester" in user["roles"],
        "user_timezone": user["preferences"]["timezone"],
        "is_user_active": user["active"],
        "created_at": datetime.utcfromtimestamp(user["created_ts"]).isoformat() + 'Z'
    }

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    roles = parse_roles(data)
    preferences = UserPreferences(timezone=data['user_timezone'])
    user = User(username=data['username'], password=data['password'], roles=roles, preferences=preferences)
    mongo.db.users.insert_one(user.to_dict())
    return jsonify({"message": "User created successfully"}), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        user.pop('_id', None)  # Remove o campo _id
        result.append(format_user(user))
    return jsonify({"users": result})

@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one_or_404({"_id": ObjectId(user_id)})
    user.pop('_id', None)  # Remove o campo _id
    return jsonify(format_user(user))

@app.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    roles = parse_roles(data)
    preferences = UserPreferences(timezone=data['user_timezone'])
    update_data = {
        "username": data['username'],
        "password": data['password'],
        "roles": roles,
        "preferences": preferences.__dict__,
        "active": data.get('is_user_active', True),
        "created_ts": datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%SZ').timestamp()
    }
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return jsonify({"message": "User updated successfully"})

@app.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return jsonify({"message": "User deleted successfully"})