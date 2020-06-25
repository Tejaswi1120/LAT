from tkinter import *
import re, os, Error_Analysis


def create_output_window(abs_path: object):
    top = Toplevel()
    top.title('Log Analysis Tool')
    top.configure(bg='light blue')

    top.geometry("1250x600")
    logo = PhotoImage(file="logo.gif")
    lbl_logo = Label(top, bg="light blue", image=logo)
    lbl_logo.place(x=1000, y=10)

    lbl = Label(top, text="Failure Log file : ", fg='Black', bg="light blue", font=("Times new roman", 16))
    lbl.place(x=150, y=80)

    lbl = Label(top, text=abs_path, fg='Black', bg="light blue", font=("Times new roman", 16,))
    lbl.place(x=300, y=80)

    listbox = Listbox(top, height=15,
                      width=100,
                      bg="light grey",
                      activestyle='dotbox',
                      font="Helvetica",
                      fg="black",
                      )

    btn = Button(top, text="Back", fg='Green', bd=5, command=top.destroy)
    btn.place(x=500, y=500)

    listbox.place(x=100, y=150)
   # frame = Frame(top)
    #frame.place(x=10, y=5, width=100, height=100)
    #framea = Frame(master=frame)
    #framea.place(x=10, y=5, width=100, height=100)

    scrollbary = Scrollbar(top, orient="vertical")
    scrollbarx = Scrollbar(top, orient="horizontal")
    scrollbary.pack(side="right", fill="y")
    scrollbarx.pack(side="bottom", fill="x")
    top.filename = "output_file.html"
    text1 = open(top.filename).read()
    l1 = text1.split("\n")
    for i in l1:
        listbox.insert(END, i)
    listbox.config(yscrollcommand=scrollbary.set)
    listbox.config(xscrollcommand=scrollbarx.set)
    scrollbary.config(command=listbox.yview)
    scrollbarx.config(command=listbox.xview)


def log_analyser(abs_path):
    with open("output_file.html", "w") as f:
        var = Error_Analysis.Searching_errors_in_logs(abs_path)
        for line in var:
            f.write('%s' % line)

    create_output_window(abs_path)

def create_search_window(entry, abs_path):
    top = Toplevel()
    top.title('Log Analysis Tool')
    top.configure(bg='light blue')

    top.geometry("1250x600")
    logo = PhotoImage(file="./logo.gif")
    lbl_logo = Label(top, bg="light blue", image=logo)
    lbl_logo.place(x=1000, y=10)

    lbl = Label(top, text="LOG ANALYSIS TOOL ", fg='black', bg="light blue", font=("Times new roman", 18))
    lbl.place(x=200, y=100)

    lbl = Label(top, text="Failure Log file : ", fg='Black', bg="light blue", font=("Times new roman", 16,))
    lbl.place(x=300, y=200)

    #   def search_with_str(entry):
    entry = Entry(top, bg="white", width=60, bd=10)
    entry.place(x=300, y=250)

    btn = Button(top, text="search", fg='blue', bd=8,
                 command=lambda: [Error_Analysis.search_str_in_logs(abs_path, entry), create_output_window(abs_path)])
    btn.place(x=650, y=250)

    btn = Button(top, text="Back", fg='Green', bd=5, command=top.destroy)
    btn.place(x=400, y=350)


    #frame.pack()
    top. mainloop()
    # lbl = Label(top, text="Failure Log file : ", fg='Black', bg="light blue", font=("Times new roman", 16))
    # lbl.place(x=150, y=80)
    # lbl = Label(top, text=abs_path, fg='search', bg="light blue", font=("Times new roman", 16,))
    # lbl.place(x=300, y=80)
    # top.mainloop()
