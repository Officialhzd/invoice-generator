from datetime import datetime
import random

def get_invoice_data():
    # Generate Invoice Number
    invoice_number = generate_invoice_number()

    # Get Basic Information
    while True:
        client_name = input("Client Name: ").strip()
        if client_name and not any(char.isdigit() for char in client_name):
            break
        print("Client Name cannot be empty or contain numbers. Please try again.")

    # Automatically set the date to today's date
    date = datetime.now().strftime("%Y-%m-%d")

    # Randomly generate the tax rate between 2% and 7%
    tax_rate = random.uniform(2, 7)
    tax_rate = round(tax_rate, 2)  # Round to 2 decimal places

    # Payment terms are fixed to "Full Payment"
    payment_terms = "Full Payment"

    # Get Itemized Service Data
    items = []
    while True:
        desc = input("Service Description: ").strip()
        if not desc:
            print("Service Description cannot be empty. Please try again.")
            continue

        try:
            qty = int(input("Quantity: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")
            continue

        # Randomly generate the rate between 300 and 700
        rate = random.uniform(300, 700)
        rate = round(rate, 2)  # Round to 2 decimal places

        items.append({"Description": desc, "Quantity": qty, "Rate": rate})

        more = input("Would you like to add another item? (y/n): ").strip().lower()
        if more != "y":
            break

    if not items:
        raise ValueError("At least one item must be added to the invoice.")

    # Return the invoice data after validation
    return {
        "Client Name": client_name,
        "Invoice Number": invoice_number,
        "Date": date,
        "Tax Rate": tax_rate,
        "Payment Terms": payment_terms,
        "Items": items
    }


def generate_invoice_number():
    """
    Generate a unique invoice number based on the current timestamp.
    """
    now = datetime.now()
    return f"INV-{now.strftime('%Y%m%d%H%M%S')}"


def validate_date(date):
    """
    Validate the date format (YYYY-MM-DD).
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
