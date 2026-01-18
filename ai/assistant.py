import openai
from app.ai.prompts import CAMPAIGN_EXPLANATION_PROMPT

def explain_campaign(plan):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": CAMPAIGN_EXPLANATION_PROMPT.format(plan=plan)
        }]
    )
    return response.choices[0].message.content
