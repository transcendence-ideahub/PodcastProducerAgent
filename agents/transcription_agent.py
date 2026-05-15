from groq import Groq
import logging
from .llm_helper import generate_content

def transcribe_audio(file_path: str, api_key: str) -> str:
    """
    Two-stage professional transcription pipeline:
    1. RAW: Groq Whisper Large V3 extracts the raw text.
    2. REFINERY: LLaMA 3.3 70B performs 'Agentic Diarization' to identify speakers, 
       fix grammar, and structure the conversation into a professional dialogue.
    """
    try:
        client = Groq(api_key=api_key)
        logging.info(f"Starting Groq Whisper transcription for {file_path}")

        # Stage 1: Raw Transcription
        with open(file_path, "rb") as audio_file:
            raw_result = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                response_format="text",
                prompt="""Please provide a verbatim transcript. Keep all details."""
            )
        
        raw_text = str(raw_result)
        logging.info("Raw transcription complete. Starting Agentic Diarization refinery...")

        # Stage 2: Agentic Diarization & Refinement
        system_prompt = """
        You are an expert Professional Transcriptionist and Conversation Architect.
        Your task is to take a raw, unstructured transcript and turn it into a high-fidelity, professional dialogue.
        
        RULES:
        1. Identify speaker changes. Use logical labels like 'Host:', 'Guest:', 'Interviewer:', or 'Speaker A/B' if names aren't clear.
        2. Format as a clean dialogue with a new line for every speaker turn.
        3. Add approximate semantic timestamps (e.g. [00:00], [02:15]) if the flow suggests it, or just focus on the speaker turn structure.
        4. Correct obvious AI transcription errors while maintaining the speaker's original intent and tone.
        5. DO NOT add any intro/outro text. Return ONLY the refined transcript.
        """
        
        refined_transcript = generate_content(
            prompt=f"Raw Transcript:\n{raw_text}",
            system_prompt=system_prompt,
            api_key=api_key,
            model="llama-3.3-70b-versatile"
        )

        logging.info("Agentic Diarization complete.")
        return refined_transcript

    except Exception as e:
        logging.error(f"Transcription/Refinery failed: {e}")
        raise e
