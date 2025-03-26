import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
label.pack()
window.mainloop()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
name = entry.get()
name 
'Real Python'