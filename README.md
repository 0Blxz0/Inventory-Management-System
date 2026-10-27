# Inventory Management System

A Python command-line application that helps a small retail business track **products, suppliers and orders**, with every record stored in plain text files.

Built as a 6-person team project at Sunway University (Apr – Aug 2025). I coordinated the team and integrated each member's functions into one working program.

**Stack:** Python 3 · file I/O · exception handling · Jupyter Notebook

## Features

| Menu option | What it does |
|---|---|
| 1. Add Product | Adds a product with a unique 5-digit ID, name, description, stock and price |
| 2. Update Product Details | Edits an existing product's details |
| 3. Add Supplier | Adds a supplier with a unique 4-digit ID, contact number and the product they supply |
| 4. Place Order | Records an order, checks there is enough stock and deducts it |
| 5. View Inventory | Lists every product with its stock and price |
| 6. View Supplier Info | Lists every supplier and their contact details |
| 7. Generate Report | Prints a 3-section report (see below) |

### The report

Option 7 combines all 3 data files into one report:

1. **Low stock items:** products with fewer than 5 units, each shown with its supplier's contact number for reordering
2. **Product sales:** units sold and total revenue per product
3. **Orders:** every order with its product, quantity and date

```text
               LOW STOCK ITEMS (Stock < 5)
=========================================================
Product ID   Product Name                 Remaining Stock
---------------------------------------------------------
10002        KEYBOARD                              3
   --> Supplier contact: 03-1234 5678
10004        HDMI CABLE                            2
   --> Supplier contact: 012-345 6789

                   PRODUCT SALES REPORT
=========================================================
Product ID   Product Name      Total Sold   Total Revenue
---------------------------------------------------------
10001        USB MOUSE                  5   $      199.50
10003        MONITOR                    2   $    1,198.00
```

## Input validation

All 18 user-input points are validated, and 19 `try/except` blocks keep invalid entries from crashing the program:

- Product IDs must be 5 digits and supplier IDs 4 digits, and duplicates are rejected
- Names and descriptions cannot be empty
- Stock, price and order quantities must be valid, non-negative numbers
- Orders cannot exceed the stock available
- A missing data file is created automatically instead of raising an error

## Run it

You need Python 3.8 or newer. There are no third-party packages.

```bash
python inventory_management.py
```

Or open `Programming_Assignment.ipynb` in Jupyter (for example through Anaconda) and run the cell.

### Try it with sample data

Copy the 3 files from `sample-data/` into the project folder, run the program and choose **7. Generate Report**.

## Data files

| File | One line per record |
|---|---|
| `products.txt` | `product_id,name,description,stock,price` |
| `suppliers.txt` | `supplier_id,name,contact,product_id` |
| `orders.txt` | `order_id,product_id,quantity,order_date` |

## Project structure

```text
inventory_management.py        # the program, runnable from the command line
Programming_Assignment.ipynb   # the same program as submitted (Jupyter Notebook)
sample-data/                   # example products, suppliers and orders
```

## What I would improve next

- Generate order IDs from the number of existing orders, not products, so they can never repeat
- Move the data from text files to SQLite
- Add automated tests for the validation rules
