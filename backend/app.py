from flask import Flask, jsonify
from flask_cors import CORS
from api import api_bp
from flask_sqlalchemy import SQLAlchemy
from models import db, Equipment, Battery, TestProfile, TestSession, MonitoringData
from config import DATABASE_URI

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(api_bp)

# 데이터베이스 생성
with app.app_context():
    db.create_all()

# 샘플 데이터 추가
@app.route("/api/init")
def init_db():
    db.session.add_all([
        #Product(name="Laptop", price=999.99, image_url="https://via.placeholder.com/150"),
        #Product(name="Phone", price=499.99, image_url="https://via.placeholder.com/150"),
        #Product(name="Headphones", price=199.99, image_url="https://via.placeholder.com/150"),
    ])
    db.session.commit()
    return jsonify({"message": "Database initialized!"})

# 제품 목록 가져오기
#@app.route("/api/products", methods=["GET"])
#def get_products():
#    products = Product.query.all()
#    return jsonify([product.to_dict() for product in products])

if __name__ == "__main__":
    app.run(debug=True, port=5000)