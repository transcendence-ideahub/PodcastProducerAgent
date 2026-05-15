import json
import re
from groq import Groq

def generate_content(prompt: str, system_prompt: str, api_key: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Call Groq LLM and return raw text response."""
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=4096
    )
    return response.choices[0].message.content


def generate_json_content(prompt: str, system_prompt: str, api_key: str, model: str = "llama-3.3-70b-versatile") -> dict:
    """Call Groq LLM and return a parsed JSON dict."""
    client = Groq(api_key=api_key)
    
    json_system_prompt = system_prompt + "\n\nIMPORTANT: Respond ONLY with valid, raw JSON. No markdown code fences, no explanation text."
    
    raw = ""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": json_system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4096,
            response_format={"type": "json_object"}
        )
        raw = response.choices[0].message.content.strip()
        return json.loads(raw)
    except json.JSONDecodeError:
        # Strip any accidental markdown fences and retry parsing
        cleaned = re.sub(r"```(?:json)?", "", raw).strip().rstrip("`").strip()
        try:
            return json.loads(cleaned)
        except Exception as e:
            raise RuntimeError(f"Groq JSON parse failed: {e}\nRaw: {raw[:300]}")
    except Exception as e:
        raise RuntimeError(f"Groq LLM error: {e}")
