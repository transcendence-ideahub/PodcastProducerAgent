import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import effects as pydub_effects
import logging


def clean_audio(input_path: str, output_path: str, silence_thresh: int = -50, min_silence_len: int = 1500) -> dict:
    """
    Professional-grade audio cleaning pipeline:
    1. Silence removal (user-configurable)
    2. Volume normalization (LUFS-style target)
    3. High-pass filter (removes low-frequency hum/rumble below 80Hz)
    4. Low-pass filter (removes high-frequency hiss above 12kHz)
    5. Dynamic range compression (evens out loud/quiet speakers)
    6. Stereo-to-mono conversion (optimal for speech/podcasts)
    7. Re-export at 192kbps MP3

    Returns a dictionary with before/after durations and processing stats.
    """
    try:
        logging.info(f"[Audio Cleaner] Loading audio: {input_path}")
        audio = AudioSegment.from_file(input_path)

        original_duration_ms = len(audio)
        original_channels = audio.channels
        original_dbfs = round(audio.dBFS, 2)

        # --- Step 1: Convert to mono (better for speech processing) ---
        logging.info("[Audio Cleaner] Converting to mono...")
        audio = audio.set_channels(1)

        # --- Step 2: High-pass filter — removes low rumble/hum (< 80Hz) ---
        logging.info("[Audio Cleaner] Applying high-pass filter (80Hz cutoff)...")
        audio = pydub_effects.high_pass_filter(audio, cutoff=80)

        # --- Step 3: Low-pass filter — softens high-frequency hiss (> 12kHz) ---
        logging.info("[Audio Cleaner] Applying low-pass filter (12000Hz cutoff)...")
        audio = pydub_effects.low_pass_filter(audio, cutoff=12000)

        # --- Step 4: Silence removal ---
        logging.info("[Audio Cleaner] Removing long silences...")
        chunks = split_on_silence(
            audio,
            min_silence_len=min_silence_len,
            silence_thresh=silence_thresh,
            keep_silence=300  # keep a small natural gap for readability
        )

        if chunks:
            cleaned_audio = chunks[0]
            for chunk in chunks[1:]:
                cleaned_audio += chunk
        else:
            cleaned_audio = audio

        # --- Step 5: Dynamic range compression ---
        # Evens out loud and quiet speakers so volume is consistent throughout
        logging.info("[Audio Cleaner] Applying dynamic range compression...")
        cleaned_audio = pydub_effects.compress_dynamic_range(
            cleaned_audio,
            threshold=-20.0,
            ratio=4.0,
            attack=5.0,
            release=50.0
        )

        # --- Step 6: Volume normalization (target -16 LUFS for podcasts) ---
        logging.info("[Audio Cleaner] Normalizing volume to -16 dBFS...")
        target_dBFS = -16.0
        change_in_dBFS = target_dBFS - cleaned_audio.dBFS
        cleaned_audio = cleaned_audio.apply_gain(change_in_dBFS)

        cleaned_duration_ms = len(cleaned_audio)

        # --- Step 7: Export at high quality ---
        logging.info(f"[Audio Cleaner] Exporting cleaned audio to {output_path}")
        cleaned_audio.export(output_path, format="mp3", bitrate="192k")

        stats = {
            "original_duration_sec": round(original_duration_ms / 1000, 2),
            "cleaned_duration_sec": round(cleaned_duration_ms / 1000, 2),
            "time_saved_sec": round((original_duration_ms - cleaned_duration_ms) / 1000, 2),
            "original_channels": original_channels,
            "original_dbfs": original_dbfs,
            "output_dbfs": round(cleaned_audio.dBFS, 2),
            "silence_removed_pct": round(100 * (original_duration_ms - cleaned_duration_ms) / max(original_duration_ms, 1), 1)
        }

        logging.info(f"[Audio Cleaner] Done. Stats: {stats}")
        return stats

    except Exception as e:
        logging.error(f"[Audio Cleaner] Error: {str(e)}")
        raise e
