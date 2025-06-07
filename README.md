# Web Scraper for "Books to Scrape"

## Project Overview and Goals

This project contains a Python script designed to scrape book data from the sandbox website [books.toscrape.com](http://books.toscrape.com).

The primary goal of this project is not just to extract data, but to demonstrate a professional approach to software engineering and data pipeline development. The key objectives were:

1.  **Functional Objective**: To build a reliable scraper that navigates all pages of the catalogue and extracts four key data points for each book: title, price, star rating, and availability. The final output is a clean, structured CSV file.

2.  **Technical & Engineering Objectives**: To showcase best practices in building a data-oriented application. This includes:
    * **Modularity**: Structuring the code into small, single-responsibility functions (e.g., for fetching HTML, parsing details, handling pagination) to improve readability, testing, and maintenance.
    * **Dependency Management**: Using a dedicated virtual environment (`venv`) and a `requirements.txt` file to ensure the project is isolated and easily reproducible.
    * **Robustness**: Implementing structured logging for clear process monitoring and robust error handling for network or parsing failures.
    * **Professional Project Structure**: Organizing the project with a standard layout (`src` directory, `.gitignore`, detailed `README`) to mirror real-world development environments.

## Features

-   **Data Extraction**: Scrapes Title, Price (in Pounds), Star Rating (1-5), and Availability status.
-   **Automated Pagination**: Automatically navigates through all 50 pages of the catalogue.
-   **Structured Logging**: Provides clear, formatted logs for monitoring the scraping process.
-   **Robust Error Handling**: Manages network errors and potential parsing issues gracefully.
-   **Clean Data Output**: Exports the collected data into a well-formed CSV file named `books_data.csv`.

## Technologies Used

-   Python 3.10+
-   `requests` for handling HTTP requests.
-   `BeautifulSoup4` with the `lxml` parser for HTML parsing.
-   `pandas` for data structuring and CSV export.

## Setup and Installation

To set up and run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, you can run the scraper with the following command from the project's root directory:

```bash
python src/scraper.py
