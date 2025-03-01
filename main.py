import numpy as np
import matplotlib.pyplot as plt

def compound_interest(P, r, n, t):
    """Calculate compound interest."""
    FV = P * (1 + r/n) ** (n*t)
    return FV

def adjust_for_inflation(future_value, inflation_rate, years):
    """Calculate future value adjusted for inflation."""
    adjusted_value = future_value / ((1 + inflation_rate) ** years)
    return adjusted_value

def plot_investment_growth(P, r, n, t, inflation_rate):
    """Visualize investment growth over time (adjusted for inflation)."""
    years = np.arange(0, t+1, 1)
    values = [compound_interest(P, r, n, year) for year in years]
    adjusted_values = [adjust_for_inflation(val, inflation_rate, year) for val, year in zip(values, years)]
    
    plt.figure(figsize=(10, 5))
    plt.plot(years, values, marker='o', linestyle='-', color='b', label='Nominal Investment Growth')
    plt.plot(years, adjusted_values, marker='o', linestyle='--', color='r', label='Inflation-Adjusted Growth')
    plt.xlabel('Years')
    plt.ylabel('Future Value ($)')
    plt.title('Investment Growth Over Time (Adjusted for Inflation)')
    plt.legend()
    plt.grid()
    plt.show()

# User inputs
total_investment = float(input("Enter initial investment amount ($): "))
interest_rate = float(input("Enter annual interest rate (as %): ")) / 100
compounds_per_year = int(input("Enter number of times interest compounds per year: "))
investment_years = int(input("Enter investment duration in years: "))
inflation_rate = float(input("Enter expected annual inflation rate (as %): ")) / 100

# Future Value Calculation
future_value = compound_interest(total_investment, interest_rate, compounds_per_year, investment_years)
adjusted_value = adjust_for_inflation(future_value, inflation_rate, investment_years)

print(f"Future Value (FV) after {investment_years} years: ${future_value:.2f}")
print(f"Inflation-Adjusted Future Value: ${adjusted_value:.2f}")

# Plot the graph
plot_investment_growth(total_investment, interest_rate, compounds_per_year, investment_years, inflation_rate)
