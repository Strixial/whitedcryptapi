from fastapi import FastAPI, Request, Header
import Whitecrypt
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
  return "dumbass"

class EncodePayload(BaseModel):
    plaintext: str

@app.post("/encode")
async def encode(payload: EncodePayload):
    plaintext = payload.plaintext
    try:
        encoded = Whitecrypt.Encode(plaintext)
    except:
        return {"success": False}
    return {"success": True, "result": encoded}

# Decode endpoint

class DecodePayload(BaseModel):
    ciphertext: str

@app.post("/decode")
async def decode(payload: DecodePayload):
    ciphertext = payload.ciphertext
    
    try:
        decoded = Whitecrypt.Decode(ciphertext)
    except:
        return {"success": False}
        
    return {"success": True, "result": decoded}

# Encrypt endpoint

class EncryptPayload(BaseModel):
    plaintext: str
    key: str

@app.post("/encrypt")
async def encrypt(payload: EncryptPayload):
    plaintext = payload.plaintext
    key = payload.key
    try:
        encrypted = Whitecrypt.Encrypt(plaintext, key)
    except:
        return {"success": False}
        
    return {"success": True, "result": encrypted}

# Decrypt endpoint

class DecryptPayload(BaseModel):
    ciphertext: str
    key: str

@app.post("/decrypt")
async def decrypt(payload: DecryptPayload):
    ciphertext = payload.ciphertext
    key = payload.key

    try:
        decrypted = Whitecrypt.Decrypt(ciphertext, key)
    except:
        return {"success": False}

    return {"success": True, "result": decrypted}
    
