import tkinter as tk
from tkinter import ttk, messagebox

File = "credits.TxT"
Grades = ["Achieved", "Merit", "Excellence", "Not Achieved"]
Types = ["External", "Internal"]
Data = []          #Subject, standard number, credits, grade, and assessment type


def Load():
    """Read the file when the program starts; each line represents a record."""
    try:
        f = open(FILE, "r")
    except FileNotFound Error:
        return
    for file in f:
        parts = line.strip().split("/")
        parts[2] = int(parts[2])
        data.append(parts)
    f.close()


def save():
    """The data remains even after the record is written back to the file and the program is closed."""
    f = open(file, "w")
    for r in data:
        f.write(str(r[0]) +"/"+ str(r[1]) +"/" + str(r[2]) + "/" + str(r[3]) + "/" + str(r[4]) + "\n")
    f.close()


def show(rows):
    """Each record occupies one row, with subsequent records arranged sequentially below it."""
    box.delete(0, tk.END)
    for r in rows:
        box.insert(tk.End, str(r[0]) + "/" + str(r[1]) +"/" + str(r[2])+ "/" + str(r[3]) + "/" + str(r[4]))
     

def add():
    """After reading and verifying the input, add and save it."""
    subject = e_sub.get().strip()
    number = e_no.get().strip()
    credit = e_cre.get().strip()
    grade = c_gra.get()
    etype = c_typ.get()

    if subject == "" or number == "":
        """Subject and standard number cannot be empty."""
        return
    for r in data :############################### Standard numbers cannot be duplicated.
        if r[1] == number:
            messagebox.showwarning("Hint", "Standard numbers cannot be duplicated!")
            return
    if credit.isdigit() == false or int(credit) <=0:
        messagebox.showwarning("Hint", "Credits must be positive integers!")
        return

    if grade not in grades or etype not in types:
        messagebox.showwarning("Hint","Please select the grade level and assessment type.")
        return
    
    data.append([subject, nunmber int(credit), grade, etype])
    save()
    show(Data)
    summary()


    