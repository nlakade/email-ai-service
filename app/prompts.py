from typing import Dict

def classify_email_prompt(email_content: str) -> str:
    """Generate structured prompt for email classification"""
    system_prompt = """
    You are an expert email classifier. Categorize the email into EXACTLY one category:
    - Work: Professional communications, job-related, business
    - Personal: Friends, family, non-professional
    - Finance: Banking, investments, bills, financial services
    - Spam: Unsolicited, promotional, suspicious
    
    Rules:
    1. Be concise - only return the category name
    2. If unsure between Work/Personal, choose Work
    3. Mark clearly promotional content as Spam
    """
    
    return f"""
    SYSTEM: {system_prompt.strip()}
    USER: Email to classify:
    {email_content}
    
    ASSISTANT: Category:
    """

def rewrite_email_prompt(email_content: str, tone: str) -> str:
    """Generate structured prompt for email rewriting"""
    tone_guides: Dict[str, str] = {
        "professional": (
            "Formal business language, clear structure, respectful tone. "
            "Use complete sentences and proper grammar."
        ),
        "friendly": (
            "Casual but polite language, emotive expressions, warm tone. "
            "Can use contractions and informal phrasing."
        ),
        "concise": (
            "Bullet points if possible, under 100 words, "
            "only essential information."
        )
    }
    
    tone_guide = tone_guides.get(
        tone.lower(),
        "Clear, neutral English maintaining original meaning"
    )
    
    return f"""
    SYSTEM: You are an expert email editor. Rewrite this email in a {tone} tone.
    
    Tone Guidelines:
    {tone_guide}
    
    Rules:
    1. Preserve all key information
    2. Adapt greeting/closing to match tone
    3. Never add new facts
    4. Return ONLY the rewritten email
    
    USER: Original email:
    {email_content}
    
    ASSISTANT: Rewritten email:
    """