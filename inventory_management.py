import textwrap
import os
from datetime import datetime

#add products
def add_product():
    # Checks whether Product ID is 5 digits
    try:
        check_product_id = input("Enter product ID (5 digits): ").strip()
        if not (check_product_id.isdigit() and len(check_product_id) == 5):
            print(f'\n---------------------------------------------------\n')
            print("Product ID must be a 5-digit number!")
            print(f'\n---------------------------------------------------\n')
            return

        # Check whether product ID already exists
        try:
            with open("products.txt", "r") as file:
                for line in file:
                    product_id = line.strip().split(',')[0]
                    if check_product_id == product_id:
                        print(f'\n---------------------------------------------------\n')
                        print("Product ID has already been used! Please try another product ID.")
                        print(f'\n---------------------------------------------------\n')
                        return

        # Checks whether products.txt exists, create if false.
        except FileNotFoundError:
            with open("products.txt", "w"):
                pass

        # Capitalise product names
        name = input("Enter product name: ").strip().upper()
        if not name:
            print(f'\n---------------------------------------------------\n')
            print("Product name cannot be empty! Please enter your choice again.")
            print(f'\n---------------------------------------------------\n')
            return

        # Input product description
        description = input("Enter product description: ").strip()
        if not description:
            print(f'\n---------------------------------------------------\n')
            print("Product description cannot be empty!")
            print(f'\n---------------------------------------------------\n')
            return

        # Input product stock
        try:
            stock = int(input("Enter product stock: "))
            if stock < 0:
                print(f'\n---------------------------------------------------\n')
                print("Product stock cannot be negative!")
                print(f'\n---------------------------------------------------\n')
                return
        except ValueError:
            print(f'\n---------------------------------------------------\n')
            print("Invalid product stock! Please enter a valid number.")
            print(f'\n---------------------------------------------------\n')
            return

        # Input product price
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print(f'\n---------------------------------------------------\n')
                print("Product price must be a positive number!")
                print(f'\n---------------------------------------------------\n')
                return
        except ValueError:
            print(f'\n---------------------------------------------------\n')
            print("Invalid product price! Please enter a valid number.")
            print(f'\n---------------------------------------------------\n')
            return

        # Append product details to the file
        with open("products.txt", "a") as file:
            file.write(f"{check_product_id},{name},{description},{stock},{price}\n")
            print(f'\n---------------------------------------------------\n')
            print("You have successfully added a product.")
            print(f'\n---------------------------------------------------\n')

    except ValueError:
        print(f'\n---------------------------------------------------\n')
        print("Invalid Input!\nPlease enter your choice again.")
        print(f'\n---------------------------------------------------\n')




#update product
def update_product():
    try:
      # Check if products file exists
        try:
            with open("products.txt", "r") as file:
                pass  # File exists, so nothing to do here
        except FileNotFoundError:
            # Create new file if it does not exist
            with open("products.txt", "w") as file:
                pass  # Create an empty file
            print(f'\n---------------------------------------------------\n')
            print("Products file not found! A new file has been created.")
            print(f'\n---------------------------------------------------\n')

        # Read products from the file
        with open("products.txt", "r") as f:
            products = [line.strip().split(",") for line in f.readlines()]

        # Check if the product list is empty
        if not products:
            print(f'\n---------------------------------------------------\n')
            print("No products available in inventory!")
            print(f'\n---------------------------------------------------\n')
            return

        # Display available products
        available_products()

        # Input product ID to update
        check_product_id = input("Enter a product ID to update (5 digits): ").strip()

        if not (check_product_id.isdigit() and len(check_product_id) == 5):
            print(f'\n---------------------------------------------------\n')
            print("Product ID must be a 5-digit number!")
            print(f'\n---------------------------------------------------\n')
            return

        found_product = False
        updated_product_list = []

        # Iterate through the product list to find the product to update
        for line in products:
          product_id, name, description, stock, price = line

          # Check product id
          if check_product_id == product_id:
              found_product = True
              print(f'\n---------------------------------------------------\n')
              print(f"Updating product: ID: {product_id}, Name: {name}, Stock: {stock}, Price: ${price}")
              print(f'\n---------------------------------------------------\n')

              # Input new product name
              new_name = input("Enter new product name (leave blank to keep current): ").strip().upper()
              if new_name:
                  name = new_name

              # Input new product description
              new_description = input("Enter new product description (leave blank to keep current): ").strip()
              if new_description:
                  description = new_description

              # Input new stock quantity
              try:
                  new_stock = input("Enter new stock quantity (leave blank to keep current): ")
                  if new_stock:
                      new_stock = int(new_stock)
                      if new_stock >= 0:
                          stock = new_stock
              except ValueError:
                  print(f'\n---------------------------------------------------\n')
                  print("Invalid stock! Please enter a valid number.")
                  print(f'\n---------------------------------------------------\n')
                  return

              # Input new product price
              try:
                  new_price = input("Enter new price (leave blank to keep current): ")
                  if new_price:
                      new_price = float(new_price)
                      if new_price > 0:
                          price = new_price
              except ValueError:
                  print(f'\n---------------------------------------------------\n')
                  print("Invalid price! Please enter a valid number.")
                  print(f'\n---------------------------------------------------\n')
                  return

              updated_product_list.append(f"{product_id},{name},{description},{stock},{price}\n")
          else:
              updated_product_list.append(",".join(line) + "\n")

        # If product ID not found, notify the user
        if not found_product:
            print(f'\n---------------------------------------------------\n')
            print("Product ID not found!")
            print(f'\n---------------------------------------------------\n')
            return

        # Write the updated product list back to the file
        with open("products.txt", "w") as file:
            file.writelines(updated_product_list)

        print(f'\n---------------------------------------------------\n')
        print("Product updated successfully.")
        print(f'\n---------------------------------------------------\n')

    except Exception as e:
        print(f'\n---------------------------------------------------\n')
        print(f"An error occurred: {e}")
        print(f'\n---------------------------------------------------\n')




