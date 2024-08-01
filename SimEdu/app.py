from fastapi import FastAPI
from SimEdu.controller.user_controller import user_router
from SimEdu.controller.vectara_controller import vectara_router

app = FastAPI()

# Include routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(vectara_router, prefix="/vectara", tags=["Demo"])

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
