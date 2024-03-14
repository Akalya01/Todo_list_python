import tkinter as tk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Task List
        self.task_list = tk.Listbox(root, width=50, height=15)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Delete Button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        # Enable Button
        self.enable_button = tk.Button(root, text="Enable/Disable Task", command=self.enable_task)
        self.enable_button.grid(row=2, column=1, padx=10, pady=10)

        # Big Box
        self.big_box = tk.Label(root, text="Selected Task:")
        self.big_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "enabled": True})
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            pass

    def enable_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.tasks[index]["enabled"] = not self.tasks[index]["enabled"]
            self.update_task_list()
        except IndexError:
            pass

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            if task["enabled"]:
                self.task_list.insert(tk.END, task["task"] + " (Enabled)")
            else:
                self.task_list.insert(tk.END, task["task"] + " (Disabled)")

    def show_selected_task(self):
        try:
            index = self.task_list.curselection()[0]
            task = self.tasks[index]["task"]
            self.big_box.config(text="Selected Task: " + task)
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    app.task_list.bind("<<ListboxSelect>>", lambda event: app.show_selected_task())
    root.mainloop()
