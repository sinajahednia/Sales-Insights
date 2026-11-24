# Sales Analysis Project

A Python-based data analysis project focused on exploring retail sales data and generating business insights using Pandas.

## Project Overview

This project analyzes an online retail dataset to identify sales performance, customer purchasing patterns, top-performing products, and monthly sales trends.

## Key Features

- Data analysis using Python and Pandas
- Revenue calculation and sales summaries
- Identification of cancelled transactions
- Top-selling countries and products
- Monthly sales performance analysis
- Excel sales report included in the reports folder

## Technologies Used

- Python
- Pandas
- NumPy
- Excel
- Git & GitHub

## Project Structure

```text
Sales-Analysis/
│
├── data/
│   └── online_retail.csv
│
├── reports/
│   ├── sales_report.xlsx
│
├── src/
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Results

- Gross Sales: £10,644,560.42
- Valid Orders: 20,728
- Average Order Value: £513.54
- Top Sales Country: United Kingdom


## How to Run

1. Clone this repository.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Download the Online Retail dataset and place the CSV file in the `data/` folder with the following name:

`online_retail.csv`

4. Run the analysis from the project root:

```bash
python src/main.py
```

5. The analysis results will be displayed in the terminal.

## Excel Report

A prepared Excel report is available in the `reports/` folder as `sales_report.xlsx`.
