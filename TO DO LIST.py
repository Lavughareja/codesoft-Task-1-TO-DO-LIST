#!/usr/bin/env python
# coding: utf-8

# # TO DO LIST

# In[1]:


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, task_index):
        try:
            del self.tasks[task_index]
            print("Task deleted successfully.")
        except IndexError:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Display Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




