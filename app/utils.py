import os
from dotenv import load_dotenv
from openai import OpenAI, APIConnectionError, RateLimitError, AuthenticationError, APIError
import logging

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def get_llm_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model=os.getenv("LLM_MODEL", "gpt-3.5-turbo"),  
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        return response.choices[0].message.content
        
    except RateLimitError as e:
        raise Exception(f"Rate limit exceeded: {e}")
    except AuthenticationError as e:
        raise Exception(f"Authentication failed: {e}")
    except APIConnectionError as e:
        raise Exception(f"API connection failed: {e}")
    except APIError as e:
        raise Exception(f"OpenAI API error: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")