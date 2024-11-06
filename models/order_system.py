# order_system.py
from .order_queue import OrderQueue
from .stack import Stack
from .transaction_history import TransactionHistory
from .tree import Tree
from .sorting import sort_trades

class OrderSystem:
    def __init__(self):
        self.queue = OrderQueue()
        self.stack = Stack()
        self.history = TransactionHistory()
        self.tree = Tree()
        self.root = None

    def add_order(self, order):
        # Add the order to the queue instead of processing immediately
        self.queue.add_order(order)
        print(f"Order queued: {order}")

    def process_order(self):
        # Process the next order in the queue
        if self.queue.is_empty():
            print("No orders to process.")
            return None
        order = self.queue.remove_order()
        
        # Add to transaction history and tree, then allow undo
        self.root = self.tree.insert(self.root, order['symbol'], order)
        self.stack.add_action(order)
        self.history.add_transaction(order)
        print(f"Order processed: {order}")
        return order

    def undo_order(self):
        # Undo the last processed order (not the one in the queue)
        last_order = self.stack.undo_action()
        if last_order:
            self.history.remove_last_transaction()
            print(f"Undone order: {last_order}")

    def view_all_orders(self):
        # Get all processed orders and sort them
        transactions = self.history.display_transactions()
        sorted_trades = sort_trades(transactions, key=lambda x: x['price'])
        return sorted_trades

    def view_pending_orders(self):
        # View all orders currently in the queue (unprocessed)
        return self.queue.display_orders()

    def search_order(self, symbol):
        # Search for an order in the tree
        return self.tree.search(self.root, symbol)
