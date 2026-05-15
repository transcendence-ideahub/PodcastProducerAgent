from .llm_helper import generate_json_content

def generate_summary(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an expert podcast producer. Generate a JSON object with 'executive_summary' (150 words), 'short_description' (50 words), and 'hook' (one sentence) based on the transcript."
    prompt = f"Transcript:\n{transcript[:10000]}"
    return generate_json_content(prompt, system_prompt, api_key, model)
