import tkinter as tk
from employee import EmployeeScreen
from frontend import CustomerScreen

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Screen")
        self.geometry("400x300")

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.show_initial_screen()

    def show_initial_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        font_style = ("Helvetica", 14, "bold")
        button_font_style = ("Helvetica", 12, "bold")

        tk.Label(self.main_frame, text="Select an Option", font=font_style).pack(pady=40)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Employees", command=self.show_employee_screen, font=button_font_style, bg="green", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=20)
        tk.Button(button_frame, text="Customers", command=self.show_customer_screen, font=button_font_style, bg="blue", fg="white", padx=20, pady=10).pack(side=tk.LEFT, padx=20)

    def show_employee_screen(self):
        self.title("Employee Screen")
        self.geometry("500x400")  # Set window size
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        EmployeeScreen(self.main_frame, self.show_initial_screen)

    def show_customer_screen(self):
        self.title("Pickup Code Details")
        self.geometry("400x300")  # Set window size
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        CustomerScreen(self.main_frame, self.show_initial_screen)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
