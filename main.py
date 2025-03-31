from fastapi import FastAPI
from api.v1.router import api_router

app = FastAPI(title="Sensitive Word Filter API")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1992)