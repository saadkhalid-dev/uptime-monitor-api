from fastapi import FastAPI

app = FastAPI(title = "Uptime Monitor API")

@app.get("/health")
def health_check():
    return {"Status" : "OK"}