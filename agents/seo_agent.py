from .llm_helper import generate_json_content

def generate_seo(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an SEO expert. Generate SEO metadata for the podcast. Return a JSON object with 'keywords' (list of 10 strings), 'hashtags' (list of 10 strings), and 'meta_description' (160 characters max)."
    prompt = f"Transcript:\n{transcript[:10000]}"
    return generate_json_content(prompt, system_prompt, api_key, model)
