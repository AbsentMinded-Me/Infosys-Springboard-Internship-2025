from fastapi import FastAPI 
from sqlFunctions import router

app = FastAPI()
app.include_router(router)
