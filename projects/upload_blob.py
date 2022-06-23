import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, __version__

load_dotenv()

class Blob:
    def upload(filename=str, filepath=str):
        connection_string = os.getenv("BLOB_CONNECTION_STRING")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container="", blob=filename)
        with open(filepath, "rb") as file:
            blob_client.upload_blob(file)
        