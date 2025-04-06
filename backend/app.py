from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from api import api_bp
from flask_sqlalchemy import SQLAlchemy
from models import db, Equipment, Battery, TestProfile, TestSession, MonitoringData
from config import DATABASE_URI

#Falsk 앱 초기화
app = Flask(__name__)
CORS(app, supports_credentials=True)
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#DB & API 연동 및 블루프린트 등록
db.init_app(app)
app.register_blueprint(api_bp)

#SocketIO 초기화
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

# 데이터베이스 모델 객체 -> 테이블 생성
with app.app_context():
    db.create_all()

# 샘플 실시간 데이터 전송 루프 (가상 시뮬레이션)
import threading
import time
import random

@socketio.on('connect')
def handle_connect():
    print('✅ 클라이언트가 SocketIO에 연결되었습니다.')


def emit_data():
    while True:
        data = {
            "equipment_id": 1,
            "temperature": round(random.uniform(20.0, 40.0), 2),
            "voltage": round(random.uniform(3.5, 4.2), 2),
            "current": round(random.uniform(0.5, 2.0), 2),
            "timestamp": time.time()
        }
        socketio.emit("monitor_data", data)
        print("📡 데이터 emit됨:", data)
        time.sleep(1)


if __name__ == "__main__":
    threading.Thread(target=emit_data, daemon=True).start()
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
    #app.run(debug=True, port=5000)