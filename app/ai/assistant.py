from openai import OpenAI
import os
from app.ai.prompts import CAMPAIGN_EXPLANATION_PROMPT

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_campaign(plan):
    """
    Generate an AI explanation of a mail campaign plan.
    Uses OpenAI GPT-4 to translate technical details into plain language.
    
    Args:
        plan: String representation of the campaign plan
        
    Returns:
        String explanation suitable for print shop operations team
        
    Raises:
        Exception: If OpenAI API call fails
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{
                "role": "system",
                "content": "You are a helpful assistant that explains mail logistics to print shop operations teams."
            }, {
                "role": "user",
                "content": CAMPAIGN_EXPLANATION_PROMPT.format(plan=plan)
            }],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    
    except Exception as e:
        raise Exception(f"OpenAI API error: {str(e)}")
