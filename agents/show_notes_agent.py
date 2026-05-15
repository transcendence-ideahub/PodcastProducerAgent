from .llm_helper import generate_json_content

def generate_show_notes(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an expert podcast producer. Create structured show notes. Return a JSON object with keys: 'introduction', 'main_points' (list of strings), 'resources_mentioned' (list of strings), 'actionable_insights' (list of strings), 'closing_thoughts'."
    prompt = f"Transcript:\n{transcript[:10000]}"
    return generate_json_content(prompt, system_prompt, api_key, model)
