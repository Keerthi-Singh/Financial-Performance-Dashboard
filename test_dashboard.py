#!/usr/bin/env python3
"""
Financial Performance Dashboard - Streamlit App
This is a simplified version of the dashboard for testing and demonstration.
"""

import streamlit as st
import sys
import os
sys.path.append('src')

from analyser import (
    load_data, filter_data, compute_kpis, revenue_timeseries,
    expense_breakdown, cost_driver_by_department, get_summary_stats
)

# Page configuration
st.set_page_config(
    page_title="Financial Dashboard - Test Version",
    page_icon="📊",
    layout="wide"
)

def main():
    st.title("Financial Performance Dashboard - Test Version")
    st.write("This is a simplified dashboard for testing the core functionality.")
    
    # Load data
    with st.spinner("Loading data..."):
        df = load_data()
    
    if df is None:
        st.error("❌ Data not found! Please run `python generate_data.py` first.")
        st.stop()
    
    st.success(f"✅ Data loaded successfully: {len(df):,} records")
    
    # Display basic info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", f"{len(df):,}")
    with col2:
        st.metric("Date Range", f"{df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}")
    with col3:
        st.metric("Regions", len(df['Region'].unique()))
    
    # Simple filters
    st.subheader("Quick Filters")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_regions = st.multiselect(
            "Select Regions",
            options=df['Region'].unique(),
            default=df['Region'].unique()
        )
    
    with col2:
        selected_departments = st.multiselect(
            "Select Departments",
            options=df['Department'].unique(),
            default=df['Department'].unique()
        )
    
    # Filter data
    filtered_df = filter_data(df, regions=selected_regions, departments=selected_departments)
    
    # Calculate KPIs
    kpis = compute_kpis(filtered_df)
    
    # Display KPIs
    st.subheader("Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}")
    with col2:
        st.metric("Total Expenses", f"${kpis['total_expenses']:,.0f}")
    with col3:
        st.metric("Net Profit", f"${kpis['net_profit']:,.0f}")
    with col4:
        st.metric("Profit Margin", f"{kpis['profit_margin']:.1f}%")
    
    # Generate charts
    st.subheader("Charts")
    
    # Revenue timeseries
    revenue_chart = revenue_timeseries(filtered_df)
    if revenue_chart:
        st.plotly_chart(revenue_chart, use_container_width=True)
    
    # Expense breakdown
    expense_chart = expense_breakdown(filtered_df)
    if expense_chart:
        st.plotly_chart(expense_chart, use_container_width=True)
    
    # Cost driver chart
    cost_chart = cost_driver_by_department(filtered_df)
    if cost_chart:
        st.plotly_chart(cost_chart, use_container_width=True)
    
    # Data table
    st.subheader("Filtered Data")
    st.dataframe(filtered_df.head(100), use_container_width=True)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="financial_data_filtered.csv",
        mime="text/csv"
    )
    
    # Summary statistics
    st.subheader("Summary Statistics")
    summary_stats = get_summary_stats(filtered_df)
    
    if summary_stats:
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Revenue by Region**")
            st.dataframe(summary_stats['region_stats']['Revenue'].round(2))
        
        with col2:
            st.write("**Revenue by Department**")
            st.dataframe(summary_stats['department_stats']['Revenue'].round(2))

if __name__ == "__main__":
    main()