# Add Supplier
def add_supplier():
    try:
        # Check if suppliers file exists, if not, create it
        try:
              with open("suppliers.txt", "r") as file:
                  pass
        except FileNotFoundError:
              try:
                  with open("suppliers.txt", "w") as file:
                      pass
              except Exception as e:
                  # Error handling for file creation
                  print(f'\n---------------------------------------------------\n')
                  print(f"Error creating suppliers file: {e}")
                  print(f'\n---------------------------------------------------\n')
                  return

              # Inform the user that a new file was created
              print(f'\n---------------------------------------------------\n')
              print("Suppliers file not found. A new file has been created.")
              print(f'\n---------------------------------------------------\n')

        # Get and validate supplier ID
        check_supplier_id = input("Enter supplier ID (4 digits): ").strip()
        if not (check_supplier_id.isdigit() and len(check_supplier_id) == 4):
            print(f'\n---------------------------------------------------\n')
            print("Supplier ID must be a 4-digit number!")
            print(f'\n---------------------------------------------------\n')
            return

        # Check if the supplier ID already exists in the file
        with open("suppliers.txt", "r") as file:
            for line in file:
                supplier_id = line.strip().split(',')[0]
                if str(check_supplier_id) == supplier_id:
                    print(f'\n---------------------------------------------------\n')
                    print("Supplier ID already exists!")
                    print(f'\n---------------------------------------------------\n')
                    return

        # Get supplier details
        name = input("Enter supplier name: ").strip().upper()
        if not name:
            print(f'\n---------------------------------------------------\n')
            print("Supplier name can only contain letters!")
            print(f'\n---------------------------------------------------\n')
            return

        contact = input("Enter supplier contact details (10-digit number): ").strip()

        # Check contact details
        if not (contact.isdigit() and len(contact) == 10):
            print(f'\n---------------------------------------------------\n')
            print("Supplier contact details must be a 10-digit number!")
            print(f'\n---------------------------------------------------\n')
            return

        # Attempt to read product file to get available products
        try:
            with open("products.txt", "r") as file:
                products = [line.strip().split(",") for line in file.readlines()]
        except FileNotFoundError:
            print(f'\n---------------------------------------------------\n')
            print("Products file not found! Please add some products first.")
            print(f'\n---------------------------------------------------\n')
            return

        # Check if there are any products available in the inventory
        if not products:
            print(f'\n---------------------------------------------------\n')
            print("No products available in the inventory!")
            print(f'\n---------------------------------------------------\n')
            return

        # Display available products
        print("\nAvailable Products:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}")

        # Get the product ID the supplier will provide
        supplied_product = input("\nEnter the product ID this supplier will supply: ").strip()

        # Check if the product ID is valid
        if not any(supplied_product == product[0] for product in products):
            print(f'\n---------------------------------------------------\n')
            print(f"Invalid product ID: {supplied_product}! Please enter a valid product ID.")
            print(f'\n---------------------------------------------------\n')
            return

        # Add the supplier to the suppliers file
        with open("suppliers.txt", "a") as f:
            f.write(f"{check_supplier_id},{name},{contact},{supplied_product}\n")
            print(f'\n---------------------------------------------------\n')
            print("You have successfully added a supplier with the supplied product.")
            print(f'\n---------------------------------------------------\n')

    except ValueError:
      print(f'\n---------------------------------------------------\n')
      print("Invalid input! Please enter a valid supplier ID (numeric).")
      print(f'\n---------------------------------------------------\n')




