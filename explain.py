import os
import openai
import re
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_risk(var, cvar):
    prompt = (
        f"Explain Value at Risk (VaR) and Conditional Value at Risk (CVaR) in simple terms. "
        f"The 5% VaR is {var:,.2f}, and the CVaR is {cvar:,.2f}. "
        f"What do these numbers mean for an investor?"
    )

    # Use updated openai client
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    raw_text = response.choices[0].message.content
    return clean_response(raw_text)


def clean_response(text):
    # Remove markdown formatting and special characters
    text = re.sub(r'[*_`$]', '', text)         # remove *, _, `, $
    text = re.sub(r'\s+', ' ', text)           # remove extra spaces and newlines
    text = re.sub(r'\\\((.*?)\\\)', r'\1', text)  # remove LaTeX-style \( \)
    text = re.sub(r'\$(.*?)\$', r'\1', text)      # remove $...$ math
    return text.strip()
