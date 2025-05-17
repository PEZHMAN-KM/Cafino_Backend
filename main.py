from fastapi import FastAPI
from database import models
from fastapi.staticfiles import StaticFiles
from database.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from authentication import authentication_route
from routers.admin_routers import admin_user

origins = [
    "http://localhost:*",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:8000"
]



app = FastAPI(
    title="Cafino",
    version="0.0.1",
    debug=True
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Reflect the allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
app.include_router(authentication_route.router)
app.include_router(admin_user.router)





app.mount('/files', StaticFiles(directory='pictures'), name='files')

Base.metadata.create_all(engine)


@app.get("/")
async def cafino():
    return "Welcome to Cafino"


if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")

    except Exception as first_error:
        print(f"Primary host failed: {first_error}")

        try:
            uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="debug")

        except Exception as fallback_error:
            print(f"Fallback host also failed: {fallback_error}")