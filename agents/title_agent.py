from .llm_helper import generate_json_content

def generate_titles(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an expert podcast producer. Generate 5 compelling, SEO-friendly podcast episode titles based on the transcript. Return ONLY a JSON object with a key 'titles' containing a list of dictionaries, each with 'title', 'catchiness_score' (1-10), and 'seo_score' (1-10)."
    prompt = f"Transcript:\n{transcript[:10000]}" # Limiting length for context window if needed, but modern models can handle more.
    return generate_json_content(prompt, system_prompt, api_key, model)
