# To-Do List Application

## Features and Functionality

This script implements a simple To-Do List application using the Tkinter library in Python. The application allows users to add, delete, and update tasks with a graphical user interface.

### GUI Layout

- The main window is created using `Tk()` and configured with a title, dimensions, and position on the screen.
  
- The application window contains:
  - A title label displaying "To-do List".
  - Two sub-labels for "Add Task" and "Tasks".
  - A Listbox widget to display the list of tasks.
  - A Text widget for user input to add new tasks.
  
### Functionality

1. **Add Task Functionality:**
   - The `addTask` method retrieves the content from the input Text widget, inserts it into the Listbox, and writes it to a file named `data.txt`.
   - The file is opened in write mode, and the content is written. The file is then closed.
   - The input Text widget is cleared after adding the task.

2. **Delete Task Functionality:**
   - The `delete` method removes the selected task from the Listbox and updates the `data.txt` file.
   - The file is opened in read-write mode, and the lines containing the selected task are removed.
   - The selected task is deleted from the Listbox.

3. **Update Task Functionality:**
   - The `Update` method updates the selected task with a new task using a dialog box.
   - The new task is obtained using `simpledialog.askstring` and is then inserted into the Listbox.
   - The original task is deleted from the Listbox.

### Data Persistence

- The application reads from and writes to a file named `data.txt` to persist tasks across sessions.
- When the application starts, it reads tasks from the file and populates the Listbox with the existing tasks.

### Buttons

- Three buttons are provided for user interaction:
  1. **Add Button:** Adds a new task to the Listbox and updates the file.
  2. **Delete Button:** Deletes the selected task from the Listbox and updates the file.
  3. **Update Button:** Updates the selected task with a new task and updates the file.

### Main Function

- The `main` function initializes the Tkinter application and creates an instance of the `todolist` class.
- The main loop (`root.mainloop()`) keeps the GUI running and responsive.

### Running the Application

- To run the application, execute the script. Tasks will be loaded from `data.txt`, and the user can interact with the To-Do List GUI.

```python
if __name__ == "__main__":
    main()
