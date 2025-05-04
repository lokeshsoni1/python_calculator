import tkinter

# Create main window
w = tkinter.Tk()
w.title("LOKESH SONI CALCULATOR")
w.geometry("500x500")
w.configure(bg="lightblue")

# Functions for operations
def add():
    n1 = float(e.get())
    n2 = float(f.get())
    result = n1 + n2
    g.delete(0, tkinter.END)
    g.insert(0, str(result))

def subtract():
    n1 = float(e.get())
    n2 = float(f.get())
    result = n1 - n2
    g.delete(0, tkinter.END)
    g.insert(0, str(result))

def multiply():
    n1 = float(e.get())
    n2 = float(f.get())
    result = n1 * n2
    g.delete(0, tkinter.END)
    g.insert(0, str(result))

def divide():
    n1 = float(e.get())
    n2 = float(f.get())
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Cannot divide by 0"
    g.delete(0, tkinter.END)
    g.insert(0, str(result))

# Function to insert number into focused entry
def insert_number(n):
    current = w.focus_get()
    if isinstance(current, tkinter.Entry):
        current.insert(tkinter.END, str(n))

# Labels and Entries
title = tkinter.Label(w, text="Name: Lokesh Soni", bg="yellow")
title.place(x=170, y=10)

roll = tkinter.Label(w, text="Roll No: 27102", bg="yellow")
roll.place(x=180, y=35)

L = tkinter.Label(w, text="First No.", bg="orange")
L.place(x=300, y=70)
e = tkinter.Entry(w)
e.place(x=150, y=70)

M = tkinter.Label(w, text="Second No.", bg="orange")
M.place(x=300, y=110)
f = tkinter.Entry(w)
f.place(x=150, y=110)

N = tkinter.Label(w, text="Result", bg="orange")
N.place(x=300, y=150)
g = tkinter.Entry(w)
g.place(x=150, y=150)

# Number Buttons (1–5 in first line)
x = 80
y = 200
for i in range(1, 6):
    btn = tkinter.Button(w, text=str(i), width=5, height=1, command=lambda i=i: insert_number(i))
    btn.place(x=x, y=y)
    x += 50

# Number Buttons (6–0 in second line)
x = 80
y = 240
for i in range(6, 11):  # includes 0 as i=10
    btn = tkinter.Button(w, text=str(i % 10), width=5, height=1, command=lambda i=i: insert_number(i % 10))
    btn.place(x=x, y=y)
    x += 50

# Operation Buttons
add_btn = tkinter.Button(w, text="+", width=5, height=1, command=add)
add_btn.place(x=100, y=290)

sub_btn = tkinter.Button(w, text="-", width=5, height=1, command=subtract)
sub_btn.place(x=160, y=290)

mul_btn = tkinter.Button(w, text="*", width=5, height=1, command=multiply)
mul_btn.place(x=220, y=290)

div_btn = tkinter.Button(w, text="/", width=5, height=1, command=divide)
div_btn.place(x=280, y=290)

# Start loop
w.mainloop()
