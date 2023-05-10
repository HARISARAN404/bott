import requests
from bs4 import BeautifulSoup
import telegram
import time

# Telegram bot token and chat ID
bot_token = 'your_bot_token_here'
chat_id = 'your_chat_id_here'

# Function to scrape product price
def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find('span', {'class': 'price'}).get_text()
    return price

# Function to send message via Telegram bot
def send_telegram_message(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Main function to track product prices
def track_prices():
    # List of product URLs to track
    product_urls = ['https://www.example.com/product1',
                    'https://www.example.com/product2',
                    'https://www.example.com/product3']
    # Loop through product URLs
    for url in product_urls:
        # Get product price
        price = get_product_price(url)
        # Send price via Telegram bot
        message = f'The price of {url} is {price}'
        send_telegram_message(message)
    # Wait for 1 hour before checking again
    time.sleep(3600)

# Call main function
while True:
    track_prices()
