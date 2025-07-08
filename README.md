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

##💡 Example Use
You input:

Mean Daily Return: 0.1%

Volatility: 1.0%

Days: 252

Simulations: 1000

Output:

VaR: $98,200

CVaR: $92,500

GPT-4 Explanation:

There is a 5% chance your portfolio will drop below $98,200 after one year. In those worst-case scenarios, the average loss is about $92,500.



##🌍 Future Enhancements
Upload portfolio CSV files

Pull real-time asset data (e.g., via yfinance)

Use LangChain for multi-turn financial conversations

Add Sharpe ratio, drawdown, and correlation heatmaps

Deploy to Streamlit Cloud / Hugging Face Spaces



