import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

class AddEmployeeScreen(tk.Frame):
    def __init__(self, master, go_back_callback):
        super().__init__(master)
        self.master = master
        self.go_back_callback = go_back_callback
        self.pack(fill=tk.BOTH, expand=True)
        self.setup_ui()

    def setup_ui(self):
        font_style = ("Helvetica", 12)
        label_font_style = ("Helvetica", 14, "bold")
        button_font_style = ("Helvetica", 12, "bold")

        tk.Label(self, text="Add New Employee", font=label_font_style).pack(pady=10)

        tk.Label(self, text="Name", font=font_style).pack(pady=5)
        self.name_entry = tk.Entry(self, font=font_style, width=40)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Email", font=font_style).pack(pady=5)
        self.email_entry = tk.Entry(self, font=font_style, width=40)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Phone", font=font_style).pack(pady=5)
        self.phone_entry = tk.Entry(self, font=font_style, width=40)
        self.phone_entry.pack(pady=5)

        tk.Label(self, text="Department", font=font_style).pack(pady=5)
        self.department_entry = tk.Entry(self, font=font_style, width=40)
        self.department_entry.pack(pady=5)

        tk.Button(self, text="Add Employee", command=self.add_employee, font=button_font_style, bg="green", fg="white", padx=10, pady=5).pack(pady=20)

        tk.Button(self, text="Back to Employee Screen", command=self.go_back_callback, font=button_font_style, bg="grey", fg="white", padx=10, pady=5).pack(pady=20)

    def add_employee(self):
        new_employee = {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'phone': self.phone_entry.get(),
            'department': self.department_entry.get()
        }

        try:
            client = MongoClient('mongodb+srv://packstation:pack@cluster0.f6o7lcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            db = client['PackstationDatabase']
            employees = db['employees']  # Assuming you have an employees collection
            employees.insert_one(new_employee)
            messagebox.showinfo("Success", "Employee added successfully.")
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.department_entry.delete(0, tk.END)
        except Exception as e:
            print(f"Error adding employee: {e}")
            messagebox.showerror("Error", "An error occurred while adding the employee.")

if __name__ == "__main__":
    root = tk.Tk()
    AddEmployeeScreen(root, root.destroy).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
