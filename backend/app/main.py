from fastapi import FastAPI

from app.api.v1.vendor import router as vendor_router

app = FastAPI(title="Studio API")

app.include_router(vendor_router)


@app.get("/")
def health():
    return {
        "status": "ok",
        "service": "Studio API",
    }