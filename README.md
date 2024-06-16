# Crypto-Price-Check-Python
Made by Naman Gupta
What We'll Learn:

Fetching Data from the Internet: We'll use the requests module to get real-time cryptocurrency prices from the CoinGecko API.

Building a Simple User Interface: We'll use tkinter to create a graphical user interface where we can enter the cryptocurrency name and price threshold.

Handling User Input and Errors: We'll add basic error handling to manage incorrect inputs or missing data.
Step-by-Step Guide:

Setting Up:

First, we need to import the necessary modules. We'll use requests to fetch data from the internet and tkinter to create our GUI.

Fetching Cryptocurrency Prices:

We'll write a function called get_crypto_price() that takes the name of a cryptocurrency as input and returns its current price in USD using the CoinGecko API.

UI--

Building the User Interface: 
Using tkinter, we'll create a simple window where users can enter the cryptocurrency name and the price threshold.
We'll add a button that, when clicked, will check the current price of the entered cryptocurrency and compare it to the threshold.

Checking Prices and Alerting the User:
We'll write a function called check_price() that gets the current price, compares it with the threshold, and displays a popup message if the price is above the threshold.
