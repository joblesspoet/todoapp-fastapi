from fastapi import APIRouter, HTTPException
from typing import List

from models.todo import TodoItem

router = APIRouter()

todos = []
TODO_ROUTE = "/{todo_id}"


# Get all todos


@router.get("")
async def get_all_todos():
    return {
        "todos": todos
    }

# Create New Todo Item


@router.post("")
async def create_todo(item: TodoItem):
    todos.append(item)
    return {
        "todo": todos
    }

# Get a Todo Item


@router.get(TODO_ROUTE)
async def get_todo(todo_id: int):
    for todo in todos:
        if (todo.id == todo_id):
            return {"todo": todo}
    return {"error": "No todo item found"}

# Update New Todo Item


@router.put(TODO_ROUTE)
async def update_todo(todo_id: int, item: TodoItem):
    for todo in todos:
        if todo.id == todo_id:
            todo.description = item.description
            return todo  # Return the updated todo item directly
    raise HTTPException(status_code=404, detail="Todo item not found")

# Delete Todo Item


@router.delete(TODO_ROUTE)
async def delete_todo(todo_id: int):
    for todo in todos:
        if (todo.id == todo_id):
            todos.remove(todo)
            return {"message": "Item removed successfully."}
    return {
        "error": "No Item found to remove."
    }

# Export the router instance
todo_router = router
