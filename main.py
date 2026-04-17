from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deine KI ist online 🚀"}
