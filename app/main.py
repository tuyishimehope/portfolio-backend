from fastapi import FastAPI


app = FastAPI()


@app.get("")
def start():
    return "Hello"


@app.get("/health/ready")
def health_checks():
    return {"status": "ready"}
