import hashlib
import os
import requests

API_URL = "https://encrypt-phonetracker.dev-lorenzo.workers.dev/"

def get_api_key():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("encryptedkey"), data.get("iv")
    except:
        return None, None

def hash_phone_md5(phone: str) -> str:
    md5 = hashlib.md5()
    md5.update(phone.encode())
    return md5.hexdigest()

def log_hashed_data(hashed_phone: str, logfile="phones.log"):
    logfile_path = os.path.join(os.path.dirname(__file__), logfile)
    with open(logfile_path, "a") as f:
        f.write(f"Hashed Phone (MD5): {hashed_phone}\n\n")

def encrypt_and_log(phone: str):
    if not phone:
        raise ValueError("No phone input provided")
    encrypted_key, iv = get_api_key()
    if encrypted_key:
        print(f"Fetched API key (length {len(encrypted_key)})")
    hashed_phone = hash_phone_md5(phone)
    log_hashed_data(hashed_phone)
