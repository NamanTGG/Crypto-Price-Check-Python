import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch cryptocurrency price
def get_crypto_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    
    # Handle case where the cryptocurrency is not found
    if crypto not in data:
        return None
    
    return data[crypto]['usd']

# Function to check price and send notification if threshold is crossed
def check_price():
    crypto = crypto_var.get().lower()
    threshold = float(threshold_var.get())
    price = get_crypto_price(crypto)
    
    if price is None:
        messagebox.showerror("Error", f"Cryptocurrency '{crypto}' not found!")
        retur
    
    current_price_label.config(text=f"Current {crypto.capitalize()} price: ${price}")
    
    if price > threshold:
        messagebox.showinfo("Notification", f"{crypto.capitalize()} price has crossed ${threshold}!")

# Tkinter GUI setup
root = tk.Tk()
root.title("Crypto Price Tracker")

crypto_var = tk.StringVar(value="bitcoin")
threshold_var = tk.StringVar(value="30000")

tk.Label(root, text="Cryptocurrency:").pack()
tk.Entry(root, textvariable=crypto_var).pack()
tk.Label(root, text="Price Threshold:").pack()
tk.Entry(root, textvariable=threshold_var).pack()

tk.Button(root, text="Check Price", command=check_price).pack()
current_price_label = tk.Label(root, text="")
current_price_label.pack()

root.mainloop()
