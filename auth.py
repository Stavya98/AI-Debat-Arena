
import firebase_admin
from firebase_admin import credentials, auth
import os
import dotenv
dotenv.load_dotenv()
FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")

cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)

def verify_user(token:str):
    decoded = auth.verify_id_token(token)
    return decoded