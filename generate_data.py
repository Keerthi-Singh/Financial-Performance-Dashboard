import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_financial_data():
    """
    Generate synthetic financial data from Jan 2021 to Dec 2023
    with realistic seasonal variations and business patterns.
    """
    
    # Create date range
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Define regions and departments
    regions = ['North America', 'Europe', 'Asia-Pacific']
    departments = ['Sales', 'Operations', 'Marketing', 'R&D']
    
    # Initialize lists to store data
    data = []
    
    for date in date_range:
        # Base values with seasonal adjustments
        month = date.month
        year = date.year
        
        # Seasonal multipliers (higher in Q4, lower in Q1)
        seasonal_multiplier = 1.0
        if month in [10, 11, 12]:  # Q4 - holiday season
            seasonal_multiplier = 1.3
        elif month in [1, 2, 3]:   # Q1 - post-holiday slump
            seasonal_multiplier = 0.8
        elif month in [4, 5, 6]:   # Q2 - spring recovery
            seasonal_multiplier = 1.1
        else:                       # Q3 - summer stability
            seasonal_multiplier = 1.0
        
        # Year-over-year growth
        year_growth = 1.0 + (year - 2021) * 0.15  # 15% annual growth
        
        for region in regions:
            for department in departments:
                # Base revenue varies by region and department
                base_revenue = {
                    'Sales': 50000,
                    'Operations': 30000,
                    'Marketing': 40000,
                    'R&D': 35000
                }
                
                # Regional multipliers
                region_multiplier = {
                    'North America': 1.2,
                    'Europe': 1.0,
                    'Asia-Pacific': 0.9
                }
                
                # Calculate revenue with all factors
                revenue = (base_revenue[department] * 
                          seasonal_multiplier * 
                          year_growth * 
                          region_multiplier[region] * 
                          np.random.normal(1.0, 0.1))  # Add some randomness
                
                # Ensure revenue is positive
                revenue = max(revenue, 1000)
                
                # Calculate costs based on revenue
                cost_of_goods_sold = revenue * np.random.uniform(0.4, 0.6)
                operating_expenses = revenue * np.random.uniform(0.2, 0.3)
                marketing_expenses = revenue * np.random.uniform(0.1, 0.2)
                other_expenses = revenue * np.random.uniform(0.05, 0.15)
                
                # Add some weekend/weekday variation
                if date.weekday() >= 5:  # Weekend
                    revenue *= 0.7
                    cost_of_goods_sold *= 0.7
                    operating_expenses *= 0.7
                    marketing_expenses *= 0.7
                    other_expenses *= 0.7
                
                # Add some random fluctuations
                noise = np.random.normal(1.0, 0.05)
                revenue *= noise
                cost_of_goods_sold *= noise
                operating_expenses *= noise
                marketing_expenses *= noise
                other_expenses *= noise
                
                # Ensure all values are positive and reasonable
                revenue = max(revenue, 1000)
                cost_of_goods_sold = max(cost_of_goods_sold, 100)
                operating_expenses = max(operating_expenses, 100)
                marketing_expenses = max(marketing_expenses, 50)
                other_expenses = max(other_expenses, 25)
                
                data.append({
                    'Date': date,
                    'Year': year,
                    'Month': month,
                    'Region': region,
                    'Department': department,
                    'Revenue': round(revenue, 2),
                    'Cost_of_Goods_Sold': round(cost_of_goods_sold, 2),
                    'Operating_Expenses': round(operating_expenses, 2),
                    'Marketing_Expenses': round(marketing_expenses, 2),
                    'Other_Expenses': round(other_expenses, 2)
                })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save to CSV
    output_path = 'data/financial_data.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Generated {len(df)} records of financial data")
    print(f"Data saved to: {output_path}")
    print(f"Date range: {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")
    print(f"Regions: {', '.join(df['Region'].unique())}")
    print(f"Departments: {', '.join(df['Department'].unique())}")
    print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")
    print(f"Total Expenses: ${(df['Cost_of_Goods_Sold'].sum() + df['Operating_Expenses'].sum() + df['Marketing_Expenses'].sum() + df['Other_Expenses'].sum()):,.2f}")
    
    return df

if __name__ == "__main__":
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate the data
    df = generate_financial_data()
    
    # Display sample data
    print("\nSample data:")
    print(df.head(10))
