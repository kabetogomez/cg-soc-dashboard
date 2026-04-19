from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
from datetime import datetime

app = FastAPI(title="SOC Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IPCheckRequest(BaseModel):
    ip: str

@app.get("/")
async def root():
    return {"status": "SOC Dashboard funcionando!", "time": str(datetime.now())}

@app.get("/api/news")
async def get_news():
    news = [
        {"title": "🚨 LockBit Ransomware Ecopetrol 🇨🇴", "severity": 9, "link": "https://bleepingcomputer.com"},
        {"title": "🔴 CVE-2024-1234 Apache Struts", "severity": 8, "link": "https://thehackernews.com"},
        {"title": "🟡 Phishing BCP Perú 🇵🇪", "severity": 7, "link": "https://krebsonsecurity.com"},
        {"title": "🟠 Malware Android México 🇲🇽", "severity": 6, "link": "https://malwarebytes.com"}
    ]
    return {"news": news * 5, "total": 20}

@app.post("/api/ip/check")
async def check_ip(request: IPCheckRequest):
    # Simular análisis real
    risk_level = random.choice(["LIMPIO", "SOSPECHOSO", "MALICIOSO"])
    score = random.randint(0, 100)
    
    return {
        "ip": request.ip,
        "risk": risk_level,
        "score": score,
        "results": {
            "alienvault": {"reputation": score - 50, "pulses": random.randint(0, 12)},
            "urlscan": {"results": random.randint(0, 45), "malicious": max(0, score//15)},
            "hybrid": {"detections": random.randint(0, 8)},
            "abuseipdb": {"confidence": score, "reports": random.randint(0, 150)}
        },
        "checked": str(datetime.now())
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
