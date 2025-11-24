# Personal Finance Advisor

## Overview

This project is a simple command-line Personal Finance Advisor written in Python. It helps you track spending, get basic budget insights, and view summaries by category. Designed for first-year CSE students, the whole app is just one Python file!

## Features

- Add spending transactions (date, category, amount, description)
- View all transactions in a table
- See total spending by category
- Get monthly budget advice (warns if you’re close to/exceeding your limit)
- Data saved in a basic CSV file (no external databases needed)

## Technologies/Tools Used

- Python 3.x (only standard libraries)
  - `csv` (for saving/loading data)
  - `datetime` (for dates)
- No third-party libraries required

## Steps to Install & Run the Project

1. **Install Python 3**.
2. **Download the code** (`personal_finance_advisor.py`) to a folder on your computer.
3. **Open Terminal or Command Prompt** and `cd` into that folder.
4. **Run this command:**
    ```
    python personal_finance_advisor.py
    ```
5. Follow the menu options in your terminal!

## Instructions for Testing

- Use menu Option 1 to add several transactions with different categories and amounts.
- Use Option 2 to view your transaction table.
- Use Option 3 to see if the summary-by-category works.
- Use Option 4 to set a monthly budget and test if warnings work near/exceeding the limit.
- Check that `transactions.csv` is created next to your code file, and try opening it in Excel.

## Screenshots

**Menu Example:**
