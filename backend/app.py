from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from api import api_bp
from flask_sqlalchemy import SQLAlchemy
from models import db, Equipment, Battery, TestProfile, TestSession, MonitoringData
from config import DATABASE_URI

#Falsk 앱 초기화
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#DB & API 연동 및 블루프린트 등록
db.init_app(app)
app.register_blueprint(api_bp)

#SocketIO 초기화
socketio = SocketIO(app, cors_allowed_origins="*")

# 클라이언트 연결 확인 로그
@socketio.on('connect')
def handle_connect():
    print('✅ 클라이언트가 SocketIO에 연결되었습니다.')

# 데이터베이스 생성
#with app.app_context():
#    db.create_all()

# 샘플 실시간 데이터 전송 루프 (가상 시뮬레이션)
import threading
import time
import random

def simulate_monitoring_data():
    while True:
        time.sleep(3)  # 3초 간격
        sample_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'voltage': round(random.uniform(3.6, 4.2), 2),
        }
        socketio.emit('monitoring_update', sample_data)
        print('📡 실시간 데이터 전송:', sample_data)

# 별도 스레드로 모의 데이터 생성 시작
threading.Thread(target=simulate_monitoring_data, daemon=True).start()

# 샘플 데이터 추가
#@app.route("/api/init")
#def init_db():
#    db.session.add_all([
        #Product(name="Laptop", price=999.99, image_url="https://via.placeholder.com/150"),
        #Product(name="Phone", price=499.99, image_url="https://via.placeholder.com/150"),
        #Product(name="Headphones", price=199.99, image_url="https://via.placeholder.com/150"),
#    ])
#    db.session.commit()
#    return jsonify({"message": "Database initialized!"})

# 제품 목록 가져오기
#@app.route("/api/products", methods=["GET"])
#def get_products():
#    products = Product.query.all()
#    return jsonify([product.to_dict() for product in products])

if __name__ == "__main__":
    app.run(debug=True, port=5000)