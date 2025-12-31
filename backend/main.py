from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from model import FundRecommender
import uvicorn

app = FastAPI(title="Mutual Fund Recommender")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Model
recommender = FundRecommender()

class UserProfile(BaseModel):
    investment_amount: float
    risk_appetite: str # Low, Medium, High
    age: int
    duration: int # Years
    sip_or_lumpsum: str
    net_worth: Optional[float] = 0
    dependents: Optional[int] = 0
    salary: Optional[float] = 0
    savings: Optional[float] = 0

@app.get("/")
def read_root():
    return {"message": "Welcome to MF Recommender API"}

@app.post("/recommend")
def get_recommendations(profile: UserProfile):
    try:
        user_data = profile.dict()
        recommendations = recommender.get_recommendations(user_data)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
