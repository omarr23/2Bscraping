Here’s a detailed README file for your project:

---

# Laptop Web Scraper

This project is a web scraper designed to extract information about laptops from the **2B.com.eg** website. It collects details such as the product name, price, and other metadata and provides options to save the scraped data in a CSV file or a MariaDB database.

---

## Features

- Scrapes product details (name, price, old price, discount percentage).
- Supports pagination to scrape all available products.
- Saves the extracted data as a CSV file.
- Optionally saves the data to a MariaDB database.

---

## Technologies Used

- **Python 3.x**: Main programming language.
- **Requests**: To make HTTP requests and fetch web pages.
- **BeautifulSoup**: For parsing HTML content.
- **Pandas**: To manage and save data as CSV files.
- **MariaDB**: To save data in a structured database.
- **time**: To handle delays between requests.

---

## Setup Instructions

### Prerequisites
- Python 3.x installed on your machine.
- Install the required Python packages:
  ```bash
  pip install requests beautifulsoup4 pandas mariadb
  ```
- MariaDB server installed and configured.

---

### Usage Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/laptop-web-scraper.git
   cd laptop-web-scraper
   ```

2. **Run the Scraper**  
   Execute the script to scrape laptop data:
   ```bash
   python scraper.py
   ```
   The script will:
   - Scrape product data from all pages.
   - Save the data to `laptops.csv` by default.

3. **Save to Database (Optional)**  
   To save the data into a MariaDB database:
   - Ensure MariaDB is running.
   - Update the database credentials in the script (`save_to_database` function).
   - Uncomment the `save_to_database(products)` line in the `if __name__ == "__main__":` block.

---

### Configuration

- **Target URL**: The base URL for scraping is predefined in the script:
  ```python
  base_url = "https://2b.com.eg/ar/computers/laptops.html?_=1734290666421&p={}&product_list_limit=24"
  ```
- **Headers**: The script uses a user-agent to mimic a browser:
  ```python
  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
  }
  ```

---

## Output

1. **CSV File**  
   A `laptops.csv` file containing all scraped products, structured as:
   ```
   Product Name, Price, Old Price, Discount Percentage
   ```

2. **Database Table (Optional)**  
   A `laptop_products` table in the specified MariaDB database with the following columns:
   - `id`: Auto-incremented primary key.
   - `product_name`: Name of the laptop.
   - `price`: Current price.
   - `old_price`: Old price (if available).
   - `discount_percentage`: Discount percentage (placeholder).

---

## Error Handling

- Handles HTTP errors gracefully using `requests.RequestException`.
- Stops scraping if no products are found on a page.
- Provides informative messages for database connection or query errors.

---

## Future Enhancements

- Add support for scraping other categories.
- Improve error handling and retry logic for failed requests.
- Implement multi-threading for faster scraping.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features.

---

## Author

- **Your Name**  
  GitHub: [omarr23](https://github.com/omarr23)  
  Email:omar.salah2015.os@gmail.com 

--- 

This README provides clear usage and setup instructions, making it easy for others to understand and use your project.
