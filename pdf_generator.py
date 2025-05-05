from fpdf import FPDF
from utils import generate_filename

class InvoicePDF(FPDF):
    def header(self):
        # Logo (top-left corner)
        self.set_xy(10, 10)
        self.image("logo.png", x=10, y=10, w=30)

        # Invoice title (top-right corner)
        self.set_xy(150, 10)
        self.set_font("Arial", "B", 16)
        self.cell(50, 10, "INVOICE", ln=1, align="R")
        self.ln(10)  # Add vertical space after header

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def generate_pdf(invoice, totals):
    try:
        pdf = InvoicePDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Client and Invoice Info
        pdf.set_fill_color(240, 240, 240)
        pdf.set_text_color(0)
        pdf.cell(0, 10, "", ln=True)  # Spacer
        pdf.set_font("Arial", "", 11)

        client_info = [
            f"Client: {invoice.get('Client Name', 'N/A')}",
            f"Invoice Number: {invoice.get('Invoice Number', 'N/A')}",
            f"Date: {invoice.get('Date', 'N/A')}"
        ]

        for line in client_info:
            pdf.cell(100, 8, line, ln=True)

        pdf.ln(5)

        # Table Header
        pdf.set_font("Arial", "B", 11)
        pdf.set_fill_color(200, 200, 200)
        pdf.cell(80, 10, "Description", border=1, fill=True)
        pdf.cell(30, 10, "Qty", border=1, fill=True, align="C")
        pdf.cell(30, 10, "Rate", border=1, fill=True, align="C")
        pdf.cell(40, 10, "Total", border=1, fill=True, align="C")
        pdf.ln()

        # Table Rows
        pdf.set_font("Arial", "", 11)
        for item in invoice.get("Items", []):
            pdf.cell(80, 10, item.get("Description", "N/A"), border=1)
            pdf.cell(30, 10, str(item.get("Quantity", 0)), border=1, align="C")
            pdf.cell(30, 10, f"${item.get('Rate', 0):.2f}", border=1, align="C")
            pdf.cell(40, 10, f"${item.get('Total', 0):.2f}", border=1, align="C")
            pdf.ln()

        # Totals Section
        pdf.ln(3)
        pdf.set_font("Arial", "B", 11)

        def add_total_row(label, value):
            pdf.cell(140, 10, label, border=0, align="R")
            pdf.cell(40, 10, f"${value:.2f}", border=0, align="R")
            pdf.ln()

        pdf.set_text_color(0)
        add_total_row("Subtotal:", totals.get("Subtotal", 0))
        add_total_row(f"Tax ({invoice.get('Tax Rate', 0)}%):", totals.get("Tax", 0))
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(50, 50, 50)
        add_total_row("Grand Total:", totals.get("Grand Total", 0))

        # Save PDF
        filename = generate_filename(invoice.get("Client Name", "Invoice"))
        pdf.output(filename)
        print(f"PDF generated successfully: {filename}")

    except Exception as e:
        print(f"An error occurred while generating the PDF: {e}")
