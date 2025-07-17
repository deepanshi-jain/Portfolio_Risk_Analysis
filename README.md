# 💼 Portfolio Risk Analysis Chatbot

A conversational AI tool that explains financial risk metrics—**Value at Risk (VaR)** and **Conditional Value at Risk (CVaR)**—in simple terms using **Monte Carlo simulations** and **GPT-4-powered natural language explanations**.

> 🔍 Ideal for investors, analysts, students, and finance professionals who want intuitive, visual, and AI-assisted insights into portfolio risks.

---

## 🧠 Project Overview

Traditional risk metrics can be hard to interpret. This chatbot:

- Simulates portfolio performance using **Monte Carlo methods**
- Computes **VaR** and **CVaR** based on those simulations
- Uses **OpenAI GPT-4** to explain those metrics in plain English
- Visualizes risk distributions and outcomes
- Presents everything in an interactive **Streamlit** app

---

## 🛠 Tech Stack

| Component     | Technology                       |
|---------------|----------------------------------|
| UI            | Streamlit                        |
| LLM           | OpenAI GPT-4                     |
| Math / Sim    | NumPy, Monte Carlo Simulation    |
| Charts        | Matplotlib                       |
| Orchestration | LangChain (LLM prompt handling)  |
| API Keys      | Python-dotenv                    |

---

## 📉 Features

- 🔢 **Monte Carlo simulation** of portfolio returns
- 💰 Computes **5% Value at Risk (VaR)** and **Conditional VaR**
- 🤖 **GPT-4-based explanations** for financial metrics
- 📈 **Risk visualization** using histograms
- 🧾 Clean UI with markdown explanations
- 🔐 API key handling with `.env` file

---

## 🧪 How It Works

1. **Simulation**:
   - Randomly simulates portfolio returns (based on given mean, std dev, and value).
   - Generates thousands of scenarios.

2. **Risk Metrics**:
   - Calculates the 5% **VaR** (threshold beyond which 5% worst losses lie).
   - Calculates **CVaR** as the average loss beyond the VaR threshold.

3. **LLM Explanation**:
   - Sends both metrics to GPT-4 for a human-friendly explanation.
   - Optionally removes formatting noise like asterisks or underscores.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/deepanshi-jain/portfolio-risk-chatbot.git
cd portfolio-risk-chatbot
```
### 2.Install Dependencies
   ```bash
      pip install -r requirements.txt

```
### 3.Set Up OpenAI API Key
```bash
OPENAI_API_KEY=your_openai_key_here
```
### 4.  Run the App
```bash
streamlit run app.py
```



## 📊 Example Use Case

Imagine you're analyzing a portfolio with the following assumptions:

- 📈 Mean Daily Return: **0.1%**
- 📉 Daily Volatility: **1.2%**
- 📆 Investment Horizon: **252 trading days (1 year)**
- 🔁 Simulations: **1000**
- 💼 Starting Value: **₹100,000**

After running the simulation, the app returns:

📉 Value at Risk (VaR 5%): ₹94,856.22
🚨 Conditional VaR (CVaR 5%): ₹89,103.94


💬 **Explanation by GPT-4**:

> With a 5% probability, your portfolio could fall below ₹94,856.22 by the end of the year. If that happens, the average loss among those worst-case scenarios would be ₹89,103.94. These metrics help quantify the downside risk of your investment.

The line chart visualizes over 1000 simulated portfolio paths, showing how values fluctuate over time and where the risk zones lie.





## 🌱 Future Enhancements

Here are features planned for upcoming versions:

- 📁 **Portfolio CSV Upload**  
  Let users upload their actual portfolio (ticker + weight) for personalized simulation.

- 📉 **Real Market Data Integration**  
  Fetch live stock or ETF prices using APIs like Yahoo Finance or Alpha Vantage.

- 📊 **More Risk Metrics**  
  Include Sharpe Ratio, Sortino Ratio, Max Drawdown, and Rolling VaR.

- 🧠 **Conversational Memory**  
  Let users ask follow-up questions about their results using LangChain-style memory.

- 🌐 **Multi-language Support**  
  Offer risk explanations in Hindi, Spanish, French, and more.

- 📤 **Deploy on Streamlit Cloud or Hugging Face Spaces**  
  Host a live demo version online with secure API key management.

- 🖼️ **Save Chart as Image/PDF**  
  Add a download button for simulation plots and reports.

- 💬 **Chat History + PDF Export**  
  Enable saving entire risk conversations as a downloadable PDF report.




