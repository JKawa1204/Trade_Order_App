# order_queue.py
from collections import deque

# order_queue.py
class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
    
    def remove_order(self):  # Changed from process_order to remove_order
        if self.queue:
            return self.queue.popleft()
        return None

    def display_orders(self):  # Added this method to match OrderSystem
        return list(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0