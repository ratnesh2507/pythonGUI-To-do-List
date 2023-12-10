To-Do List Application
This is a simple To-Do List application implemented in Python using the Tkinter library. The application provides a graphical user interface (GUI) for managing tasks.

Features and Functionality
GUI Components
Window Setup:

The application window is created using Tkinter and has a title "To-do List" with dimensions 800x600 pixels.
Labels:

There are three labels:
"To-do List" at the top with a black background and white text.
"Add Task" on the left for task entry with a black background and white text.
"Tasks" on the right for displaying the list of tasks with a black background and white text.
Listbox and Text Widgets:

A Listbox widget (main_text) is used to display the list of tasks.
A Text widget (text) is used for entering new tasks.
Buttons:

"Add": Adds a new task to the list. The entered task is appended to the Listbox and saved to a file named "data.txt."
"Delete": Deletes the selected task from the Listbox and updates the "data.txt" file.
"Update": Updates the selected task in the Listbox. It opens a dialog to input the updated task.
Methods
addTask:

Reads the task from the Text widget, inserts it into the Listbox, and saves it to "data.txt."
Clears the Text widget after adding the task.
delete:

Deletes the selected task from the Listbox and updates the "data.txt" file.
Update:

Updates the selected task in the Listbox by replacing it with a new task entered through a dialog box.
File Handling:

Reads tasks from "data.txt" during the initialization of the application.
Saves tasks to "data.txt" when adding or updating tasks.
Deletes tasks from "data.txt" when removing tasks.
Usage
Run the script.
Enter a task in the "Add Task" Text widget and click the "Add" button to add it to the Listbox.
Select a task in the Listbox:
Click the "Delete" button to remove the task.
Click the "Update" button to update the task.
Note: The application reads and writes tasks to a file named "data.txt" for persistent storage.

Feel free to enhance the application by adding more features or improving the user interface.
