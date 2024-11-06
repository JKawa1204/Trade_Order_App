import tkinter as tk
from tkinter import messagebox, ttk
from models.order_system import OrderSystem

class TradeOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trade Order App")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
        self.order_system = OrderSystem()

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Order Details", padding="10 10 10 10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        input_frame.columnconfigure(1, weight=1)

        # Create entries dictionary
        self.entries = {}

        # Asset Symbol
        ttk.Label(input_frame, text="Asset Symbol:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entries['symbol'] = ttk.Entry(input_frame, width=30)
        self.entries['symbol'].grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=5)

        # Order Type
        ttk.Label(input_frame, text="Order Type (buy/sell):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entries['type'] = ttk.Entry(input_frame, width=30)
        self.entries['type'].grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=5)

        # Quantity
        ttk.Label(input_frame, text="Quantity:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entries['quantity'] = ttk.Entry(input_frame, width=30)
        self.entries['quantity'].grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=5)

        # Price
        ttk.Label(input_frame, text="Price:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entries['price'] = ttk.Entry(input_frame, width=30)
        self.entries['price'].grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=5)

        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
        button_frame.columnconfigure((0, 1), weight=1)

        # Buttons
        buttons = [
            ("Queue Order", self.queue_order),
            ("Process Next Order", self.process_order),
            ("Undo Last Order", self.undo_order),
            ("View All Orders", self.view_all_orders),
            ("View Pending Orders", self.view_pending_orders),
            ("Search Order", self.search_order)
        ]

        for i, (text, command) in enumerate(buttons):
            ttk.Button(button_frame, text=text, command=command, width=20).grid(
                row=i//2, column=i%2, padx=5, pady=5, sticky=(tk.W, tk.E)
            )

    def queue_order(self):
        try:
            # Validate inputs
            if not all(self.entries[field].get() for field in ['symbol', 'type', 'quantity', 'price']):
                self.show_warning("Input Error", "All fields must be filled")
                return

            # Validate numeric inputs
            try:
                quantity = int(self.entries['quantity'].get())
                price = float(self.entries['price'].get())
                if quantity <= 0 or price <= 0:
                    raise ValueError
            except ValueError:
                self.show_warning("Input Error", "Quantity must be a positive integer and Price must be a positive number")
                return

            order = {
                "symbol": self.entries['symbol'].get().upper(),
                "type": self.entries['type'].get().lower(),
                "quantity": quantity,
                "price": price
            }

            # Validate order type
            if order['type'] not in ['buy', 'sell']:
                self.show_warning("Input Error", "Order type must be 'buy' or 'sell'")
                return

            self.order_system.add_order(order)
            self.show_info("Order Queued", 
                          f"Order queued:\n\n"
                          f"Asset: {order['symbol']}\n"
                          f"Type: {order['type']}\n"
                          f"Quantity: {order['quantity']}\n"
                          f"Price: ${order['price']:.2f}")
            
            # Clear entries after successful queue
            for entry in self.entries.values():
                entry.delete(0, tk.END)

        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def process_order(self):
        try:
            order = self.order_system.process_order()
            if order:
                self.show_info("Order Processed", 
                              f"Order processed:\n\n"
                              f"Asset: {order['symbol']}\n"
                              f"Type: {order['type']}\n"
                              f"Quantity: {order['quantity']}\n"
                              f"Price: ${order['price']:.2f}")
            else:
                self.show_info("No Orders", "No pending orders to process.")
        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def undo_order(self):
        try:
            self.order_system.undo_order()
            self.show_info("Undo", "Last processed order has been undone.")
        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def view_all_orders(self):
        try:
            orders = self.order_system.view_all_orders()
            if orders:
                formatted_orders = "\n\n".join(
                    [f"Asset: {order['symbol']}\n"
                     f"Type: {order['type']}\n"
                     f"Quantity: {order['quantity']}\n"
                     f"Price: ${order['price']:.2f}" for order in orders]
                )
                self.show_info("All Orders", f"Processed Orders:\n\n{formatted_orders}")
            else:
                self.show_info("No Orders", "No processed orders available.")
        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def view_pending_orders(self):
        try:
            orders = self.order_system.view_pending_orders()
            if orders:
                formatted_orders = "\n\n".join(
                    [f"Asset: {order['symbol']}\n"
                     f"Type: {order['type']}\n"
                     f"Quantity: {order['quantity']}\n"
                     f"Price: ${order['price']:.2f}" for order in orders]
                )
                self.show_info("Pending Orders", f"Pending Orders:\n\n{formatted_orders}")
            else:
                                self.show_info("No Pending Orders", "No pending orders in the queue.")
        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def search_order(self):
        try:
            symbol = self.entries['symbol'].get().upper()
            order = self.order_system.search_order(symbol)
            if order:
                self.show_info("Order Found", 
                              f"Order details:\n\n"
                              f"Asset: {order['symbol']}\n"
                              f"Type: {order['type']}\n"
                              f"Quantity: {order['quantity']}\n"
                              f"Price: ${order['price']:.2f}")
            else:
                self.show_warning("Order Not Found", "No matching order found.")
        except Exception as e:
            self.show_warning("Error", f"An error occurred: {str(e)}")

    def show_info(self, title, message):
        messagebox.showinfo(title, message, parent=self.root)

    def show_warning(self, title, message):
        messagebox.showwarning(title, message, parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = TradeOrderApp(root)
    root.mainloop()