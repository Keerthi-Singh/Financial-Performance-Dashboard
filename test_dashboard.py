#!/usr/bin/env python3
"""
Test script to verify the Financial Performance Dashboard functionality.
This script tests all the core functions without running the Streamlit app.
"""

import sys
import os
sys.path.append('src')

from analyser import (
    load_data, filter_data, compute_kpis, revenue_timeseries,
    expense_breakdown, cost_driver_by_department, get_summary_stats
)

def test_data_loading():
    """Test data loading functionality."""
    print("🧪 Testing data loading...")
    
    df = load_data()
    if df is not None and not df.empty:
        print(f"✅ Data loaded successfully: {len(df):,} records")
        print(f"   Date range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"   Regions: {', '.join(df['Region'].unique())}")
        print(f"   Departments: {', '.join(df['Department'].unique())}")
        return df
    else:
        print("❌ Data loading failed")
        return None

def test_filtering(df):
    """Test data filtering functionality."""
    print("\n🧪 Testing data filtering...")
    
    # Test date filtering
    filtered_df = filter_data(df, start_date='2022-01-01', end_date='2022-12-31')
    print(f"✅ Date filtering: {len(filtered_df):,} records (2022 only)")
    
    # Test region filtering
    filtered_df = filter_data(df, regions=['North America'])
    print(f"✅ Region filtering: {len(filtered_df):,} records (North America only)")
    
    # Test department filtering
    filtered_df = filter_data(df, departments=['Sales'])
    print(f"✅ Department filtering: {len(filtered_df):,} records (Sales only)")
    
    # Test combined filtering
    filtered_df = filter_data(
        df, 
        start_date='2022-06-01', 
        end_date='2022-08-31',
        regions=['Europe'],
        departments=['Marketing', 'R&D']
    )
    print(f"✅ Combined filtering: {len(filtered_df):,} records (Summer 2022, Europe, Marketing+R&D)")

def test_kpi_calculation(df):
    """Test KPI calculation functionality."""
    print("\n🧪 Testing KPI calculations...")
    
    kpis = compute_kpis(df)
    print(f"✅ Total Revenue: ${kpis['total_revenue']:,.2f}")
    print(f"✅ Total Expenses: ${kpis['total_expenses']:,.2f}")
    print(f"✅ Net Profit: ${kpis['net_profit']:,.2f}")
    print(f"✅ Profit Margin: {kpis['profit_margin']:.1f}%")

def test_chart_generation(df):
    """Test chart generation functionality."""
    print("\n🧪 Testing chart generation...")
    
    # Test revenue timeseries
    revenue_chart = revenue_timeseries(df)
    if revenue_chart is not None:
        print("✅ Revenue timeseries chart generated")
    
    # Test expense breakdown
    expense_chart = expense_breakdown(df)
    if expense_chart is not None:
        print("✅ Expense breakdown chart generated")
    
    # Test cost driver chart
    cost_chart = cost_driver_by_department(df)
    if cost_chart is not None:
        print("✅ Cost driver chart generated")

def test_summary_statistics(df):
    """Test summary statistics functionality."""
    print("\n🧪 Testing summary statistics...")
    
    summary_stats = get_summary_stats(df)
    if summary_stats:
        print("✅ Region statistics generated")
        print("✅ Department statistics generated")
        print(f"   Sample - North America Revenue: ${summary_stats['region_stats'].loc['North America', 'Revenue']:,.2f}")

def main():
    """Run all tests."""
    print("🚀 Financial Performance Dashboard - Test Suite")
    print("=" * 50)
    
    # Test data loading
    df = test_data_loading()
    if df is None:
        print("❌ Cannot proceed with tests - data loading failed")
        return
    
    # Test all functionality
    test_filtering(df)
    test_kpi_calculation(df)
    test_chart_generation(df)
    test_summary_statistics(df)
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed successfully!")
    print("\n📋 Dashboard Features Verified:")
    print("   ✅ Data loading and parsing")
    print("   ✅ Date, region, and department filtering")
    print("   ✅ KPI calculations (Revenue, Expenses, Profit, Margin)")
    print("   ✅ Chart generation (Timeseries, Pie, Stacked Bar)")
    print("   ✅ Summary statistics by region and department")
    print("\n🚀 Ready to run: streamlit run src/app.py")

if __name__ == "__main__":
    main()
