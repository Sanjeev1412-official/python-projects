import json
import argparse
import os
from datetime import datetime

TASKFILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKFILE):
        return []
    
    #if file is empty
    if os.path.getsize(TASKFILE) == 0:
        return []
    
    with open(TASKFILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASKFILE,'w') as file:
        json.dump(tasks,file,indent=4)
        
def add_task(title):
    
    tasks = load_tasks()
    
    task = {
        "id" : len(tasks) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{title}" added successfully ✅.')
    
def list_tasks():
    
    tasks = load_tasks()
    
    for task in tasks:
        status = "✔️" if task["done"] else "❌"
        print(f'{task["id"]}. {task["title"]} [{status}])')
        
        
def delete_task(task_id):
    
    tasks = load_tasks()
    
    tasks = [t for t in tasks if t["id"] != task_id]
    
    save_tasks(tasks)
    print(f'Task with ID {task_id} deleted successfully 🗑️.')
    

def mark_task_done(task_id):
    
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f'Task with ID {task_id} marked as done ✅.')
            break
    else:
        print(f'Task with ID {task_id} not found ❌.')
        return
    
    save_tasks(tasks)
    

def search_tasks(keyword):
    
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t["title"].lower()]
    
    if not results:
        print(f'No tasks found containing "{keyword}" 🔍.')
        return
    
    for task in results:
        print(f"[{task['id']}] {task['title']}")

def main():
    parser = argparse.ArgumentParser(description="Command-Line Task Manager")

    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", type=str)

    # list command
    subparsers.add_parser("list")

    # delete command
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    # done command
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)

    # search command
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("keyword", type=str)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)

    elif args.command == "list":
        list_tasks()

    elif args.command == "delete":
        delete_task(args.id)

    elif args.command == "done":
        mark_task_done(args.id)

    elif args.command == "search":
        search_tasks(args.keyword)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()