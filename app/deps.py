# app/deps.py
import os
import firebase_admin
from firebase_admin import auth, credentials, firestore
from dotenv import load_dotenv

load_dotenv()

FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID")

# initialize firebase admin (handle multiple initializations)
if not firebase_admin._apps:
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  # path to json
    if cred_path:
        cred = credentials.Certificate(cred_path)
    else:
        # fallback: read JSON from env var FIREBASE_ADMIN_CREDENTIALS_JSON
        import json
        cred_json = os.getenv("FIREBASE_ADMIN_CREDENTIALS_JSON")
        cred = credentials.Certificate(json.loads(cred_json))
    firebase_admin.initialize_app(cred, {"projectId": FIREBASE_PROJECT_ID})

db = firestore.client()

def verify_id_token(id_token: str):
    try:
        decoded = auth.verify_id_token(id_token)
        return decoded  # dict with uid and email
    except Exception as e:
        raise
