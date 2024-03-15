from fastapi import Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

# Connect to MongoDB
DATABASE_URL = config("MONGODB_URL")

async def get_db():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client.my_portfolio
        yield db
    finally:
        client.close()

db = get_db()

# Collection
user_collection = db.get_collection("users")
portfolio_collection = db.get_collection("portfolios")