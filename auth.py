"""
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
    return decoded"""

import os
import json
import firebase_admin
from firebase_admin import credentials, auth

firebase_json = os.getenv("FIREBASE_CREDENTIALS")

# convert string -> dict
cred_dict = json.loads(firebase_json)

cred = credentials.Certificate(cred_dict)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def verify_user(token: str):
    decoded = auth.verify_id_token(token, clock_skew_seconds=10)
    return decoded