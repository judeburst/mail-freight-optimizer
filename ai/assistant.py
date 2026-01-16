import openai
from app.ai.prompts import DROP_EXPLANATION_PROMPT

def explain_plan(plan):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": DROP_EXPLANATION_PROMPT.format(plan=plan)
        }]
    )
    return response.choices[0].message.content
