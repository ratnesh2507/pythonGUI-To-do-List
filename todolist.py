from tkinter import *
from tkinter import ttk
from tkinter import simpledialog

class todolist:
    def __init__(self , root):
        self.root = root
        self.root.title('To-do List')
        self.root.geometry('800x600+375+100')
        
        self.label = Label(self.root, text='To-do List',
              font='CalistoMT, 25 bold', width=10, height=2, bd=5, bg='black', fg='white')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
              font='ariel, 18 bold', width=10, bd=5, bg='black', fg='white')
        self.label2.place(x=50, y=90)

        self.label3 = Label(self.root, text='Tasks',
              font='ariel, 18 bold', width=10, bd=5, bg='black', fg='white')
        self.label3.place(x=450, y=90)

        self.main_text = Listbox(self.root, height=12, bd=5, width=32, font="ariel, 20 italic bold",
                                  bg='deep sky blue')
        self.main_text.place(x=280, y=140)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=30,y=150)
        
        def addTask():
            content = self.text.get(1.0,END)
            self.main_text.insert(END, content)
            with open('data.txt','w') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            look =self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_file = f.readlines()
                f.seek(0)
                for line in new_file:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        def Update():
            update_ = self.main_text.curselection()
            look = self.main_text.get(update_)
            new_task = simpledialog.askstring("Update Task","Update Task:",initialvalue=look)
            self.main_text.insert(END, new_task)
            self.main_text.delete(update_)
        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                             width=10,bd=5,bg='PeachPuff3', fg='green', command=addTask)
        self.button.place(x=40,y=220)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                             width=10,bd=5,bg='PeachPuff3', fg='red', command=delete)
        self.button2.place(x=40,y=300)

        self.button3 = Button(self.root, text="Update", font='sarif, 20 bold italic',
                             width=10,bd=5,bg='PeachPuff3', fg='yellow', command=Update)
        self.button3.place(x=40,y=380)
def main():
    root = Tk()
    ui = todolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()
