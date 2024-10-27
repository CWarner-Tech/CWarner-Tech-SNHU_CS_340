from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD():
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password, host, port, database, collection):
        # Initializing the MongoClient to access MongoDB databases and collections.

        # Connection Variables
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the MongoDB collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)  # data should be a dictionary
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """Query documents from MongoDB."""
        try:
            cursor = self.collection.find(query)
            return list(cursor)  # Convert cursor to list of documents
        except Exception as e:
            print(f"Error querying documents: {e}")
            return []

    def update(self, query, new_data):
        """Update document in MongoDB."""
        try: 
            result = self.collection.update_many(query, {'$set': new_data})
            return result.modified_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def delete(self, query):
        """Delete document from MongoDB."""
        try: 
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def check_connection(self):
        """Check if the connection to the database is working."""
        try:
            # Attempt to count documents in the collection
            count = self.collection.count_documents({})
            print(f"Connection successful! Number of documents in the 'animals' collection: {count}")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
