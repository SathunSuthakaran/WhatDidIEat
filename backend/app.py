from fastapi import FastAPI
from routers import upload, analyze

app = FastAPI(
    title="FoodVision API",
    description="Backend for estimating nutritional value from food images",
    version="0.1"
)

app.include_router(upload.router)
app.include_router(analyze.router)

@app.get("/")
async def root():
    return {"message": "FoodVision backend is running!"}