# Place Order
def place_order():
    try:
        # Check if products file exists
        try:
            with open("products.txt", "r") as file:
                pass  # File exists, so nothing to do here
        except FileNotFoundError:
            # Create new file if it does not exist
            with open("products.txt", "w") as file:
                pass  # Create an empty file
            print(f'\n---------------------------------------------------\n')
            print("Products file not found. A new file has been created.")
            print(f'\n---------------------------------------------------\n')

        # Read product data from the file
        with open("products.txt", "r") as f:
            products = [line.strip().split(",") for line in f.readlines()]

        # Check if there are any products available
        if not products:
            print(f'\n---------------------------------------------------\n')
            print("No products available in inventory.")
            print(f'\n---------------------------------------------------\n')
            return

        # Display available products (you need to define available_products() if not already)
        available_products()

        # Get product ID to order
        product_id = input("\nEnter Product ID to order: ").strip()
        selected_product = None  # Default value if no match is found

        # Find the product matching the entered product ID
        for product in products:
            if product[0].strip() == product_id.strip():
                selected_product = product
                break

        # If no product was found, notify the user
        if not selected_product:
            print(f'\n---------------------------------------------------\n')
            print(f"Error: Product ID does not exist.\nPlease enter a 5-digit number.")
            print(f'\n---------------------------------------------------\n')
            return

        # Get and validate quantity
        try:
            quantity = int(input(f"Enter quantity to order (Available: {selected_product[3]}): "))
            if quantity < 1:
                print(f'\n---------------------------------------------------\n')
                print('Please enter a value larger than 1.')
                print(f'\n---------------------------------------------------\n')
                return

        except ValueError:
            print(f'\n---------------------------------------------------\n')
            print("Error: Please enter an integer")
            print(f'\n---------------------------------------------------\n')
            return

        # Check if there is enough stock
        current_stock = int(selected_product[3])
        if quantity > current_stock:
            print(f'\n---------------------------------------------------\n')
            print(f"Error: Insufficient stock available.\nAvailable Stock: {current_stock}")
            print(f'\n---------------------------------------------------\n')
            return

        # Generate Order ID
        order_id = f"ORD{len(products) + 1}"
        order_date = datetime.now().strftime("%Y-%m-%d")

        # Record the order in orders.txt
        with open("orders.txt", "a") as f:
            f.write(f"{order_id},{product_id},{quantity},{order_date}\n")

        # Update product stock
        selected_product[3] = str(current_stock - quantity)
        with open("products.txt", "w") as f:
            for product in products:
                f.write(",".join(product) + "\n")

        # Confirmation message
        print(f'\n---------------------------------------------------\n')
        print(f"Order placed successfully! Order ID: {order_id}")
        print(f'\n---------------------------------------------------\n')

    except Exception as e:
        print(f'\n---------------------------------------------------\n')
        print(f"An error occurred: {e}")
        print(f'\n---------------------------------------------------\n')




# View Inventory
def view_inventory():
    width = 100
    print('\n')
    print('=' * width)
    print('VIEWING INVENTORY'.center(width))
    print('=' * width)
    print(f"{'Product ID':<15} {'Product Name':<20} {'Product Description':<30}"
          f"{'Remaining Stocks':<19} {'Product Price':<14}")
    print('-' * width)

    try:
        with open('products.txt', 'r') as f:
            file_contents = f.readlines()

        for lines in file_contents:
            product_data = [item.strip() for item in lines.strip().split(',')]

            # Wrap the product description if it is too long
            wrapped_description = textwrap.wrap(product_data[2], width=25)  # Adjust width as needed

            # Print the first line of the product description
            print(f"{product_data[0]:<15} {product_data[1]:<20} {wrapped_description[0]:<30} "
                  f"{product_data[3]:>15} {'$':>4} {product_data[4]:>11}")

            # Print additional lines of the product description, if any
            for line in wrapped_description[1:]:
                print(f"{'':<15} {'':<20} {line:<30}")

            print('-' * width)

    except IOError as e:
        print(e)
        print(f'\n' + '-' * width + '\n')
        print('Cannot read from file'.center(width))
        print(f'\n' + '-' * width + '\n')




