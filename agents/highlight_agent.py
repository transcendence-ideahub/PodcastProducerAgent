from .llm_helper import generate_json_content

def generate_highlights(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an expert podcast producer. Extract highlights from the transcript. Return a JSON object with 'quotes' (list of top 5 memorable quotes) and 'chapters' (list of dictionaries with 'timestamp' string like '00:00' and 'title')."
    prompt = f"Transcript:\n{transcript[:10000]}"
    return generate_json_content(prompt, system_prompt, api_key, model)
