
import json
import os
from datetime import datetime

FILE = "billing_data.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)

    return {
        "products": {},
        "customers": {},
        "sales": []
    }


data = load_data()


def save_data():
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_product():
    pid = input("Enter Product ID: ")

    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    data["products"][pid] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    save_data()
    print("Product added successfully!")

def display_products():
    print("\n------ PRODUCT LIST ------")

    if not data["products"]:
        print("No products available.")
        return

    for pid, p in data["products"].items():
        print(
            f"ID: {pid} | Name: {p['name']} | "
            f"Price: Rs.{p['price']:.2f} | Stock: {p['stock']}"
        )

def search_product():
    pid = input("Enter Product ID: ")

    if pid in data["products"]:
        p = data["products"][pid]
        print("\nProduct Found!")
        print("Name:", p["name"])
        print("Price:", p["price"])
        print("Stock:", p["stock"])
    else:
        print("Product not found.")

def add_customer():
    cid = input("Enter Customer ID: ")

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")

    data["customers"][cid] = {
        "name": name,
        "phone": phone
    }

    save_data()
    print("Customer added successfully!")

def generate_bill():
    cid = input("Enter Customer ID: ")

    if cid not in data["customers"]:
        print("Customer not found. Please add customer first.")
        return

    customer = data["customers"][cid]
    items = []
    subtotal = 0

    print("\n------ BILLING ------")
    print("Customer:", customer["name"])
    print("Phone:", customer["phone"])

    while True:
        pid = input("\nEnter Product ID (or 0 to finish): ")

        if pid == "0":
            break

        if pid not in data["products"]:
            print("Product not found!")
            continue

        product = data["products"][pid]

        print("Product:", product["name"])
        print("Price:", product["price"])
        print("Available Stock:", product["stock"])

        try:
            qty = int(input("Enter Quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if qty <= 0:
            print("Quantity must be greater than zero.")
            continue

        if qty > product["stock"]:
            print("Insufficient stock!")
            continue

        amount = product["price"] * qty
        subtotal += amount

        items.append({
            "product": product["name"],
            "quantity": qty,
            "price": product["price"],
            "amount": amount
        })

        product["stock"] -= qty

        print("Product added to bill.")

    if not items:
        print("No products selected.")
        return

    discount = float(input("\nEnter Discount (%): "))

    if discount < 0 or discount > 100:
        print("Invalid discount.")
        for item in items:
            for p in data["products"].values():
                if p["name"] == item["product"]:
                    p["stock"] += item["quantity"]
                    break
        return

    discount_amount = subtotal * discount / 100
    taxable_amount = subtotal - discount_amount

    tax = taxable_amount * 0.05
    total = taxable_amount + tax

    print("\nSelect Payment Method")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    payment_choice = input("Enter Choice: ")

    methods = {
        "1": "Cash",
        "2": "UPI",
        "3": "Card"
    }

    if payment_choice not in methods:
        print("Invalid payment method.")
        for item in items:
            for p in data["products"].values():
                if p["name"] == item["product"]:
                    p["stock"] += item["quantity"]
                    break
        return

    payment = methods[payment_choice]

    invoice_id = "INV" + str(len(data["sales"]) + 1)
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("\n================================")
    print("          BILLING SYSTEM")
    print("================================")
    print("Invoice ID:", invoice_id)
    print("Date:", date)
    print("Customer:", customer["name"])
    print("--------------------------------")
    print("Product       Qty      Amount")
    print("--------------------------------")

    for item in items:
        print(
            f"{item['product']:<14}"
            f"{item['quantity']:<9}"
            f"Rs.{item['amount']:.2f}"
        )

    print("--------------------------------")
    print(f"Subtotal:          Rs.{subtotal:.2f}")
    print(f"Discount:          Rs.{discount_amount:.2f}")
    print(f"Tax (5%):          Rs.{tax:.2f}")
    print(f"Final Amount:      Rs.{total:.2f}")
    print("Payment Method:", payment)
    print("================================")
    print("       THANK YOU!")
    print("================================")

    transaction = {
        "invoice_id": invoice_id,
        "date": date,
        "customer": customer["name"],
        "items": items,
        "subtotal": subtotal,
        "discount": discount_amount,
        "tax": tax,
        "total": total,
        "payment": payment
    }

    data["sales"].append(transaction)

    save_data()
    print("\nBill generated and saved successfully!")

def sales_history():
    print("\n------ SALES HISTORY ------")

    if not data["sales"]:
        print("No sales records available.")
        return

    for sale in data["sales"]:
        print("\nInvoice ID:", sale["invoice_id"])
        print("Date:", sale["date"])
        print("Customer:", sale["customer"])
        print("Total: Rs.", sale["total"])
        print("Payment:", sale["payment"])

def sales_report():
    print("\n------ SALES REPORT ------")
    print("1. Daily Report")
    print("2. Weekly Report")
    print("3. Monthly Report")
    print("4. All Sales")

    choice = input("Enter Choice: ")

    today = datetime.now().date()
    total = 0
    count = 0

    for sale in data["sales"]:
        sale_date = datetime.strptime(
            sale["date"], "%d-%m-%Y %H:%M:%S"
        ).date()

        if choice == "1" and sale_date == today:
            total += sale["total"]
            count += 1

        elif choice == "2" and (today - sale_date).days < 7:
            total += sale["total"]
            count += 1

        elif choice == "3" and (
            sale_date.month == today.month
            and sale_date.year == today.year
        ):
            total += sale["total"]
            count += 1

        elif choice == "4":
            total += sale["total"]
            count += 1

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return

    print("\nTotal Transactions:", count)
    print(f"Total Sales: Rs.{total:.2f}")

def main():
    while True:
        print("\n========== BILLING SYSTEM ==========")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Add Customer")
        print("5. Generate Bill")
        print("6. View Sales History")
        print("7. Sales Report")
        print("8. Exit")

        choice = input("\nEnter Choice: ")

        try:
            if choice == "1":
                add_product()

            elif choice == "2":
                display_products()

            elif choice == "3":
                search_product()

            elif choice == "4":
                add_customer()

            elif choice == "5":
                generate_bill()

            elif choice == "6":
                sales_history()

            elif choice == "7":
                sales_report()

            elif choice == "8":
                save_data()
                print("Thank you for using Billing System!")
                break

            else:
                print("Invalid choice! Try again.")

        except (ValueError, KeyError):
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
