import os
from tkinter import *
from tkinter.filedialog import askopenfile
from log_display import log_analyser,create_search_window


window = Tk()
window.configure(bg='light blue')

window.title('Log Analysis Tool')
window.geometry("1300x650+10+20")
logo = PhotoImage(file="logo.gif")
lbl_logo = Label(window, bg="light blue", image=logo)
lbl_logo.place(x=1000, y=10)

lbl = Label(window, text="Log Analysis Tool ", fg='black', bg="light blue", font=("Times new roman", 24))
lbl.place(x=400, y=20)

lbl = Label(window, text="Failure Log file : ", fg='Black', bg="light blue", font=("Times new roman", 16,))
lbl.place(x=300, y=200)

entry = Entry(window, bg="white", width=60, bd=10)
entry.place(x=300, y=250)


def open_file(entry):
    path = askopenfile(mode="r", filetypes=[('All Flies', '*.txt')])
    global abs_path
    abs_path=path.name
    if abs_path is not None:
        entry.insert(0,abs_path)
    return abs_path

def create_popup(err_text):
    warn_window=Tk()
    warn_window.minsize(300,100)

    warn_window.title('Error')
    warn_window.geometry("500x100+500+400")

    Label(warn_window, text= err_text, fg='Red', font=("Times new roman", 16,)).pack()
    aply_btn=Button(warn_window, text="OK", bd=8, fg='Red', command=lambda:[warn_window.destroy(), entry.delete(0,len(abs_path))])
    aply_btn.place(x=200,y=45)

def check_file_size(abs_path):
    if os.path.getsize(abs_path) == 0:
        get_msg = "empty"
        create_popup("File is Empty, Unable to parse the file")
    elif os.path.getsize(abs_path) > 524288000:
        get_msg = "too large"
        create_popup("File is Too Large, Unable to parse the file")
    else:
        get_msg = "ready to parse"
        log_analyser(abs_path)
    print(get_msg)

btn = Button(window, text="choose file", fg='blue', bd=8, command=lambda :open_file(entry))
btn.place(x=750, y=250)

lbl = Label(window, text="<Min-Max size of log file>", fg='Black',bg="light blue", font=("Times new roman", 16))
lbl.place(x=300, y=300)

btn1 = Button(window, text="ANALISE", fg='blue', bd=8, command=lambda : check_file_size(abs_path))#command=lambda : log_analyser(abs_path))

btn1.place(x=300, y=350)

btn1 = Button(window, text="SEARCH", fg='blue', bd=8,command=lambda : create_search_window(entry,abs_path))
btn1.place(x=500, y=350)

window.mainloop()
