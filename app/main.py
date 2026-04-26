from fastapi import FastAPI
from app.api.routes import router
import os
import uvicorn

app = FastAPI(title="Enterprise AI Backend")

app.include_router(router, prefix="/api/v1")  

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)