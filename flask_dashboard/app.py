from flask import Flask
from flask_cors import CORS
from routes.dashboard_routes import dashboard_bp
from pymongo import MongoClient

app = Flask(__name__)
print("🚀 Flask app is starting...")
CORS(app)

# MongoDB connection
client = MongoClient("mongodb+srv://mo7amednabih:Cpz0xP5eJV0NsLDQ@cluster0.lpj4mo9.mongodb.net/")
db = client["CareDent"]

# Register Blueprints
app.register_blueprint(dashboard_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
