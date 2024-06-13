import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

class ViewEmployeesScreen(tk.Frame):
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

        tk.Label(self, text="Employees", font=label_font_style).pack(pady=10)
        
        employee_frame = tk.Frame(self)
        employee_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        self.employee_listbox = tk.Listbox(employee_frame, font=font_style, width=80, height=15)
        self.employee_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        employee_scrollbar = tk.Scrollbar(employee_frame, orient="vertical")
        employee_scrollbar.config(command=self.employee_listbox.yview)
        employee_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.employee_listbox.config(yscrollcommand=employee_scrollbar.set)

        self.load_employees()

        tk.Button(self, text="Back to Employee Screen", command=self.go_back_callback, font=button_font_style, bg="grey", fg="white", padx=10, pady=5).pack(pady=20)

    def load_employees(self):
        try:
            client = MongoClient('mongodb+srv://packstation:pack@cluster0.f6o7lcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            db = client['PackstationDatabase']
            employees = db['employees']  # Assuming you have an employees collection

            self.employee_listbox.delete(0, tk.END)
            for employee in employees.find():
                self.employee_listbox.insert(tk.END, f"{employee['name']} - {employee['email']} - {employee['phone']} - {employee['department']}")

            print("Employees loaded successfully.")
        except Exception as e:
            print(f"Error loading employees: {e}")
            messagebox.showerror("Error", "An error occurred while loading employees.")

if __name__ == "__main__":
    root = tk.Tk()
    ViewEmployeesScreen(root, root.destroy).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