# Display Available Products
def available_products():
    width = 100
    print('\n')
    print('=' * width)
    print('AVAILABLE PRODUCTS'.center(width))
    print('=' * width)
    print(f"{'Product ID':<15} {'Product Name':<20} {'Product Description':<30}"
          f"{'Remaining Stocks':<19} {'Product Price':<14}")
    print('-' * width)

    try:
        with open('products.txt', 'r') as f:
            file_contents = f.readlines()

        for lines in file_contents:
            product_data = [item.strip() for item in lines.strip().split(',')]

            # Wrap the product description if it is too long
            wrapped_description = textwrap.wrap(product_data[2], width=25)  # Adjust width as needed

            # Print the first line of the product description
            print(f"{product_data[0]:<15} {product_data[1]:<20} {wrapped_description[0]:<30} "
                  f"{product_data[3]:>15} {'$':>4} {product_data[4]:>11}")

            # Print additional lines of the product description, if any
            for line in wrapped_description[1:]:
                print(f"{'':<15} {'':<20} {line:<30}")

            print('-' * width)

    except IOError as e:
        print(e)
        print(f'\n' + '-' * width + '\n')
        print('Cannot read from file'.center(width))
        print(f'\n' + '-' * width + '\n')


# View Supplier Info
def view_supplier():
    width = 84  # Define total width for centering the title
    print('=' * width)
    print('VIEWING SUPPLIER INFO'.center(width))  # Center the title in the given width
    print('=' * width)

    # Display the header for supplier information
    print(f"{'Supplier ID':<15} {'Supplier Name':<25} {'Contact Details':<25} {'Supplied Product':<20}")
    print('-' * width)

    try:
        # Open the suppliers file and read the data
        with open('suppliers.txt', 'r') as f:
            file_contents = f.readlines()

        # Loop through each supplier and print their details
        for lines in file_contents:
            supplier_data = [item.strip() for item in lines.strip().split(',')]  # Strip spaces and split by comma
            print(f"{supplier_data[0]:<15} {supplier_data[1]:<25} {supplier_data[2]:<25} {supplier_data[3]:<15}")

        print(f'-' * width + '\n')
    except IOError as e:
        # Handle error if the file cannot be read
        print(e)
        print(f'\n' + '-'*width + '\n')
        print('Cannot read from file'.center(width))
        print(f'\n' + '-'*width + '\n')




