from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI(title = "Uptime Monitor API")

class MonitorCreate(BaseModel):
    name: str
    url: HttpUrl

@app.get("/health")
def health_check():
    return {"Status" : "OK"}

@app.post("/monitors")
def create_monitor(monitor: MonitorCreate):
    return {
        "ID" : 1,
        "Name": monitor.name,
        "URL": monitor.url
    }