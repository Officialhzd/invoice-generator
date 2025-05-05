import logging
import json
from input_handler import get_invoice_data
from calculator import calculate
from pdf_generator import generate_pdf

# Configure logging
logging.basicConfig(
    filename="invoice_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def save_to_json(data, filename="invoices.json"):
    """
    Save the given invoice data to a single JSON file dynamically.
    """
    try:
        # Load existing data if the file exists
        try:
            with open(filename, "r") as json_file:
                all_invoices = json.load(json_file)
        except FileNotFoundError:
            all_invoices = []  # Start with an empty list if the file doesn't exist

        # Append the new invoice data
        all_invoices.append(data)

        # Save the updated data back to the file
        with open(filename, "w") as json_file:
            json.dump(all_invoices, json_file, indent=4)

        logging.info(f"Invoice data added to {filename} successfully.")
    except Exception as e:
        logging.error(f"Failed to save data to {filename}: {e}")
        print(f"An error occurred while saving data to {filename}: {e}")

def main():
    try:
        # Step 1: Get invoice data
        logging.info("Starting invoice generation process.")
        invoice_data = get_invoice_data()
        logging.info("Invoice data collected successfully.")

        # Step 2: Calculate totals
        totals = calculate(invoice_data)
        logging.info("Invoice totals calculated successfully.")

        # Step 3: Save data to JSON
        save_to_json({"Invoice Data": invoice_data, "Totals": totals})

        # Step 4: Generate PDF
        generate_pdf(invoice_data, totals)
        logging.info("Invoice PDF generated successfully.")

        print("Invoice generated successfully!")
        logging.info("Invoice generation process completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()