# Generate reports
def generate_report():
    try:
        # Load product and order data from their respective files
        with open("products.txt", "r") as file:
            products = [line.strip().split(",") for line in file.readlines()]

        with open("orders.txt", "r") as file:
            orders = [line.strip().split(",") for line in file.readlines()]

        with open("suppliers.txt", "r") as file:
            suppliers = {}
            for line in file.readlines():
                parts = line.strip().split(",")
                product_id = parts[3]  # Product ID from suppliers.txt
                supplier_contact = parts[2]

                # Add the supplier contact to the list for this product_id
                if product_id not in suppliers:
                    suppliers[product_id] = []
                suppliers[product_id].append(supplier_contact)

        # Low stock report (products with stock < 5)
        # Low stock report (products with stock < 5)
        print("\n" + "="*57)
        print("LOW STOCK ITEMS (Stock < 5)".center(57))  # Center the title for the report
        print("="*57)
        print(f"{'Product ID'.ljust(12)} {'Product Name'.ljust(20)} {'Remaining Stock'.rjust(23)}")
        print("-" * 57)
        for product in products:
            if int(product[3].strip()) < 5:  # Check stock for each product
                print(f"{product[0].ljust(12)} {product[1].ljust(20)} {product[3].strip().rjust(18)}")

                # Match the product ID with suppliers and get the contacts
                product_id = product[0].strip()
                supplier_contacts = suppliers.get(product_id, ["Supplier contact not available"])

                # Display all supplier contacts for the product
                for contact in supplier_contacts:
                    print(f"   --> Supplier contact: {contact}")

        # Sales report (showing total sold and revenue)
        print("\n" + "="*57)
        print("PRODUCT SALES REPORT".center(57))  # Center the title for the report
        print("="*57)
        print(f"{'Product ID'.ljust(12)} {'Product Name'.ljust(15)} {'Total Sold'.rjust(12)} {'Total Revenue'.rjust(15)}")
        print("-" * 57)

        # Initialize dictionaries to store sales and revenue data
        sales = {product[0].strip(): 0 for product in products}
        revenue = {product[0].strip(): 0.0 for product in products}

        # Loop through the orders and update sales and revenue
        for order in orders:
            order_product_id = order[1].strip()  # Get the product ID from the order
            quantity = int(order[2].strip())
            for product in products:
                product_id = product[0].strip()
                price = float(product[4].strip().replace("$", ""))  # Remove the dollar sign from price
                if product_id == order_product_id:  # Match order to the correct product
                    sales[product_id] += quantity
                    revenue[product_id] += quantity * price

        # Print the sales report with total sales and revenue for each product
        for product in products:
            product_id = product[0].strip()
            product_name = product[1].strip()
            total_sold = sales[product_id]
            total_revenue = revenue[product_id]
            # Print product ID, name, total sold, and total revenue (formatted correctly)
            print(f"{product_id:<12} {product_name:<20} {total_sold:>7} {'$':>3.5} {total_revenue:>11,.2f}")

        # Display order details (including order ID, product ID, quantity, and order date)
        print("\n" + "="*57)
        print("ORDERS REPORT".center(57))  # Center the title for the report
        print("="*57)
        print(f"{'Order ID'.ljust(12)} {'Product ID'.ljust(12)} {'Quantity'.rjust(15)} {'Order Date'.rjust(15)}")
        print("-" * 57)
        for order in orders:
            order_id = order[0].strip()
            product_id = order[1].strip()
            quantity = order[2].strip()
            order_date = order[3].strip()  # Assuming the date is stored in the 4th column
            print(f"{order_id:<12} {product_id:<12} {quantity:>15} {order_date:>15}")

        print("="*57)
        print(f'\n')

    except FileNotFoundError as e:
        # Handle file not found error
        print(f'\n---------------------------------------------------\n')
        print(f"Error: {e}")
        print(f'\n---------------------------------------------------\n')
    except Exception as e:
        # Handle any other exceptions that occur
        print(f'\n---------------------------------------------------\n')
        print(f"An error occurred: {e}")
        print(f'\n---------------------------------------------------\n')



# Function to allow the user to repeat an action if desired
def repeat_function(function_to_run, repeat_question):
    while True:
        function_to_run()  # Run the function
        repeat = input(repeat_question).strip().lower()  # Ask user if they want to repeat
        if repeat == "no":
            print("\nReturning to the main menu...")
            break  # Exit the loop and return to main menu
        elif repeat != "yes":
            print(f'\n---------------------------------------------------\n')
            print("Invalid input. Returning to the main menu...")
            print(f'\n---------------------------------------------------\n')
            break  # Return to main menu on invalid input




# Main function to run the menu
def main():
    while True:
        print("\n======== MAIN MENU ========")
        # Display options for the user to choose from
        print("[1] Add Product")
        print("[2] Update Product Details")
        print("[3] Add Supplier")
        print("[4] Place Order")
        print("[5] View Inventory")
        print("[6] View Supplier Info")
        print("[7] Generate Report")
        print("[8] Exit")
        print("===========================\n")

        # Get user input for menu selection
        choice = input("Enter your choice: ").strip()

        # Based on the user's choice, call the respective function
        if choice == "1":
            repeat_function(add_product, "Do you want to add another product? (yes/no): ")
        elif choice == "2":
            repeat_function(update_product, "Do you want to update another product? (yes/no): ")
        elif choice == "3":
            repeat_function(add_supplier, "Do you want to add another supplier? (yes/no): ")
        elif choice == "4":
            repeat_function(place_order, "Do you want to place another order? (yes/no): ")
        elif choice == "5":
            view_inventory()
        elif choice == "6":
            view_supplier()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print(f'\n---------------------------------------------------\n')
            print("Exiting program. Have a great day!")
            print(f'\n---------------------------------------------------\n')
            break  # Exit the program
        else:
            print("Invalid choice! Please try again.")  # Handle invalid input




# Start the program by calling the main function
if __name__ == "__main__":
    main()