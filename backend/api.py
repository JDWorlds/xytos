from flask import Blueprint, jsonify, request
from models import db, Equipment, Battery, TestSession, MonitoringData
from datetime import datetime

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/equipments', methods=['GET'])
def get_equipments():
    equipments = Equipment.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "status": e.status,
        "location": e.location
    } for e in equipments])


@api_bp.route('/batteries', methods=['GET'])
def get_batteries():
    batteries = Battery.query.all()
    return jsonify([{
        "id": b.id,
        "serial_number": b.serial_number,
        "type": b.type,
        "capacity_mAh": b.capacity_mAh
    } for b in batteries])


@api_bp.route('/sessions/<int:id>', methods=['GET'])
def get_session(id):
    session = TestSession.query.get_or_404(id)
    return jsonify({
        "id": session.id,
        "battery_id": session.battery_id,
        "equipment_id": session.equipment_id,
        "profile_id": session.profile_id,
        "start_time": session.start_time.isoformat() if session.start_time else None,
        "end_time": session.end_time.isoformat() if session.end_time else None,
        "result": session.result,
        "monitoring_data": [{
            "timestamp": m.timestamp.isoformat(),
            "voltage": m.voltage,
            "current": m.current,
            "temperature": m.temperature
        } for m in session.monitoring_data]
    })


@api_bp.route('/sessions', methods=['GET', 'POST'])
def handle_sessions():
    if request.method == 'POST':
        data = request.get_json()
        new_session = TestSession(
            battery_id=data['battery_id'],
            equipment_id=data['equipment_id'],
            profile_id=data['profile_id'],
            start_time=datetime.now(),
            result='성공'
        )
        db.session.add(new_session)
        db.session.commit()
        return jsonify({"message": "Test session created", "id": new_session.id}), 201

    elif request.method == 'GET':
        sessions = TestSession.query.all()
        return jsonify([
            {
                "id": s.id,
                "battery_id": s.battery_id,
                "equipment_id": s.equipment_id,
                "profile_id": s.profile_id,
                "start_time": s.start_time.isoformat(),
                "end_time": s.end_time.isoformat() if s.end_time else None,
            }
            for s in sessions
        ])
