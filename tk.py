import tkinter as tk

root = tk.Tk()
root.title("Basic Test")

tk.Label(root, text="Hello, Tkinter!").pack(pady=10)
tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

root.mainloop()
