from sqlalchemy.orm import Session
from app.models import User, Appointment, Prescription
from app.schemas import UserCreate, AppointmentCreate, PrescriptionCreate
from app.auth import hash_password



def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_pw,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    return new_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()



def create_appointment(db: Session, appointment: AppointmentCreate):
    new_appointment = Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        date_time=appointment.date_time,
        status=appointment.status
    )
    db.add(new_appointment)
    db.commit()
    return new_appointment

def get_all_appointments(db: Session):
    return db.query(Appointment).all()



def create_prescription(db: Session, prescription: PrescriptionCreate):
    new_prescription = Prescription(
        appointment_id=prescription.appointment_id,
        doctor_id=prescription.doctor_id,
        patient_id=prescription.patient_id,
        medicines=prescription.medicines,
        notes=prescription.notes
    )
    db.add(new_prescription)
    db.commit()
    return new_prescription

def get_all_prescriptions(db: Session):
    return db.query(Prescription).all()
