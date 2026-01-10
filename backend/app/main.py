from fastapi import FastAPI
from app.routes import claims, claim_status, faq

app = FastAPI(title="Insurance Callbot API", version="1.0.0")

# Routers
app.include_router(claims.router, prefix="/claims", tags=["Claims"])
app.include_router(claim_status.router, prefix="/claim_status", tags=["Claim Status"])
app.include_router(faq.router, prefix="/faq", tags=["FAQ"])

@app.get("/")
def root():
    return {"message": "Insurance Callbot API is running"}