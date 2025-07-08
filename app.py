import streamlit as st
from monte_carlo import monte_carlo_simulation, plot_simulation
from explain import explain_risk
import numpy as np

st.title("📉 Portfolio Risk Analysis Chatbot")

mean = st.slider("Mean Daily Return (%)", -2.0, 2.0, 0.1) / 100
std = st.slider("Daily Volatility (%)", 0.0, 5.0, 1.0) / 100
days = st.number_input("Simulation Days", 30, 365, 252)
sims = st.number_input("Number of Simulations", 100, 10000, 1000)

if st.button("Run Simulation"):
    sims_data = monte_carlo_simulation(mean, std, days, sims)
    plot_simulation(sims_data)

    # VaR and CVaR calculation
    final_values = sims_data[:, -1]
    var_95 = np.percentile(final_values, 5)
    cvar_95 = final_values[final_values < var_95].mean()

    st.subheader("📊 Risk Metrics")
    st.write(f"5% VaR: ${round(var_95, 2)}")
    st.write(f"CVaR: ${round(cvar_95, 2)}")

    st.subheader("🤖 Explanation")
    with st.spinner("Generating explanation..."):
     explanation = explain_risk(var_95, cvar_95)
     st.markdown(explanation, unsafe_allow_html=True)


