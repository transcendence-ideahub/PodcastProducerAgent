# Podcast Producer Agent 🎙️

An automated AI-powered podcast post-production agent built with Streamlit and OpenAI. 
This application takes a raw audio file and automatically cleans it, transcribes it, and generates a suite of professional assets including titles, summaries, show notes, highlights, social media captions, and SEO tags.

## Features ✨

*   **Audio Cleanup**: Automatically detects and removes long silences and normalizes audio volume.
*   **Speech-to-Text**: High-accuracy transcription using OpenAI's Whisper model.
*   **AI Content Generation**:
    *   Catchy, SEO-optimized titles.
    *   Executive summaries and hooks.
    *   Structured show notes.
    *   Highlight quotes and chapter markers.
    *   Social media posts (LinkedIn, Twitter/X, Instagram, YouTube).
    *   SEO keywords and meta descriptions.
*   **Analytics**: Word clouds and topic frequency charts.
*   **Human-in-the-loop**: Fully editable UI to review and modify AI outputs before export.
*   **Export Options**: Download a comprehensive ZIP package containing PDF reports, Markdown, JSON, and the cleaned audio.

## Installation & Setup 🛠️

### Prerequisites

*   Python 3.11+
*   **FFmpeg**: Required for audio processing via `pydub`.
    *   Mac: `brew install ffmpeg`
    *   Linux: `sudo apt install ffmpeg`
    *   Windows: Download from the official site and add to PATH.

### Local Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/podcast_producer_agent.git
    cd podcast_producer_agent
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:
    *   Copy `.env.example` to `.env`.
    *   Add your `OPENAI_API_KEY`.

### Running the App

```bash
streamlit run app.py
```

## Docker Deployment 🐳

Build the image:
```bash
docker build -t podcast-agent .
```

Run the container:
```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key_here podcast-agent
```

## Screenshots 📸

*(Placeholder for screenshots of the dashboard, analytics, and export)*

## Future Enhancements 🚀
*   Local transcription using `faster-whisper` for offline use.
*   Speaker diarization (identifying "Speaker 1", "Speaker 2").
*   Direct API integrations to publish to WordPress, YouTube, or podcast hosts.
