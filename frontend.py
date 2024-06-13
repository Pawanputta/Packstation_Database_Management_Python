import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox

class CustomerScreen:
    def __init__(self, master, go_back_callback):
        self.master = master
        self.go_back_callback = go_back_callback
        self.setup_ui()

    def setup_ui(self):
        font_style = ("Helvetica", 12)
        label_font_style = ("Helvetica", 14, "bold")
        button_font_style = ("Helvetica", 12, "bold")

        tk.Label(self.master, text="Enter Pickup Code:", font=label_font_style).pack(pady=20)
        self.entry = tk.Entry(self.master, font=font_style, width=30)
        self.entry.pack(pady=10)

        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Get Details", command=self.get_details, font=button_font_style, bg="blue", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Reset", command=self.reset_fields, font=button_font_style, bg="red", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Back to Main Screen", command=self.go_back_callback, font=button_font_style, bg="grey", fg="white", padx=10, pady=5).pack(side=tk.LEFT, padx=10)

    def get_details(self):
        pickup_code = self.entry.get()
        print(f"Pickup code entered: {pickup_code}")

        try:
            client = MongoClient('mongodb+srv://packstation:pack@cluster0.f6o7lcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            db = client['PackstationDatabase']
            notifications = db['notifications-csv']
            customers = db['customers-csv']
            compartments = db['compartments-csv']
            print("Connected to MongoDB Atlas.")

            notification = notifications.find_one({'pickup_code': pickup_code})
            print(f"Notification found: {notification}")

            if not notification:
                print("Notification not found")
                messagebox.showerror("Error", "Pickup code not found.")
                return

            customer_id = notification['customer_id']
            compartment_id = notification['compartment_id']

            print(f"Querying customers with customer_id: {customer_id}")
            customer = customers.find_one({'ID': customer_id})
            print(f"Customer found: {customer}")

            print(f"Querying compartments with compartment_id: {compartment_id}")
            compartment = compartments.find_one({'ID': compartment_id})
            print(f"Compartment found: {compartment}")

            if customer and compartment:
                details = (
                    f"Customer ID: {customer.get('ID')}\n"
                    f"Name: {customer.get('Name')}\n"
                    f"Email: {customer.get('Email')}\n"
                    f"Phone Number: {customer.get('Phone')}\n"
                    f"Compartment ID: {compartment.get('ID')}\n"
                    f"Compartment Size: {compartment.get('compartment_size')}\n"
                    f"Lock Code: {compartment.get('lock_code')}\n"
                    f"Notification Type: {notification.get('notification_type')}\n"
                    f"Instructions: {notification.get('instructions')}"
                )
                print(f"Details to show: {details}")
                messagebox.showinfo("Details", details)
            else:
                print("Customer or Compartment details not found")
                messagebox.showerror("Error", "Details not found.")
        except Exception as e:
            print(f"Error retrieving details: {e}")
            messagebox.showerror("Error", "An error occurred while retrieving details.")

    def reset_fields(self):
        self.entry.delete(0, tk.END)
        self.entry.focus()
