from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from authentication import authentication_route
from routers.general_routers import user, food, order, notification, category
from routers.waitress_routers import waitress_notification
from routers.admin_routers import admin_food, admin_order, admin_waitress
from routers.super_admin_routers import (
    super_admin_super_admin,
    super_admin_user,
    super_admin_category,
    super_admin_admin
)

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
app.include_router(user.router)
app.include_router(food.router)
app.include_router(order.router)
app.include_router(notification.router)
app.include_router(category.router)
app.include_router(waitress_notification.router)
app.include_router(admin_food.router)
app.include_router(admin_order.router)
app.include_router(admin_waitress.router)
app.include_router(super_admin_super_admin.router)
app.include_router(super_admin_user.router)
app.include_router(super_admin_category.router)
app.include_router(super_admin_admin.router)
app.include_router(authentication_route.router)






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