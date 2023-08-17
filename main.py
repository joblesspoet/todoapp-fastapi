from fastapi import FastAPI, HTTPException
from routes.todo import todo_router

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello World"
    }


# Include the router
# You can specify a prefix if needed
app.include_router(todo_router, prefix="/todos")
