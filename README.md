# 🛒 Automated E-Commerce Web Scraper

###  Project Overview
A robust Python-based tool designed to extract, clean, and structure product data from e-commerce platforms automatically. This script demonstrates high-performance web scraping techniques, including user-agent rotation, error handling, and automated CSV export using **Pandas**.

**Goal:** Transform unstructured web data into actionable business intelligence (Excel/CSV).

---

###  Tech Stack & Tools
* **Language:** Python 3.9+
* **Core Libraries:**
    * `BeautifulSoup4`: For precise HTML parsing and data extraction.
    * `Requests`: For managing HTTP protocols and sessions.
    * `Pandas`: For data manipulation and CSV/Excel export.
* **Key Concepts:** Object-Oriented Logic, Exception Handling, Data Cleaning.

---

###  Key Features
* **📊 Automatic Data Structuring:** Extracts Title, Price, Stock Status, and Star Rating instantly.
* **🧹 Data Cleaning Pipeline:** Automatically removes currency symbols and formats text for analysis.
* **🛡️ Anti-Blocking Mechanism:** Includes ethical delays (`time.sleep`) and User-Agent headers to mimic human behavior.
* **📉 Error Resilience:** Continues running even if specific items or pages fail to load.
* **💾 Instant Export:** Generates a ready-to-use `libros_extraidos.csv` file.

---

###  How to Run This Project
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NSVargas/ecommerce-web-scraper.git](https://github.com/NSVargas/ecommerce-web-scraper.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install requests beautifulsoup4 pandas
    ```
3.  **Run the script:**
    ```bash
    python scraper.py
    ```
4.  **Check results:** Open the generated `.csv` file in Excel or Google Sheets.

---

###  Contact
**Need a custom scraping solution or automation script?**
I am available for freelance work. Feel free to reach out to automate your data entry tasks.

* **Engineer:** Nahuel Sebastián (NSVargas)
* **Services:** Python Scripting, Web Scraping, Process Automation.