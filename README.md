# Python Billing Management System

## Project Overview

The **Python Billing Management System** is a menu-driven application developed using Python. It helps manage products, customer information, billing transactions, and sales reports.

The system allows users to add and search products, manage customer details, generate bills, calculate discounts and taxes, and maintain sales records. It uses JSON file handling to store data permanently.

## Features

- **Add Product:** Add products with Product ID, name, price, and stock quantity.
- **Display Products:** View all available products and their details.
- **Search Product:** Search for a product using its Product ID.
- **Add Customer:** Store customer ID, name, and phone number.
- **Generate Bill:** Create bills by selecting products and quantities.
- **Discount Calculation:** Apply a discount to the subtotal.
- **Tax Calculation:** Automatically calculate 5% tax.
- **Payment Methods:** Supports Cash, UPI, and Card.
- **Sales History:** View previously generated invoices.
- **Sales Reports:** Generate daily, weekly, monthly, and all-time sales reports.
- **Data Storage:** Save product, customer, and sales information in a JSON file.

## Technologies Used

- Python 3
- JSON
- File handling
- Built-in Python modules:
  - `json`
  - `os`
  - `datetime`

## Project Structure

```text
Python-Billing-System/
├── billing_system.py
├── billing_data.json
├── README.md
└── .gitignore
```

**Note:** `billing_data.json` is created automatically when the program runs. Do not upload real customer information or private sales records to a public repository.

## How to Run the Project

### 1. Install Python

Install Python 3 on your computer.

### 2. Clone the Repository

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd Python-Billing-System
```

### 4. Run the Program

```bash
python billing_system.py
```

On some Windows installations, you may need to use:

```bash
py billing_system.py
```

## Main Menu

```text
========== BILLING SYSTEM ==========
1. Add Product
2. Display Products
3. Search Product
4. Add Customer
5. Generate Bill
6. View Sales History
7. Sales Report
8. Exit

Enter Choice:
```

## Billing Calculation

The program uses the following formulas:

- **Subtotal:** Sum of all product amounts.
- **Discount Amount:** Subtotal × Discount Percentage / 100.
- **Taxable Amount:** Subtotal − Discount Amount.
- **Tax:** Taxable Amount × 5 / 100.
- **Final Amount:** Taxable Amount + Tax.

## Data Storage

The application stores information in `billing_data.json`, including:

- Product details and stock quantities
- Customer details
- Sales transactions
- Invoice details

The JSON file allows records to remain available after the program is closed and reopened.

## Learning Outcomes

This project demonstrates the use of:

- Python functions
- Lists and dictionaries
- Conditional statements and loops
- File handling and JSON
- Exception handling
- Basic billing and sales calculations

## Future Improvements

- Graphical User Interface (GUI)
- Database integration using SQLite or MySQL
- PDF invoice generation
- Improved inventory management
- User authentication

## Author

**Susmita Mandal**

## Purpose

This project was developed for educational purposes.
