from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Endpoint to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    print("Received request to add user:", request.method, request.json)
    data = request.json
    new_user = User(name=data['name'], username=data['username'], password=data['password'])
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [
        {
            "id": user.id,
            "name": user.name,
            "username": user.username,
            # We typically don't return passwords in API responses for security reasons
            # "password": user.password  
        } for user in users
    ]

    return jsonify(user_list)

# Endpoint to remove a user
@app.route('/remove_user/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User removed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)