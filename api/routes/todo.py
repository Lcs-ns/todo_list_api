from fastapi import APIRouter

todo_router = APIRouter(prefix="/api", tags="Todo")

@todo_router.get("/")
def all_todos():
    return "Not implemented"

@todo_router.post("/")
def post_todo():
    return "Not implemented"

@todo_router.put("/{key}")
def update_todo(key: int):
    return "Not implemented"

@todo_router.get("/{key}")
def delete_todo(key: int):
    return "Not implemented"

