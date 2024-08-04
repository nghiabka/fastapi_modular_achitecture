from repositories.todo_repository import TodoRepository, TodoCreate, Todo
from typing import List, Union


class TodoService:
    def __init__(self):
        self.todo_repository = TodoRepository()

    def create_todo(self, todo: TodoCreate) -> Todo:
        return self.todo_repository.create_todo(todo)

    def get_todos(self) -> List[Todo]:
        return self.todo_repository.get_todos()

    def get_todo(self, todo_id: int) -> Union[Todo, None]:
        return self.todo_repository.get_todo(todo_id)

    def update_todo(self, todo_id: int, updated_todo: TodoCreate) -> Union[Todo, None]:
        return self.todo_repository.update_todo(todo_id, updated_todo)

    def delete_todo(self, todo_id: int) -> bool:
        return self.todo_repository.delete_todo(todo_id)