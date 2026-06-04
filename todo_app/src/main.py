import sys
from engine import TodoEngine

def render_task_list(engine: TodoEngine) -> None:
    tasks = engine.get_all_tasks()
    if not tasks:
        print("\n--- Your To-Do List is currently empty ---")
        return

    print("\n================ ACTIVE TASKS ================")
    print(f"{'ID':<6}{'Status':<12}{'Task Description'}")
    print("-" * 46)
    
    for task_id, details in tasks.items():
        status_marker = "[✔] Done" if details["completed"] else "[ ] Pending"
        print(f"{task_id:<6}{status_marker:<12}{details['title']}")
    print("==============================================")

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid Input! Please provide a numerical ID sequence.", file=sys.stderr)

def main() -> None:
    # Initialize the core task engine manager
    todo = TodoEngine()
    
    while True:
        print("\n--- Menu Options ---")
        print("1. View Tasks\n2. Add Task\n3. Toggle Task Status\n4. Delete Task\n5. Exit Application")
        
        choice = input("\nSelect an operational option (1-5): ").strip()
        
        try:
            if choice == "1":
                render_task_list(todo)
                
            elif choice == "2":
                title_input = input("Enter the task description: ")
                new_id = todo.add_task(title_input)
                print(f"Success: Task added with tracking reference ID: {new_id}")
                
            elif choice == "3":
                render_task_list(todo)
                if todo.get_all_tasks():
                    target_id = get_integer_input("Enter the ID of the task to toggle: ")
                    new_status = todo.toggle_task_completion(target_id)
                    status_text = "Done" if new_status else "Pending"
                    print(f"Success: Task {target_id} updated status to {status_text}.")
                    
            elif choice == "4":
                render_task_list(todo)
                if todo.get_all_tasks():
                    target_id = get_integer_input("Enter the ID of the task to delete: ")
                    todo.delete_task(target_id)
                    print(f"Success: Task {target_id} removed from register.")
                    
            elif choice == "5":
                print("\nShutting down application state pipeline. Goodbye!")
                sys.exit(0)
                
            else:
                print("Invalid Option chosen. Please input an execution value between 1 and 5.", file=sys.stderr)
                
        except (ValueError, KeyError) as business_error:
            print(f"Operational Error: {business_error}", file=sys.stderr)
        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting gracefully.")
            sys.exit(0)

if __name__ == "__main__":
    main()