# 🎙️ Podcast Producer Agent: Agentic Post-Production Suite

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Inference Engine](https://img.shields.io/badge/LLM-Groq%20Cloud-f55a42.svg)](https://groq.com/)
[![Database](https://img.shields.io/badge/database-MongoDB%20Atlas-47A248.svg)](https://www.mongodb.com/)
[![Audio Engine](https://img.shields.io/badge/audio-Pydub%20%2F%20FFmpeg-lightgrey.svg)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An automated, hyper-optimized **AI-powered podcast post-production suite** designed to transform raw audio into an exhaustive list of studio-grade, distribution-ready media assets in seconds. 

By orchestrating specialized AI agents running on the ultra-low-latency **Groq Cloud API** and leveraging local audio signal processing via **FFmpeg/Pydub**, this application automates the tedious, multi-hour workflow of cleaning audio, transcribing conversations, and generating show notes, summaries, social media posts, and interactive analytics.

---

## 📖 Table of Contents
1. [Project Overview & Vision](#-project-overview--vision)
2. [The Problem It Solves](#-the-problem-it-solves)
3. [Key Features & Functionalities](#-key-features--functionalities)
4. [Internal Workings & Feature Deep Dive](#-internal-workings--feature-deep-dive)
5. [Technical Architecture & Workflow](#-technical-architecture--workflow)
6. [Complete Technology Stack](#-complete-technology-stack)
7. [Directory & Folder Structure](#-directory--folder-structure)
8. [Installation & Setup Instructions](#-installation--setup-instructions)
9. [Environment Variables & Configuration](#-environment-variables--configuration)
10. [Usage Guide](#-usage-guide)
11. [Screenshots](#-screenshots)
12. [Docker & Production Deployment](#-docker--production-deployment)
13. [Performance Optimizations](#-performance-optimizations)
14. [Security Considerations](#-security-considerations)
15. [Future Enhancements](#-future-enhancements)
16. [Contribution Guidelines](#-contribution-guidelines)
17. [License Information](#-license-information)

---

## 🌟 Project Overview & Vision

The **Podcast Producer Agent** is not just an API wrapper; it is an intelligent, reactive post-production workspace. 

Its design philosophy centers on **Human-in-the-Loop AI Collaboration**. The system runs the heavy lifting asynchronously, populates a stunning, dark-mode dashboard with highly structured assets, and allows creators to review, edit, and fine-tune every generated field before exporting. 

With an built-in continuous synchronization engine, it automatically backs up the active workspace state to a cloud-based **MongoDB Atlas** database, enabling seamless collaboration, persistence across browser crashes, and one-click historical restoration.

### Why This Project is Unique
* **Two-Stage Diarization Pipeline:** Unlike standard Whisper transcriptions that produce a continuous block of text, this agent runs a secondary LLaMA-based "Conversation Architect" refinery. It automatically reconstructs paragraph structures, identifies speaker changes, labels conversational roles, corrects phonetic anomalies, and injects semantic timestamps.
* **Studio-Grade DSP Pipeline:** Integrates a physical audio engineering channel strip locally. It performs silence-gating, high-pass filtering (80Hz rumble removal), low-pass filtering (12kHz hiss attenuation), dynamic range compression (balancing speakers), and LUFS-standardized volume normalization.
* **Stunning High-Fidelity UI:** Features custom CSS injects, dark-mode optimization, responsive tab interfaces, and a high-fidelity animated splash screen that plays during heavy system startup initialization.
* **Robust Multi-Format Exporter:** Synthesizes markdown, JSON, raw text, and generates dynamic PDF reports using ReportLab with custom page sizes, headings, and margins. All assets, along with the processed high-quality audio, are bundled into a single ZIP file.

---

## 🎯 The Problem It Solves

For content creators, podcasters, and marketing teams, post-production is a bottleneck:
1. **Manual Audio Editing:** Trimming dead space, normalization, and hiss removal requires dedicated Digital Audio Workstation (DAW) software and technical audio engineering skills.
2. **Transcription Bottlenecks:** Speech-to-text tools are either highly expensive, inaccurate, or fail to differentiate who is speaking (lacking speaker segmentation).
3. **Content Repurposing Fatigue:** Writing different promotional copy for LinkedIn, X (Twitter), Instagram, and YouTube descriptions takes hours of copywriting for a single episode.
4. **SEO Neglect:** Creators lose organic search discoverability because extracting rich metadata (optimized titles, keywords, hashtags, and description hooks) is an afterthought.
5. **State Loss & Fragmented Workflows:** Juggling between transcription files, text documents, audio editors, and cloud drives leads to a chaotic production environment.

The Podcast Producer Agent consolidates these fragmented pipelines into a single, unified, local-first cockpit that runs the entire pipeline in **under 30 seconds** for a standard episode.

---

## 🛠️ Key Features & Functionalities

* **📤 Upload & High-Fidelity Preprocessing:** Accepts major audio containers (`.mp3`, `.wav`, `.m4a`, `.aac`). Displays live playback of original and cleaned files side-by-side with compression metrics (e.g. original duration, cleaned duration, time saved, silence removed percentage).
* **📝 Two-Stage Refined Transcription:** Renders high-accuracy transcription under 5 seconds using Whisper Large V3 over Groq, and automatically restructures speaker dialogue into a clean professional format. Features a toggle between a reader view and an inline editor.
* **💡 Multi-Metric Title Selection:** Generates 5 compelling, SEO-friendly titles. Renders live visual metrics showcasing a **Catchiness Score (1-10)** and an **SEO Score (1-10)** dynamically computed by a specialized LLM agent.
* **📋 Structuring & Summarization:** Extracts a multi-layered summary featuring:
  * **The Hook:** A highly engaging, single-sentence click-magnet.
  * **Short Description:** A concise 50-word catalog description.
  * **Executive Summary:** A comprehensive 150-word overview of the episode's narrative arc.
* **📋 Smart Show Notes & Highlights:** Formulates beautifully categorized timestamps, chapter markers, a list of resources/links mentioned, top 5 viral-ready quotes, and actionable insights.
* **📱 Multi-Platform Social Media Suite:** Automatically structures posts tailored to individual social network formats:
  * **LinkedIn:** A professional summary highlighting key career or business lessons.
  * **X (Twitter):** An engaging 5-tweet micro-thread designed to maximize reach.
  * **Instagram:** A vibrant caption rich in emojis and visual cues.
  * **YouTube:** An SEO-optimized video description complete with automated chapters.
* **📊 Visual Transcript Analytics:** Built-in semantic metrics including:
  * An automated matplotlib-rendered **Word Cloud** highlighting the core themes.
  * A custom keyword frequency chart mapping the **Top 10 Topic Keywords**.
  * A dynamic bar chart rendering **Speaker Participation** (calculating word count shares per speaker).
  * Standard indicators for word count, character count, and estimated reading time.
* **📚 MongoDB Cloud Project Library:** An in-app catalog of all past processed episodes. Creators can browse histories, inspect transcript snippets, restore historical projects back to the active workspaces with a single click, or delete records.

---

## 🔍 Internal Workings & Feature Deep Dive

### 1. The Audio Cleanup DSP Pipeline (`utils/audio_cleaner.py`)
This module bypasses heavy graphic interfaces, executing a series of digital signal processing (DSP) steps in Python using Pydub:

```python
# Convert to mono to reduce bandwidth and streamline speech processing
audio = audio.set_channels(1)

# Remove subsonic hum and microphone rumble below 80Hz
audio = pydub_effects.high_pass_filter(audio, cutoff=80)

# Soften high-frequency tape hiss or electrical static above 12,000Hz
audio = pydub_effects.low_pass_filter(audio, cutoff=12000)

# Silence Gate: Split audio on pauses, removing sections below threshold
chunks = split_on_silence(
    audio,
    min_silence_len=min_silence_len, # standard 1.5s
    silence_thresh=silence_thresh,   # standard -50 dBFS
    keep_silence=300                 # natural padding (300ms) to prevent robotic cutoffs
)
```
Following silence removal, a dynamic range compressor evens out the audio level between loud and quiet voices (applying a `4:1` compression ratio above `-20dBFS`), and normalizes the master output to `-16.0 dBFS` (the broadcast standard for modern podcast platforms).

### 2. The Two-Stage Agentic Transcription (`agents/transcription_agent.py`)
Standard API transcription engines often misspell technical vocabulary, miss speaker transitions, and drop formatting. The transcription agent utilizes a **two-stage pipeline**:

```
+------------------+     Whisper Large V3     +----------------------+
| Raw Audio Upload | -----------------------> | Raw Unstructured TXT |
+------------------+                          +----------------------+
                                                         |
                                                         v
+------------------+     LLaMA-3.3-70B API    +----------------------+
| Final Workspace  | <----------------------- |  Agentic Refinery    |
+------------------+    - Dialog Formatting   +----------------------+
                        - Timestamps & Labels
```

1. **Stage 1 (Transcription):** Sends the cleaned audio block directly to Groq's specialized `whisper-large-v3` API endpoint, resulting in high-speed, verbatim text output.
2. **Stage 2 (Refinement):** Takes the raw string and forwards it to `llama-3.3-70b-versatile` with custom instructions. The LLM identifies semantic transitions, groups paragraphs by speaker context, handles dialogue attribution, and corrects transcription anomalies.

### 3. Continuous Cloud Sync & Autosave Engine (`app.py`)
To prevent session loss, `app.py` continuously runs an active state comparison check. 
Whenever an asset value (like a modified transcription or title selection) changes in the Streamlit session state:
1. It gathers the current state fields.
2. Performs a cryptographic check (compares sorted JSON string hashes of the current session state against the `last_saved_data`).
3. If a difference is detected, it asynchronously ships a sanitized clone of the payload to MongoDB Atlas via PyMongo.
4. Renders a modern green `☁️ Saved to Cloud` synchronization indicator in the header.

---

## 📐 Technical Architecture & Workflow

The following flowchart outlines the end-to-end data pipeline from audio upload to physical package distribution:

```mermaid
graph TD
    A[Raw Audio File] --> B[audio_cleaner.py - Pydub DSP]
    B -->|High/Low-Pass, Compress, Normalise| C[Cleaned Audio MP3]
    C --> D[transcription_agent.py - Whisper V3]
    D -->|Raw Verbatim Text| E[Agentic Refinery - LLaMA 70B]
    E -->|Structured Dialogue with Speakers| F[Central Transcript Workspace]
    
    F --> G1[Title Agent]
    F --> G2[Summary Agent]
    F --> G3[Show Notes Agent]
    F --> G4[Highlight Agent]
    F --> G5[Social Media & SEO Agent]
    F --> G6[Analytics Engine]
    
    G1 & G2 & G3 & G4 & G5 --> H[Streamlit UI Dashboard & Editor]
    G6 -->|Matplotlib WordCloud & Keyword Chart| H
    
    H -->|Autosave Check| I[PyMongo DB Handler]
    I -->|Async Push| J[(MongoDB Atlas Cloud)]
    
    H -->|Human-in-the-Loop Review| K[exporters.py]
    K -->|Compile PDF, Markdown, JSON, Cleaned Audio| L[podcast_package.zip]
    L --> M[Downloadable Archive]
```

---

## 💻 Complete Technology Stack

### Frontend & UI
* **[Streamlit](https://streamlit.io/):** Used to construct the high-interactivity dashboard, sidebars, sliders, and progress loading panels.
* **CSS Custom Injectors:** Embedded glassmorphic design system tokens, responsive navigation overrides, glowing card styling, and animated preloading elements.

### AI Engine (Large Language Models)
* **[Groq Cloud Python API](https://groq.com/):** High-speed API interface used for sub-second text completions.
* **LLaMA-3.3-70B-Versatile:** Selected for advanced logical reasoning, zero-shot structured JSON formatting, and linguistic refinement.
* **Whisper Large V3:** Industry-standard speech-to-text neural network used for robust multi-lingual transcription.

### Digital Signal Processing (DSP)
* **[Pydub](https://github.com/jiaaro/pydub):** Audio segment utility for Python. Used to interface with the audio file structures.
* **FFmpeg:** Underlying compiled binary library handling heavy operations (mono downsampling, sample rate conversion, dynamic amplitude scaling).

### Storage & Serialization
* **[MongoDB Atlas](https://www.mongodb.com/cloud/atlas):** Managed cloud document database storing operational data collections.
* **PyMongo:** Stable database connector with configured connection pooling and strict connection timeouts.

### Exporting & Reporting
* **[ReportLab](https://www.reportlab.com/):** Python PDF Generation library. Used to programmatically compile vector documents containing custom text flows, cover pages, and grid layouts.
* **Python Zipfile:** standard framework library executing file serialization and compressed archive packaging.

---

## 📁 Directory & Folder Structure

Below is the directory architecture for the **Podcast Producer Agent** project:

```text
podcast_producer_agent/
├── .streamlit/
│   └── config.toml         # Streamlit UI configuration (themes, port bindings)
├── agents/
│   ├── __init__.py
│   ├── highlight_agent.py  # Extracts top quotes and structures chapter timestamps
│   ├── llm_helper.py       # Core wrapper for raw and JSON-structured Groq completions
│   ├── seo_agent.py        # Generates SEO tags, hashtags, and description copy
│   ├── show_notes_agent.py # Builds introduction, bullet points, and resource logs
│   ├── social_media_agent.py# Generates copy for LinkedIn, X threads, Instagram, and YouTube
│   ├── summary_agent.py    # Formulates episode hooks, descriptions, and executive summaries
│   ├── title_agent.py      # Produces 5 titles with calculated catchiness & SEO scores
│   └── transcription_agent.py# Orchestrates Whisper transcribing and LLaMA diarization
├── utils/
│   ├── __init__.py
│   ├── analytics.py        # Tokenizer, stop-word filter, matplotlib and WordCloud renderer
│   ├── audio_cleaner.py    # Multi-stage audio cleaner, silence-gating, and normalizer
│   ├── db.py               # MongoDB Atlas connection manager (insert, fetch, delete)
│   ├── exporters.py        # reportlab PDF layout generator, markdown, JSON, and ZIP serializing
│   └── helpers.py          # Setup of temp directories (uploads/outputs) and cleanup utilities
├── uploads/                # Temporary landing directory for raw uploaded audio files
├── outputs/                # Temporary target directory for clean audio MP3s
├── reports/                # Build directory for PDF, MD, TXT, JSON and ZIP packages
├── assets/                 # Brand assets, static images, and documentation resources
├── Dockerfile              # Production-grade multi-stage container construction recipe
├── requirements.txt        # Frozen third-party library dependencies file
├── packages.txt            # System dependencies for Streamlit Cloud deployments (installs ffmpeg)
├── runtime.txt             # Python runtime version lockfile (python-3.11)
├── .env                    # Active local environment variables file (git-ignored)
├── .gitignore              # standard file exclusion definitions
├── app.py                  # Main entry point, splash screen, layout builder, and autosave loop
└── README.md               # Extremely comprehensive, high-fidelity project documentation
```

---

## ⚙️ Installation & Setup Instructions

### System Prerequisites
To run this application locally, your system must have **FFmpeg** installed and accessible in the system path. Pydub relies on FFmpeg to convert, read, and write compressed audio codecs.

#### Installation of FFmpeg:
* **macOS (via Homebrew):**
  ```bash
  brew install ffmpeg
  ```
* **Ubuntu/Linux:**
  ```bash
  sudo apt update
  sudo apt install -y ffmpeg
  ```
* **Windows (via winget or manual path installation):**
  ```powershell
  winget install Gyan.FFmpeg
  ```
  *(Verify installation by executing `ffmpeg -version` in your terminal)*

---

### Step-by-Step Local Deployment

#### 1. Clone the Codebase
```bash
git clone https://github.com/yourusername/podcast_producer_agent.git
cd podcast_producer_agent
```

#### 2. Initialize a Python Virtual Environment
It is highly recommended to isolate dependencies inside a virtual environment using Python 3.11+:
```bash
# Create the environment
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows (Command Prompt):
venv\Scripts\activate.bat

# Activate on Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

#### 3. Install Required Dependencies
Installs Streamlit, PyMongo, Groq client, Pydub, and visualization engines:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Configure Local Environment Variables
Create a new file named `.env` in the root directory (based on `.env.example` if available, or simply create it manually) and add your connection keys:
```env
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=your_mongodb_atlas_connection_string_here
```
*(Refer to the [Environment Variables & Configuration](#-environment-variables--configuration) section for full configuration keys details)*

#### 5. Launch the Application
Run the Streamlit server locally:
```bash
streamlit run app.py
```
The application will automatically initialize and launch in your default web browser at `http://localhost:8501`.

---

## 🔑 Environment Variables & Configuration

Below are the environment configuration parameters loaded by the system at runtime:

| Variable Name | Type | Required | Description | Example / Fallback |
| :--- | :--- | :--- | :--- | :--- |
| `GROQ_API_KEY` | String | **Yes** | Your API key to authenticate with Groq Cloud for sub-second LLaMA and Whisper inference. | `gsk_your_key_here` |
| `MONGO_URI` | String | No | Connection string for MongoDB Atlas cloud data persistence. If empty, sync features fail gracefully. | `mongodb+srv://user:pass@cluster.mongodb.net/...` |

### Streamlit Custom Styling Override (`.streamlit/config.toml`)
To enforce high-fidelity appearance styles, verify the config contains parameters similar to:
```toml
[theme]
primaryColor = "#3B82F6"
backgroundColor = "#0B0E14"
secondaryBackgroundColor = "#151A25"
textColor = "#F8FAFC"
font = "sans serif"
```

---

## 📖 Usage Guide

Executing your first post-production run is straightforward. Follow the workflow below:

```
[ Step 1: Config UI ] ---> [ Step 2: Upload Audio ] ---> [ Step 3: Run DSP/AI Pipeline ]
                                                                      |
                                                                      v
[ Step 6: Export Package ] <--- [ Step 5: Visual Analytics ] <--- [ Step 4: Human Review & Edit ]
```

### Step 1: Open the Sidebar Configurations
* Open your browser to `http://localhost:8501`.
* In the sidebar, select your preferred LLaMA engine model (Default: `llama-3.3-70b-versatile` for high-fidelity reasoning).
* Adjust the **Silence Threshold (dBFS)** and **Minimum Silence Length (ms)** sliders depending on your audio quality. Lower silence thresholds (e.g. `-55dB`) prevent cutting quiet speakers, while higher parameters (e.g. `-40dB`) trim aggressive gaps.
* Alternatively, if you do not have an audio file ready, click the **🚀 Load Demo Project** button. This instantly populates the active session workspace with pre-transcribed, studio-grade conversation data to demonstrate analytics, editors, and exporters immediately.

### Step 2: Upload and Process Audio
* Navigate to the **📤 Upload & Process** tab.
* Name your project or episode (e.g., *“EP 42: The Future of Quantum Banking”*).
* Drag and drop your audio file (`.mp3`, `.wav`, `.m4a`, etc.) into the blue dashed file container.
* Click the **Process Audio Pipeline** button. The system displays a live 7-step progress pipeline showing which agent is currently active.

### Step 3: Human-in-the-Loop Verification & Review
Once processing finishes, click through the dynamic tab interface:
* **📝 Transcript:** Toggle to **Editor Mode** to modify grammar, fix typos, or add speaker names. Changes are saved dynamically.
* **💡 Titles & Summary:** Choose the most engaging title. Review the calculated Catchiness and SEO scores. Customize the executive summary, description, and hook text blocks.
* **📋 Show Notes & Highlights:** Inspect generated outlines, key resources, chapters, and viral quotes. The raw JSON structure is fully editable in-app.
* **📱 Social & SEO:** Copy the formatted posts directly for X/LinkedIn. Add or remove custom SEO keywords and meta descriptions.

### Step 4: Analytics Inspection
* Go to the **📊 Analytics** tab to inspect visualization charts, read statistics, and check speaker share ratios. Matplotlib-generated word clouds and topic charts display core conversational topics instantly.

### Step 5: Bulk Export
* Navigate to the **📦 Export** tab.
* Click **Generate Export Package**. The system programmatically generates:
  * A professional multi-page vector **PDF report** via ReportLab.
  * A structured **Markdown file** suitable for website publishing.
  * A portable **JSON document** holding all metadata.
  * The cleaned, compressed **Audio MP3 file**.
* Click the **Download ZIP Package** button to pull down a comprehensive zip bundle containing all assets.

---

## 📸 Screenshots

| Feature Section | Screenshot Description / Mock Placement | Layout Component |
| :--- | :--- | :--- |
| **Splash Screen Loader** | High-fidelity animated neon blue/purple loading panel featuring a pulsing microphone icon and a dynamic progressive loading bar. | `[ Splash Screen Preloader ]` |
| **Processing Control Panel** | Clean file uploader area with custom drag-and-drop borders and a sequential, multi-step progress bar showing live agent processing updates. | `[ 📤 Upload & Process Tab ]` |
| **Interactive Editor Workspace** | Dual-mode dialogue view showing professional transcript text blocks side-by-side with interactive JSON edit cards and selector metrics. | `[ 📝 Transcript & Editor Tab ]` |
| **Analytics Dashboard** | Side-by-side grid rendering a vibrant high-density WordCloud and a clean Matplotlib bar chart plotting word occurrences and speaker participations. | `[ 📊 Transcript Analytics Tab ]` |

---

## 🐳 Docker & Production Deployment

### Docker Setup
The suite is containerized to ensure consistent execution regardless of host system configuration. The `Dockerfile` implements a clean layer build:

#### 1. Build the Docker Image
```bash
docker build -t podcast-agent .
```

#### 2. Run the Container
Pass your system environment API keys directly at runtime:
```bash
docker run -p 8501:8501 \
  -e GROQ_API_KEY="your_groq_key" \
  -e MONGO_URI="mongodb+srv://..." \
  podcast-agent
```
The application will be accessible at `http://localhost:8501` inside your local docker network host.

---

### Streamlit Cloud Production Deployment
If deploying to the public **Streamlit Community Cloud** hosting platform, ensure the following files exist in the repository root to automatically resolve host requirements:
1. **`requirements.txt`:** Locked library definitions.
2. **`packages.txt`:** Installs binary system libraries (specifically lists `ffmpeg` so the OS container can run audio conversion).
3. **`runtime.txt`:** Locks the execution instance to `python-3.11`.
4. **Secrets Manager:** Add your `GROQ_API_KEY` and `MONGO_URI` directly inside the Streamlit Cloud dashboard under *Settings > Secrets* in standard TOML format:
   ```toml
   GROQ_API_KEY = "your_key_here"
   MONGO_URI = "mongodb+srv://..."
   ```

---

## ⚡ Performance Optimizations

* **Instant-Render Splash Screen:** Streamlit by default executes all imports on application load, causing a 5-10 second blank screen block. This project bypasses this behavior by performing a **Fast Render Splash Screen** before executing any libraries imports. Creators are met with an immediate animated splash screen loading bar, dramatically improving perceived responsiveness.
* **Downsampled Mono Conversion:** Upon uploading, files are converted from multi-channel stereo configurations to a single mono track. This halves the audio payload size, speeds up processing, and optimizes the file structure for Whisper transcription.
* **Sub-Second Groq Completions:** The LLM engine relies on Groq LLaMA endpoints rather than local pipelines. This results in standard completion times of **~0.3s for short text** and **under 3.0s for massive transcripts**, providing instant updates to the user.
* **Smart Connection Pooling & Expiry Timeouts:** PyMongo client configurations strictly restrict MongoDB network connection attempts to a maximum `5000ms` timeout (`serverSelectionTimeoutMS`, `connectTimeoutMS`, `socketTimeoutMS`). This prevents app lockups or frozen tabs in poor network environments.

---

## 🔒 Security Considerations

* **API Keys Protection:** Environment variables are strictly parsed using `python-dotenv`. Credentials should never be hardcoded into the source files. The project contains a predefined `.gitignore` to prevent pushing `.env` files to remote repositories.
* **Path Traversal Shielding:** File upload pathways use strict directory mappings (`uploads/`, `outputs/`, `reports/`) and use clean file extensions to prevent execution vulnerabilities or script injections.
* **MongoDB TLS Configuration:** PyMongo connections enforce secure SSL/TLS handshakes (`tls=True`), preventing intermediate packet sniffing or payload manipulation over unsecured networks.
* **Temporary Space Sanitization:** A manual **Clean Up Temp Files** button is exposed in the sidebar layout. Creators can wipe physical assets from local disks (`uploads/`, `outputs/`, `reports/`) instantly to protect proprietary content and reclaim disk space.

---

## 🚀 Future Enhancements

* 🎙️ **Deep Speaker Diarization:** Implement advanced speaker embedding extraction (using models like PyAnnote) to automatically map names to real speaker voices based on vocal frequencies instead of semantic contexts.
* 📦 **Direct Publishing APIs:** Build integrations to upload final media assets and audio directly to podcast hosting providers (e.g. Spotify for Podcasters, Buzzsprout), content management systems (e.g. WordPress, Webflow), or social channels via official webhooks.
* 🌐 **Local Offline Processing Option:** Add support for running local `faster-whisper` and small open-source LLMs (via Ollama) to allow completely disconnected, private post-production pipelines.

---

## 🤝 Contribution Guidelines

We welcome contributions from the developer and creator community! To contribute:
1. **Fork the Repository** to your personal GitHub account.
2. **Create a Feature Branch** explaining the changes:
   ```bash
   git checkout -b feature/audio-noise-reduction
   ```
3. **Commit your changes** with clear, descriptive messages:
   ```bash
   git commit -m "feat: integrate dynamic noise gate filters using spectral gating"
   ```
4. **Ensure Coding Standards** are met:
   * Keep functions isolated and clean.
   * Write comprehensive docstrings for new utility helper files.
   * Ensure compatibility with the Streamlit Cloud environment schema.
5. **Open a Pull Request** against the `main` branch. Provide detailed explanations, test runs, and snapshots if applicable.

---

## 📄 License Information

This project is licensed under the **MIT License**. You are free to modify, distribute, and integrate this software into proprietary workflows, provided the original copyright and license notice are retained. See the [LICENSE](LICENSE) file for complete details.

---

*Developed with 💙 by the Podcast Producer Agent Team. Transform your raw audio into viral digital assets today!*
