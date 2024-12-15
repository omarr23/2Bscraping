import requests
from bs4 import BeautifulSoup
import pandas as pd
import mariadb
import time

# Base URL template for laptops
base_url = "https://2b.com.eg/ar/computers/laptops.html?_=1734290666421&p={}&product_list_limit=24"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

def get_product_details(product):
    name = product.find('a', {'class': 'product-item-link'}).get_text(strip=True)
    price = product.find('span', {'class': 'price'}).get_text(strip=True)
    old_price = product.find('span', {'class': 'old-price'})
    old_price = old_price.get_text(strip=True) if old_price else None

    discount = None  
    return {
        'Product Name': name,
        'Price': price,
        'Old Price': old_price,
        'Discount Percentage': discount
    }


def scrape_page(page_num):
    url = base_url.format(page_num)
    print(f"Scraping page {page_num}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching page {page_num}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    products = soup.find_all('li', {'class': 'item product product-item'})

    if not products:
        print(f"No products found on page {page_num}. Stopping.")
        return []

    return [get_product_details(product) for product in products]

# Main function to scrape all pages
def scrape_all_pages():
    all_products = []
    page = 1

    while True:
        products = scrape_page(page)
        if not products:
            break
        all_products.extend(products)
        page += 1
        time.sleep(1) 

    return all_products

def save_to_csv(data, filename="laptops.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}.")

def save_to_database(data):
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3306,
            database="processors"
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS laptop_products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255),
                price VARCHAR(50),
                old_price VARCHAR(50),
                discount_percentage VARCHAR(50)
            )
        """)

        for item in data:
            cursor.execute("""
                INSERT INTO laptop_products (product_name, price, old_price, discount_percentage)
                VALUES (?, ?, ?, ?)
            """, (item['Product Name'], item['Price'], item['Old Price'], item['Discount Percentage']))

        conn.commit()
        print("Data saved to the database.")
    except mariadb.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

# Main entry point
if __name__ == "__main__":
    products = scrape_all_pages()
    if products:
        save_to_csv(products)
        # Uncomment below to save to database
        save_to_database(products)
    else:
        print("No products scraped.")
