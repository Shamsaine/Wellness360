from flask import Flask, jsonify
from flask_cors import CORS
from routes import register_routes

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Register routes
register_routes(app)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
