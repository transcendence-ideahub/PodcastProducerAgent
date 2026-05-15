from pymongo import MongoClient
import logging

MONGO_OPTS = {
    "serverSelectionTimeoutMS": 5000,
    "connectTimeoutMS": 5000,
    "socketTimeoutMS": 5000,
    "tls": True,
    "tlsAllowInvalidCertificates": False
}

def get_client(connection_string: str):
    return MongoClient(connection_string, **MONGO_OPTS)

def save_podcast_data(connection_string: str, data: dict) -> bool:
    """Save finalized podcast assets to MongoDB."""
    try:
        client = get_client(connection_string)
        db = client.get_database("podcast_db")
        collection = db.get_collection("episodes")
        result = collection.insert_one(data)
        logging.info(f"Successfully inserted podcast data with ID: {result.inserted_id}")
        return True
    except Exception as e:
        logging.error(f"Failed to save to MongoDB: {e}")
        raise e

from bson import ObjectId

def get_all_podcast_data(connection_string: str) -> list:
    """Retrieve all historical podcast assets from MongoDB."""
    try:
        client = get_client(connection_string)
        db = client.get_database("podcast_db")
        collection = db.get_collection("episodes")
        
        records = list(collection.find({}))
        for r in records:
            if '_id' in r:
                r['_id'] = str(r['_id'])
        return records
    except Exception as e:
        logging.error(f"Failed to fetch from MongoDB: {e}")
        return []

def delete_podcast_data(connection_string: str, record_id: str) -> bool:
    """Delete a specific project from MongoDB."""
    try:
        client = get_client(connection_string)
        db = client.get_database("podcast_db")
        collection = db.get_collection("episodes")
        
        result = collection.delete_one({"_id": ObjectId(record_id)})
        return result.deleted_count > 0
    except Exception as e:
        logging.error(f"Failed to delete from MongoDB: {e}")
        return False

