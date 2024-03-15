
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
import pymongo

client = AsyncIOMotorClient("mongodb+srv://admin:7j9nXmuOvVY4viL9@portfolio-cluster.ewd0sam.mongodb.net/mongoAPIdb?retryWrites=true&w=majority&appName=portfolio-cluster")

# client = AsyncIOMotorClient(settings.mongodb_uri)

db = client[settings.database_name]
tokens = db.get_collection("tokens")
user_collection = db.get_collection("users")

