# 📊 Financial Performance Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-purple.svg)](https://plotly.com/python/)

A comprehensive, interactive dashboard for tracking financial performance metrics including profit margins, revenue trends, operational costs, and cost drivers across different regions and departments.

## 🚀 Features

- **📈 Real-time KPI Tracking**: Monitor Total Revenue, Total Expenses, Net Profit, and Profit Margin
- **🔍 Advanced Filtering**: Filter data by date range, region, and department
- **📊 Interactive Visualizations**: 
  - Revenue vs Expenses time series
  - Expense breakdown pie chart
  - Cost drivers by department (stacked bar chart)
- **📋 Data Export**: Download filtered results as CSV
- **🌍 Multi-dimensional Analysis**: Analyze performance across regions (North America, Europe, Asia-Pacific) and departments (Sales, Operations, Marketing, R&D)
- **📅 Historical Data**: Comprehensive dataset from January 2021 to December 2023

## 🏗️ Project Structure

```
financial-dashboard/
├── data/
│   └── financial_data.csv          # Synthetic financial dataset
├── src/
│   ├── analyser.py                 # Data analysis and chart generation
│   └── app.py                      # Streamlit web application
├── generate_data.py                 # Dataset generation script
├── requirements.txt                 # Python dependencies
├── test_dashboard.py                # Functionality testing script
└── README.md                       # Project documentation
```

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework for interactive dashboards
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations and synthetic data generation
- **Plotly**: Interactive data visualizations

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/financial-performance-dashboard.git
   cd financial-performance-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate sample data**
   ```bash
   python generate_data.py
   ```

## 🚀 Usage

### Running the Dashboard

Start the Streamlit application:
```bash
streamlit run src/app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Alternative Launch Method

If `streamlit` command is not recognized:
```bash
python -m streamlit run src/app.py
```

## 📊 Data Schema

The synthetic dataset includes the following columns:

| Column | Description | Example Values |
|--------|-------------|----------------|
| `Date` | Transaction date | 2021-01-01 to 2023-12-31 |
| `Year` | Year of transaction | 2021, 2022, 2023 |
| `Month` | Month of transaction | 1-12 |
| `Region` | Geographic region | North America, Europe, Asia-Pacific |
| `Department` | Business department | Sales, Operations, Marketing, R&D |
| `Revenue` | Total revenue amount | $1,000 - $100,000+ |
| `Cost_of_Goods_Sold` | Direct production costs | 40-60% of revenue |
| `Operating_Expenses` | General operational costs | 20-30% of revenue |
| `Marketing_Expenses` | Marketing and advertising costs | 10-20% of revenue |
| `Other_Expenses` | Miscellaneous costs | 5-15% of revenue |

## 🔍 Dashboard Features

### Filters
- **Date Range**: Select specific time periods for analysis
- **Region**: Filter by geographic regions
- **Department**: Focus on specific business units

### Key Performance Indicators (KPIs)
- **Total Revenue**: Sum of all revenue across selected filters
- **Total Expenses**: Sum of all expense categories
- **Net Profit**: Revenue minus total expenses
- **Profit Margin**: Net profit as a percentage of revenue

### Visualizations
1. **Revenue vs Expenses Timeline**: Line chart showing trends over time
2. **Expense Breakdown**: Pie chart displaying expense category distribution
3. **Cost Drivers by Department**: Stacked bar chart showing expense allocation

### Data Export
- Download filtered results as CSV file
- Includes all data matching current filter criteria

## 🧪 Testing

Run the test suite to verify functionality:
```bash
python test_dashboard.py
```

This script tests:
- Data loading and parsing
- Filtering functionality
- KPI calculations
- Chart generation
- Summary statistics

## 🔄 Regenerating Data

To create a new synthetic dataset with different parameters:
```bash
python generate_data.py
```

The script generates realistic data with:
- Seasonal variations (Q4 peaks, Q1 slumps)
- Year-over-year growth patterns
- Regional and departmental variations
- Random fluctuations for realism

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for rapid web app development
- Data visualization powered by [Plotly](https://plotly.com/python/)
- Data manipulation with [Pandas](https://pandas.pydata.org/)

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/financial-performance-dashboard/issues) page
2. Create a new issue with detailed description
3. Include your Python version and error messages

---

**⭐ Star this repository if you find it helpful!** 