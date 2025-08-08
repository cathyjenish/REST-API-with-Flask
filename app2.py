from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}

# GET: Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET: Fetch user by ID
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404

# POST: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"message": "User created", "id": user_id}), 201

# PUT: Update existing user
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated"}), 200

# DELETE: Remove a user
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
