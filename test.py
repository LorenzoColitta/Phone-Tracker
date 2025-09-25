import os
import base64

# Generate 32 random bytes (256-bit AES key)
key_bytes = os.urandom(32)

# Encode to Base64 for storing in environment
key_b64 = base64.urlsafe_b64encode(key_bytes).decode()
print("AES key for environment variable:", key_b64)