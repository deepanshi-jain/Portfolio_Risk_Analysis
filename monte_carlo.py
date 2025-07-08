import matplotlib.pyplot as plt
import numpy as np
import streamlit as st  # ✅ Import Streamlit

def monte_carlo_simulation(mean, std_dev, days=252, simulations=1000, start_val=100000):
    results = []
    for _ in range(simulations):
        daily_returns = np.random.normal(mean, std_dev, days)
        prices = start_val * np.cumprod(1 + daily_returns)
        results.append(prices)
    return np.array(results)

def plot_simulation(simulations):
    plt.figure(figsize=(10, 5))
    for sim in simulations:
        plt.plot(sim, color='blue', alpha=0.03)
    plt.title("Monte Carlo Simulation of Portfolio Value")
    plt.xlabel("Days")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    
    st.pyplot(plt)  # ✅ Renders the chart in Streamlit
