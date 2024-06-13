import tkinter as tk
from view_employees import ViewEmployeesScreen
from add_employee import AddEmployeeScreen

class EmployeeScreen(tk.Frame):
    def __init__(self, master, go_back_callback):
        super().__init__(master)
        self.master = master
        self.go_back_callback = go_back_callback
        self.pack(fill=tk.BOTH, expand=True)
        self.setup_ui()

    def setup_ui(self):
        font_style = ("Helvetica", 14, "bold")
        button_font_style = ("Helvetica", 12, "bold")

        tk.Label(self, text="Employee Management", font=font_style).pack(pady=40)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="View Employees", command=self.show_view_employees_screen, font=button_font_style, bg="blue", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=20)
        tk.Button(button_frame, text="Add Employee", command=self.show_add_employee_screen, font=button_font_style, bg="green", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=20)

        tk.Button(self, text="Back to Main Screen", command=self.go_back_callback, font=button_font_style, bg="grey", fg="white", padx=10, pady=5).pack(pady=20)

    def show_view_employees_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        ViewEmployeesScreen(self, self.setup_ui)

    def show_add_employee_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        AddEmployeeScreen(self, self.setup_ui)

if __name__ == "__main__":
    root = tk.Tk()
    EmployeeScreen(root, root.destroy).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
