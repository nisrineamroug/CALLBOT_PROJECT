from fastapi import FastAPI
from app.routes import (
    claims_routes,
    customer_routes,
    policy_routes,
    agent_routes,
    escalation_routes,
    claimEntity_routes,
)

app = FastAPI(title="Insurance Callbot API", version="1.0.0")

# Routers
app.include_router(claims_routes.router, prefix="/claims", tags=["Claims"])
app.include_router(customer_routes.router, prefix="/customers", tags=["Customers"])
app.include_router(policy_routes.router, prefix="/policies", tags=["Policies"])
app.include_router(agent_routes.router, prefix="/agents", tags=["Agents"])
app.include_router(escalation_routes.router, prefix="/escalations", tags=["Escalations"])
app.include_router(claimEntity_routes.router, prefix="/claim-entities", tags=["ClaimEntities"])

@app.get("/")
def root():
    return {"message": "Insurance Callbot API is running"}
