
from typing import Dict, Any

class TodoEngine:
    def __init__(self) -> None:
        self._tasks: Dict[int, Dict[str, Any]] = {}
        self._id_counter: int = 1

    def add_task(self, title: str) -> int:
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Task title cannot be empty.")
            
        task_id = self._id_counter
        
        self._tasks[task_id] = {
            "title": clean_title,
            "completed": False 
        }
        
        self._id_counter += 1
        return task_id

    def get_all_tasks(self) -> Dict[int, Dict[str, Any]]:
        return self._tasks

    def toggle_task_completion(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            raise KeyError(f"Task ID {task_id} does not exist.")
        current_state = self._tasks[task_id]["completed"]
        self._tasks[task_id]["completed"] = not current_state
        return self._tasks[task_id]["completed"]

    def delete_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"Task ID {task_id} does not exist.")
        del self._tasks[task_id]