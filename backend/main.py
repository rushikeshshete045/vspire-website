from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="VSpireInnovations Website API",
    description="Backend API for VSpireInnovations company website",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

@app.get("/api/health")
def health_check():
    return {
        "status": "success",
        "message": "VSpireInnovations backend is running"
    }

@app.get("/api/company")
def company_info():
    return {
        "name": "VSpireInnovations",
        "tagline": "We Vision Inspiration",
        "services": [
            "Artificial Intelligence",
            "Data Science",
            "DevOps",
            "MLOps",
            "Full Stack Development"
        ]
    }