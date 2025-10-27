from fastapi import FastAPI


app = FastAPI(title="Remote Compute Server")

@app.get("/")
def home():
    return {"message": "Server is running!"}

@app.get("/health")
def health():
    return {"status" : "healthy"}