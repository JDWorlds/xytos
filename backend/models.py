from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Equipment(db.Model):
    __tablename__ = "equipment"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100))
    location = db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    install_date = db.Column(db.Date)
    status = db.Column(db.Enum("정상", "점검중", "고장"), default="정상")

    test_sessions = db.relationship("TestSession", back_populates="equipment")


class Battery(db.Model):
    __tablename__ = "battery"
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    type = db.Column(db.String(50))
    capacity_mAh = db.Column(db.Integer)
    manufacturer = db.Column(db.String(100))
    production_date = db.Column(db.Date)

    test_sessions = db.relationship("TestSession", back_populates="battery")


class TestProfile(db.Model):
    __tablename__ = "test_profile"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    charge_voltage = db.Column(db.Float)
    discharge_current = db.Column(db.Float)
    cutoff_voltage = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    test_sessions = db.relationship("TestSession", back_populates="profile")


class TestSession(db.Model):
    __tablename__ = "test_session"
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, db.ForeignKey("battery.id"), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("test_profile.id"), nullable=False)

    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    result = db.Column(db.Enum("성공", "실패", "중단"))

    battery = db.relationship("Battery", back_populates="test_sessions")
    equipment = db.relationship("Equipment", back_populates="test_sessions")
    profile = db.relationship("TestProfile", back_populates="test_sessions")
    monitoring_data = db.relationship("MonitoringData", back_populates="session")


class MonitoringData(db.Model):
    __tablename__ = "monitoring_data"
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey("test_session.id"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
    temperature = db.Column(db.Float)
    internal_resistance = db.Column(db.Float)
    state_of_charge = db.Column(db.Float)

    session = db.relationship("TestSession", back_populates="monitoring_data")