from .llm_helper import generate_json_content

def generate_social_media(transcript: str, api_key: str, model: str = "gpt-3.5-turbo") -> dict:
    system_prompt = "You are an expert social media manager. Generate promotional posts for the podcast episode. Return a JSON object with 'linkedin' (professional summary), 'twitter_thread' (list of 5 tweets), 'instagram' (engaging caption with emojis), and 'youtube_description' (SEO optimized)."
    prompt = f"Transcript:\n{transcript[:10000]}"
    return generate_json_content(prompt, system_prompt, api_key, model)
