import pandas as pd
import matplotlib.pyplot as plt

# Read Total Revenue data from CSV file
def read_sales_data(filename):
    return pd.read_csv(filename)

# Clean the data by handling missing values and inconsistencies
def clean_sales_data(sales_data):
    # Drop rows with missing values
    cleaned_data = sales_data.dropna()

    cleaned_data = cleaned_data[cleaned_data['Total Revenue'] > 0]
    return cleaned_data

# Calculate key metrics
def calculate_metrics(sales_data):
    total_sales = sales_data['Total Revenue'].sum()
    average_order_value = sales_data['Total Revenue'].mean()
    sales_by_region = sales_data.groupby('Region')['Total Revenue'].sum()
    return total_sales, average_order_value, sales_by_region

# Visualize results
def visualize_results(sales_by_region):
    sales_by_region.plot(kind='bar', rot=45, color='skyblue')
    plt.title('Sales by Region',fontdict={'family':'serif','color':'blue','size':18},loc='center')
    plt.xlabel('Region')
    plt.ylabel('Total Revenue',fontdict={'family':'serif','color':'red','size':18})
    plt.show()

# Main function
def main():
    # File path of sales data CSV
    filename = 'C:/Users/SWEETA/Desktop/Python/Project/Sales.csv'
    
    # Read sales data
    sales_data = read_sales_data(filename)
    
    # Clean data
    cleaned_data = clean_sales_data(sales_data)
    
    # Calculate metrics
    total_sales, average_order_value, sales_by_region = calculate_metrics(cleaned_data)
    
    # Print metrics
    print("Total Sales:", total_sales)
    print("Average Order Value:", average_order_value)
    print("\nSales by Region:")
    print(sales_by_region)
    
    # graph plotting
    visualize_results(sales_by_region)

if __name__ == "__main__":
    main()
