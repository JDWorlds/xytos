from app import app, db
from models import Equipment, Battery, TestProfile, TestSession, MonitoringData
from datetime import datetime, timedelta

with app.app_context():
    # ───── 설비 샘플 생성 ─────
    equip1 = Equipment(
        name="Battery Tester A",
        model="BT-1000",
        location="Lab 1",
        manufacturer="TestTech Inc.",
        install_date=datetime(2023, 5, 10),
        status="정상"
    )

    # ───── 배터리 샘플 생성 ─────
    battery1 = Battery(
        serial_number="BAT123456",
        type="Li-ion",
        capacity_mAh=3000,
        manufacturer="BatteryCorp",
        production_date=datetime(2024, 1, 15)
    )

    # ───── 테스트 프로파일 샘플 생성 ─────
    profile1 = TestProfile(
        name="Standard Charge-Discharge",
        description="4.2V charge / 0.5A discharge / 3.0V cutoff",
        charge_voltage=4.2,
        discharge_current=0.5,
        cutoff_voltage=3.0
    )

    # ───── 테스트 세션 샘플 생성 ─────
    session1 = TestSession(
        battery=battery1,
        equipment=equip1,
        profile=profile1,
        start_time=datetime.now() - timedelta(hours=1),
        end_time=datetime.now(),
        result="성공"
    )

    # ───── 모니터링 데이터 샘플 생성 ─────
    data_points = []
    for i in range(6):  # 10분 간격으로 1시간치 데이터
        data_points.append(MonitoringData(
            session=session1,
            timestamp=session1.start_time + timedelta(minutes=i*10),
            voltage=4.2 - i*0.2,
            current=0.5,
            temperature=25.0 + i * 0.3,
            internal_resistance=50 + i,
            state_of_charge=100 - i*15
        ))

    # DB에 저장
    db.session.add_all([equip1, battery1, profile1, session1] + data_points)
    db.session.commit()

    print("✅ 샘플 데이터 삽입 완료")