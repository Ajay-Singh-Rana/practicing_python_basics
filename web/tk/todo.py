import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("To Do List")

taskEntry = ""
index = 0
# defining all the funcitons
def add(event):
    global index
    a = taskEntry.get("1.0","end-1c")
    taskEntry.delete("1.0","end")
    tasksList.insert(index,a)
    index = index+1

def add_task():
    global taskEntry
    taskwindow = tk.Toplevel()
    taskwindow.geometry("200x80")
    taskEntry = tk.Text(taskwindow)
    taskEntry.pack(fill=tk.BOTH)
    taskEntry.bind("<Return>",add)

tasksList = tk.Listbox(window)
tasksList.pack()

addButton = tk.Button(window,text="Add Task",fg="Black",activebackground="Purple",command=add_task)
addButton.pack()

window.mainloop()