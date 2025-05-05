import os
from datetime import date

def generate_filename(client_name):
    # Sanitize client name to remove invalid characters
    client = "".join(c if c.isalnum() or c == "_" else "_" for c in client_name.strip())

    # Get today's date in YYYYMMDD format
    today = date.today().strftime("%Y%m%d")

    # Ensure the "Invoices" directory exists
    directory = "Invoices"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate the filename
    return f"{directory}/Invoice_{client}_{today}.pdf"