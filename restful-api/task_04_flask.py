#!/usr/bin/python3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Users dictionary in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# /data endpoint: returns all usernames
@app.route("/data")
def data():
    return jsonify(list(users.keys()))


# /users/<username> endpoint
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


# /add_user endpoint: POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Run on all interfaces so you can access from outside the VM
    app.run(host="0.0.0.0", port=5000)
