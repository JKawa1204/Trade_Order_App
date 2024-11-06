class Stack:
    def __init__(self):
        self.stack = []
    
    def add_action(self, action):
        self.stack.append(action)
        print(f"Action added: {action}")
    
    def undo_action(self):
        if self.stack:
            action = self.stack.pop()
            print(f"Undoing action: {action}")
            return action
        else:
            print("No actions to undo.")
            return None
