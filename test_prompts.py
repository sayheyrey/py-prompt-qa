import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

# Load env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load CSV
df = pd.read_csv("AI_Prompts_Testing_Template - AI_Prompt_Testing_Template.csv")

# Prepare result columns
df["Response"] = ""
df["Token Cost"] = 0
df["Score"] = 0.0

# GPT-4 test 
def test_prompt(prompt_text):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_text}],
            temperature=0.7,
        )
        content = response.choices[0].message.content
        usage = response.usage.total_tokens
        return content, usage
    except Exception as e:
        return f"Error: {e}", 0

# Limit test to first 10 prompts (adjustable)
for i in tqdm(range(min(10, len(df)))):
    prompt = df.loc[i, "Prompt"]
    content, tokens = test_prompt(prompt)
    score = min(10.0, max(5.0, len(content) / 100))
    
    df.at[i, "Response"] = content
    df.at[i, "Token Cost"] = tokens
    df.at[i, "Score"] = round(score, 2)

# Save to new CSV
df.to_csv("TESTED_AI_Prompts_Testing_Template.csv", index=False)
print("✅ First 10 prompts tested and saved.")
