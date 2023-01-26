from fastapi import FastAPI
import WhitedCrypt
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
	return "dumbass"

class EncodePayload(BaseModel):
	mappingmethod: int
	plaintext: str
    

@app.post("/encode")
async def encode(payload: EncodePayload):
	mappingmethod = payload.mappingmethod
	plaintext = payload.plaintext
	try:
		encoded = WhitedCrypt.Encode(mappingmethod, plaintext)
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
		decoded = WhitedCrypt.Decode(ciphertext)
	except:
		return {"success": False}
	return {"success": True, "result": decoded}

# Encrypt endpoint

class EncryptPayload(BaseModel):
	hashing_algorithm_name: str
	is_mapped: bool
	plaintext: str
	key: str

@app.post("/encrypt")
async def encrypt(payload: EncryptPayload):
	hashing_algorithm_name = payload.hashing_algorithm_name
	is_mapped = payload.is_mapped
	plaintext = payload.plaintext
	key = payload.key
	try:
		encrypted = WhitedCrypt.Encrypt(hashing_algorithm_name, is_mapped, plaintext, key)
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
		decrypted = WhitedCrypt.Decrypt(ciphertext, key)
	except:
		return {"success": False}
	return {"success": True, "result": decrypted}

