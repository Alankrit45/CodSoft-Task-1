import os
import pickle

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'Done' if self.completed else 'Not Done'}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\nYour Tasks:")
        print("-" * 40)
        print(f"{'No.':<4} {'Status':<10} {'Description'}")
        print("-" * 40)

        for idx, task in enumerate(self.tasks, 1):
            status = "Done" if task.completed else "Not Done"
            print(f"{idx:<4} {status:<10} {task.description}")
        print("-" * 40)

    def mark_task_completed(self, index):
        if self._valid_index(index):
            self.tasks[index].mark_completed()
            print("Task marked as completed.")

    def delete_task(self, index):
        if self._valid_index(index):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.description}' deleted.")

    def save_tasks(self, filename="tasks.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.tasks, f)
        print("Tasks saved.")

    def load_tasks(self, filename="tasks.pkl"):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.tasks = pickle.load(f)
            print("Tasks loaded.")
        else:
            print("No saved tasks found.")

    def _valid_index(self, index):
        if 0 <= index < len(self.tasks):
            return True
        print("Invalid task number.")
        return False

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "3":
            todo_list.view_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "4":
            todo_list.view_tasks()
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "5":
            todo_list.save_tasks()
        elif choice == "6":
            todo_list.load_tasks()
        elif choice == "7":
            todo_list.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
