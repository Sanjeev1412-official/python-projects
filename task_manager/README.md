# Task Manager (Python)

A practical **task management** project showcasing clean Python structure, CRUD workflows, and basic engineering practices (validation, persistence, and tests). Built to be easy to run locally and easy to review.

---

## Learning outcomes

- Implementing CRUD workflows and status transitions in Python
- Persisting application state (file or DB) and handling read/write safely
- Modeling and validating data (required fields, allowed values, date parsing)
- Structuring code for testability (separating I/O from business logic)

---

## Features
- Create tasks with fields like `title`, `description`, `due_date`, `priority`, `status` *(edit to match your model)*
- List tasks
- task can mark as complete
- Delete tasks

---

## Tech stack
- **Dependencies:** *(list only the real ones; examples below)*
  - `datetime`
  - `json`
  - `argparse`

---


## CLI examples
```powershell
python task_manager.py add --title
python task_manager.py list
python task_manager.py done --id
python task_manager.py delete --id
python task_manager.py search --query
```

---
