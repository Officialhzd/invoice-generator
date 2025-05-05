def calculate(invoice):
    # Validate input
    items = invoice.get("Items", [])
    if not isinstance(items, list):
        raise ValueError("Invalid invoice format: 'Items' must be a list.")

    tax_rate = invoice.get("Tax Rate", 0)
    if not isinstance(tax_rate, (int, float)):
        raise ValueError("Invalid invoice format: 'Tax Rate' must be a number.")

    # Calculate totals
    subtotal = 0
    for item in items:
        quantity = item.get("Quantity", 0)
        rate = item.get("Rate", 0)
        if not isinstance(quantity, (int, float)) or not isinstance(rate, (int, float)):
            raise ValueError("Invalid item format: 'Quantity' and 'Rate' must be numbers.")
        
        total = quantity * rate
        item["Total"] = round(total, 2)  # Add total to the item and round to 2 decimal places
        subtotal += total

    tax = round(subtotal * (tax_rate / 100), 2)
    grand_total = round(subtotal + tax, 2)

    # Return calculated totals
    return {
        "Subtotal": round(subtotal, 2),
        "Tax": tax,
        "Grand Total": grand_total
    }