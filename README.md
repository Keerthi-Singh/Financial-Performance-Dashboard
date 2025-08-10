# Financial Performance Dashboard

Interactive dashboard for tracking financial performance metrics including profit margins, revenue trends, operational costs, and cost drivers.

## Features

- Real-time KPI tracking (Revenue, Expenses, Profit, Margin)
- Filtering by date, region, and department
- Interactive charts and visualizations
- CSV data export
- Historical data from 2021-2023

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate sample data:
   ```bash
   python generate_data.py
   ```

3. Run dashboard:
   ```bash
   python -m streamlit run src/app.py
   ```

## Data Columns

- Date, Region, Department
- Revenue, Cost of Goods Sold
- Operating, Marketing, Other Expenses

## Technologies

- Python, Streamlit, Pandas, Plotly
