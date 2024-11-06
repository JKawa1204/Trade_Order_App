# main.py
import tkinter as tk
from gui.trade_app import TradeOrderApp

def main():
    root = tk.Tk()
    app = TradeOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
