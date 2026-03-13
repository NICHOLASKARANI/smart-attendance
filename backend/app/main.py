from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uuid
import random

app = FastAPI(title="Smart Attendance System", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data
users = [
    {"id": str(uuid.uuid4()), "name": "John Doe", "department": "Computer Science"},
    {"id": str(uuid.uuid4()), "name": "Jane Smith", "department": "Engineering"},
    {"id": str(uuid.uuid4()), "name": "Bob Johnson", "department": "Business"}
]

attendance_records = []

@app.get("/")
async def root():
    return {
        "message": "🎓 Smart Attendance System API",
        "version": "1.0.0",
        "status": "running (demo mode)"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/v1/face/detect")
async def detect_face():
    # Simulate face detection
    success = random.choice([True, False])
    
    if success:
        user = random.choice(users)
        record = {
            "id": str(uuid.uuid4()),
            "user_id": user["id"],
            "user_name": user["name"],
            "check_in_time": datetime.now().isoformat(),
            "status": "present",
            "confidence": round(random.uniform(0.85, 0.98), 2)
        }
        attendance_records.append(record)
        
        return {
            "success": True,
            "message": f"Welcome {user['name']}!",
            "user_name": user["name"],
            "confidence_score": record["confidence"],
            "attendance_recorded": True
        }
    else:
        return {
            "success": False,
            "message": "Face not recognized. Please try again.",
            "attendance_recorded": False
        }

@app.get("/api/v1/attendance/today")
async def get_today_attendance():
    today = datetime.now().date().isoformat()
    return {
        "date": today,
        "total_present": len(attendance_records),
        "total_absent": 50,
        "attendance_percentage": 85
    }

@app.get("/api/v1/attendance/recent")
async def get_recent_attendance(limit: int = 10):
    return attendance_records[-limit:] if attendance_records else []

@app.get("/api/v1/users")
async def get_users():
    return users