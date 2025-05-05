# 🧾 Invoice Generator

A simple Python-based invoice generator that collects service details, calculates totals, exports a clean PDF invoice, and saves the data to a JSON file.

## 🚀 Features

- Dynamic service input
- Total and tax calculation
- PDF invoice generation using `fpdf`
- Invoice data saved in JSON format
- Modular and beginner-friendly codebase

## 🛠 Tech Stack

- Python 3
- [fpdf](https://pyfpdf.github.io/fpdf2/)
- Built-in `json` module

## 📦 Project Structure

invoice_generator/
│
├── main.py # Runs the app
├── input_handler.py # Handles user input
├── calculator.py # Computes totals
├── pdf_generator.py # Creates PDF invoices
├── utils.py # Helper functions
└── invoices/ # Generated files


## ✅ How to Run

1. Clone the repo  
2. Install dependencies:
pip install fpdf
3. Run the app:
python main.py


## 📍 Output

- PDF Invoice saved in `/invoices`
- Invoice data stored in `invoices.json`

## 📈 Future Improvements

- GUI (Tkinter or PyQt)
- Email invoice feature
- Currency formatting
- Database support

---

> Built for freelancers, students, and small businesses who need fast and simple billing automation
