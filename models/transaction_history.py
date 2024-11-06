# transaction_history.py
class TransactionNode:
    def __init__(self, trade):
        self.trade = trade
        self.next = None
        self.prev = None

class TransactionHistory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_transaction(self, trade):
        new_node = TransactionNode(trade)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_transactions(self):
        trades = []
        current = self.head
        while current:
            trades.append(current.trade)
            current = current.next
        return trades

    def remove_last_transaction(self):
        if self.tail:
            removed_trade = self.tail.trade
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return removed_trade
        return None
