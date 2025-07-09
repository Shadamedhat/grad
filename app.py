from flask import Flask
from flask_cors import CORS
import os
import traceback

app = Flask(__name__)
print("🚀 Flask app is starting...")
CORS(app)

# Endpoint بسيط لاختبار جاهزية السيرفر
@app.route("/ping")
def ping():
    return "pong"

# MongoDB connection
try:
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://mo7amednabih:Cpz0xP5eJV0NsLDQ@cluster0.lpj4mo9.mongodb.net/")
    db = client["CareDent"]
    print("✅ Connected to MongoDB")
except Exception as e:
    db = None
    print("❌ Failed to connect to MongoDB")
    print(traceback.format_exc())

# Register Blueprints
try:
    from flask_dashboard.routes.dashboard_routes import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix="/api")
    print("✅ Blueprint registered")
except Exception as e:
    print("❌ Failed to register blueprint")
    print(traceback.format_exc())

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Azure يبعت البورت هنا
    app.run(debug=True, host='0.0.0.0', port=port)