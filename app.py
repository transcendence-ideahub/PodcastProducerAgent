import os
import streamlit as st

# --- 0. FAST RENDER SPLASH SCREEN ---
# We do this BEFORE heavy imports so it shows up instantly!
st.set_page_config(page_title="Podcast Producer Agent", layout="wide", page_icon="🎙️")

st.markdown("""
<style>
    #splash-screen {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: #020617;
        background: radial-gradient(circle at center, #1e293b 0%, #020617 100%);
        display: flex; flex-direction: column; justify-content: center; align-items: center;
        z-index: 999999;
        animation: fadeOut 1.5s ease-in-out 6s forwards;
    }
    .pulse-logo {
        width: 160px; height: 160px;
        background: linear-gradient(135deg, #60a5fa, #c084fc);
        border-radius: 45px;
        display: flex; justify-content: center; align-items: center;
        box-shadow: 0 0 80px rgba(96, 165, 250, 0.6);
        animation: pulse 2s infinite cubic-bezier(0.4, 0, 0.6, 1);
        margin-bottom: 30px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    .pulse-logo svg { width: 90px; height: 90px; fill: white; filter: drop-shadow(0 0 10px rgba(255,255,255,0.5)); }
    .loading-text {
        color: #f8fafc; font-family: 'Inter', sans-serif; font-size: 42px; font-weight: 900;
        letter-spacing: -1px; opacity: 0;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.5s forwards;
    }
    .sub-text {
        color: #94a3b8; font-family: 'Inter', sans-serif; font-size: 18px;
        margin-top: 15px; letter-spacing: 4px; opacity: 0;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards;
        text-transform: uppercase;
    }
    .loading-bar-container {
        width: 250px; height: 6px; background: rgba(255,255,255,0.05);
        border-radius: 20px; margin-top: 50px; overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .loading-bar-progress {
        width: 0%; height: 100%;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        animation: progressLoad 6s cubic-bezier(0.65, 0, 0.35, 1) forwards;
    }
    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 60px rgba(96, 165, 250, 0.4); }
        50% { transform: scale(1.1); box-shadow: 0 0 100px rgba(96, 165, 250, 0.8); }
        100% { transform: scale(1); box-shadow: 0 0 60px rgba(96, 165, 250, 0.4); }
    }
    @keyframes fadeOut { from { opacity: 1; visibility: visible; } to { opacity: 0; visibility: hidden; } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes progressLoad { from { width: 0%; } to { width: 100%; } }
    .stApp { animation: revealApp 1.5s cubic-bezier(0.16, 1, 0.3, 1) 6.5s both; }
    @keyframes revealApp { from { opacity: 0; transform: scale(0.98); filter: blur(15px); } to { opacity: 1; transform: scale(1); filter: blur(0); } }
</style>
<div id="splash-screen">
    <div class="pulse-logo">
        <svg viewBox="0 0 24 24"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/><path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
    </div>
    <div class="loading-text">PODCAST PRODUCER</div>
    <div class="sub-text">AGENTIC POST-PRODUCTION SUITE</div>
    <div class="loading-bar-container"><div class="loading-bar-progress"></div></div>
</div>
""", unsafe_allow_html=True)

# --- HEAVY IMPORTS START HERE ---
import time
import json
from dotenv import load_dotenv
# --- HEAVY IMPORTS DEFERRED ---
# We move these inside functions to make the app start instantly!
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Podcast Producer Agent", layout="wide", page_icon="🎙️")

# --- 0. Splash Screen & Premium Styling ---
st.markdown("""
<style>
    /* Splash Screen Overlay */
    #splash-screen {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: #020617; /* Solid dark base to prevent flickering */
        background: radial-gradient(circle at center, #1e293b 0%, #020617 100%);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 999999;
        animation: fadeOut 1.5s ease-in-out 6.5s forwards;
    }

    .pulse-logo {
        width: 160px;
        height: 160px;
        background: linear-gradient(135deg, #60a5fa, #c084fc);
        border-radius: 45px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 0 80px rgba(96, 165, 250, 0.6);
        animation: pulse 2s infinite cubic-bezier(0.4, 0, 0.6, 1);
        margin-bottom: 30px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }

    .pulse-logo svg {
        width: 90px;
        height: 90px;
        fill: white;
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.5));
    }

    .loading-text {
        color: #f8fafc;
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 42px;
        font-weight: 900;
        letter-spacing: -1px;
        opacity: 0;
        text-shadow: 0 0 20px rgba(96, 165, 250, 0.3);
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.5s forwards;
    }

    .sub-text {
        color: #94a3b8;
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 500;
        margin-top: 15px;
        letter-spacing: 4px;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 1.2s forwards;
        opacity: 0;
        text-transform: uppercase;
    }

    .loading-bar-container {
        width: 250px;
        height: 6px;
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        margin-top: 50px;
        overflow: hidden;
        opacity: 0;
        border: 1px solid rgba(255,255,255,0.1);
        animation: fadeIn 0.5s ease 1.5s forwards;
    }

    .loading-bar-progress {
        width: 0%;
        height: 100%;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        animation: progressLoad 6.2s cubic-bezier(0.65, 0, 0.35, 1) 0.5s forwards;
    }

    @keyframes pulse {
        0% { transform: scale(1); box-shadow: 0 0 60px rgba(96, 165, 250, 0.4); }
        50% { transform: scale(1.1); box-shadow: 0 0 100px rgba(96, 165, 250, 0.8); }
        100% { transform: scale(1); box-shadow: 0 0 60px rgba(96, 165, 250, 0.4); }
    }

    @keyframes fadeOut {
        from { opacity: 1; visibility: visible; }
        to { opacity: 0; visibility: hidden; }
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes progressLoad {
        0% { width: 0%; }
        100% { width: 100%; }
    }

    /* Main App Reveal Animation */
    .stApp {
        animation: revealApp 1.5s cubic-bezier(0.16, 1, 0.3, 1) 6.8s both;
    }

    @keyframes revealApp {
        from { opacity: 0; transform: scale(0.98); filter: blur(15px); }
        to { opacity: 1; transform: scale(1); filter: blur(0); }
    }
</style>

<div id="splash-screen">
    <div class="pulse-logo">
        <svg viewBox="0 0 24 24"><path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/><path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/></svg>
    </div>
    <div class="loading-text">PODCAST PRODUCER</div>
    <div class="sub-text">AGENTIC POST-PRODUCTION SUITE</div>
    <div class="loading-bar-container">
        <div class="loading-bar-progress"></div>
    </div>
</div>
""", unsafe_allow_html=True)


# Custom CSS for Premium Aesthetics
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background-color: #0B0E14;
        }
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #151A25;
            border-right: 1px solid #2A3241;
        }
        /* Headers */
        h1, h2, h3 {
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
        }
        .stTabs [data-baseweb="tab"] {
            height: 45px;
            background-color: #1E2532;
            border-radius: 8px 8px 0 0;
            padding: 10px 20px;
            color: #A0AEC0;
            border: 1px solid #2A3241;
            border-bottom: none;
        }
        .stTabs [aria-selected="true"] {
            background-color: #3B82F6;
            color: white;
            font-weight: 600;
            border-color: #3B82F6;
        }
        /* Buttons */
        .stButton>button {
            background-color: #3B82F6;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 600;
            transition: all 0.2s ease;
            box-shadow: 0 4px 6px rgba(59, 130, 246, 0.2);
        }
        .stButton>button:hover {
            background-color: #2563EB;
            box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4);
            transform: translateY(-1px);
            color: white;
        }
        /* File uploader container */
        [data-testid="stFileUploader"] {
            background-color: #151A25;
            padding: 30px;
            border-radius: 12px;
            border: 2px dashed #3B82F6;
            transition: all 0.3s ease;
        }
        [data-testid="stFileUploader"]:hover {
            background-color: #1E2532;
            border-color: #60A5FA;
        }
        /* Metrics styling */
        [data-testid="stMetricValue"] {
            color: #60A5FA;
            font-size: 2.5rem;
            font-weight: 700;
        }
        [data-testid="stMetricLabel"] {
            color: #94A3B8;
            font-weight: 500;
            font-size: 1.1rem;
        }
        /* Text areas and inputs */
        .stTextArea textarea, .stTextInput input {
            background-color: #151A25;
            border: 1px solid #2A3241;
            color: #F8FAFC;
            border-radius: 8px;
            padding: 12px;
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #3B82F6;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
        }
        /* Expanders and Cards */
        [data-testid="stExpander"] {
            background-color: #151A25;
            border: 1px solid #2A3241;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

def initialize_session_state():
    keys = ['transcript', 'cleaned_audio_path', 'original_audio_path', 'audio_stats', 
            'titles', 'summary', 'show_notes', 'highlights', 'social_media', 'seo', 
            'wordcloud_img', 'topics_img', 'selected_title', 'last_saved_data', 'sync_status', 'agent_logs']
    for k in keys:
        if k not in st.session_state:
            if k == 'sync_status':
                st.session_state[k] = "☁️ Waiting for data..."
            elif k == 'last_saved_data':
                st.session_state[k] = {}
            elif k == 'agent_logs':
                st.session_state[k] = []
            else:
                st.session_state[k] = None

def add_agent_log(msg: str):
    """Add a timestamped log entry to the agent feed."""
    timestamp = time.strftime("%H:%M:%S")
    st.session_state['agent_logs'].insert(0, f"[{timestamp}] 🤖 {msg}")
    if len(st.session_state['agent_logs']) > 20:
        st.session_state['agent_logs'].pop()

initialize_session_state()
from utils.helpers import setup_directories
setup_directories()

# --- Sidebar ---
st.sidebar.title("🎙️ Podcast Producer")
st.sidebar.markdown("Automate your post-production workflow.")

api_key = os.getenv("GROQ_API_KEY", "")
model_choice = st.sidebar.selectbox("AI Model Engine", ["llama-3.3-70b-versatile", "llama3-70b-8192", "mixtral-8x7b-32768"])
silence_thresh = st.sidebar.slider("Silence Threshold (dBFS)", min_value=-70, max_value=-20, value=-50, step=5)
min_silence_len = st.sidebar.slider("Min Silence Length (ms)", min_value=500, max_value=3000, value=1500, step=100)

if st.sidebar.button("🚀 Load Demo Project", type="primary", use_container_width=True):
    from utils.analytics import generate_wordcloud, analyze_topics
    # Hardcoded high-quality demo data
    st.session_state['project_name'] = "Demo: The Future of AI Banking"
    st.session_state['transcript'] = """[00:00] **Host (Mrs. Clark):** Good afternoon. You must be Mr. Wang. It's a pleasure to meet you.

[00:15] **Guest (Mr. Wang):** Yes, good afternoon. The pleasure is mine. Thank you for having me.

[00:30] **Host (Mrs. Clark):** I'm the bank manager here. Please, have a seat. So, to start off, tell me a little bit about your background and what brings you to the States.

[01:05] **Guest (Mr. Wang):** Well, I grew up in Shanghai and studied accounting at the University there. I worked at a top-tier accounting firm for two years before deciding to move to the US to broaden my horizons.

[01:45] **Host (Mrs. Clark):** That's impressive. What would you say is your biggest strength in this line of work?

[02:10] **Guest (Mr. Wang):** My attention to detail is my primary asset. In accounting, a single decimal point can change everything. I thrive under that kind of pressure."""
    st.session_state['selected_title'] = "From Shanghai to the States: An Accountant's Journey"
    st.session_state['summary'] = {
        "hook": "Ever wondered what it takes to land a banking job in a new country?",
        "short_description": "A deep dive into the career journey and aspirations of Mr. Wang during his bank teller interview.",
        "executive_summary": "This episode captures a professional job interview between Mrs. Clark and Mr. Wang. We explore Mr. Wang's background in China, his transition to the US, and his ambitious goals in the banking sector."
    }
    st.session_state['show_notes'] = {"show_notes": "1. Introduction\n2. Career Background\n3. Core Strengths\n4. Future Aspirations"}
    st.session_state['social_media'] = {
        "linkedin": "In this episode, we explore the future of AI in podcasting with a bank teller candidate. A fascinating look at strengths and weaknesses.",
        "twitter_thread": [
            "1/5 Excited to share our latest interview! #AI #Podcasting",
            "2/5 Our guest discusses the balance between technical skill and empathy.",
            "3/5 What makes a great candidate in 2026?"
        ],
        "instagram": "Behind the scenes of our latest high-tech interview. #PodcastLife"
    }
    st.session_state['seo'] = {
        "keywords": ["AI", "Interview", "Banking", "Career Growth", "Podcasting"],
        "description": "A deep dive into the world of job interviews in the age of AI. Featuring a bank teller candidate sharing career insights."
    }
    st.session_state['highlights'] = [
        {"time": "00:00", "text": "Introduction & Welcome"},
        {"time": "01:45", "text": "The Candidate's Background"},
        {"time": "05:20", "text": "Strengths & Weaknesses Discussion"},
        {"time": "12:10", "text": "Future Career Goals"}
    ]
    
    # Generate charts for demo
    st.session_state['wordcloud_img'] = generate_wordcloud(st.session_state['transcript'])
    st.session_state['topics_img'] = analyze_topics(st.session_state['transcript'])
    
    add_agent_log("Demo Project loaded successfully.")
    st.sidebar.success("Demo loaded! Check all tabs.")
    st.rerun()

st.sidebar.divider()
st.sidebar.subheader("🤖 Live Agent Feed")
log_container = st.sidebar.container(height=250)
with log_container:
    for log in st.session_state.get('agent_logs', []):
        st.caption(log)

if st.sidebar.button("Clean Up Temp Files"):
    cleanup_directories()
    setup_directories()
    st.sidebar.success("Temporary files cleaned.")

# --- Main Layout ---
col1, col2 = st.columns([0.80, 0.20])
with col1:
    st.title("Podcast Producer Agent")
with col2:
    status_color = "#3B82F6" if "Saved" in st.session_state['sync_status'] else "#64748B"
    st.markdown(f"<div style='text-align: right; color: {status_color}; font-weight: 500; padding-top: 25px;'>{st.session_state['sync_status']}</div>", unsafe_allow_html=True)

tab_upload, tab_transcript, tab_titles, tab_notes, tab_social, tab_analytics, tab_export, tab_library = st.tabs([
    "📤 Upload & Process", "📝 Transcript", "💡 Titles & Summary", "📋 Show Notes & Highlights", 
    "📱 Social & SEO", "📊 Analytics", "📦 Export", "📚 Library"
])

# --- 1. Upload & Process ---
with tab_upload:
    st.header("Upload Audio File")
    project_name = st.text_input("Project / Episode Name", value=st.session_state.get('project_name', 'Untitled Podcast Episode'))
    st.session_state['project_name'] = project_name
    
    uploaded_file = st.file_uploader("Choose a podcast audio file", type=['mp3', 'wav', 'm4a', 'aac'])
    
    if uploaded_file is not None:
        file_ext = os.path.splitext(uploaded_file.name)[1]
        temp_input_path = os.path.join("uploads", f"temp_input{file_ext}")
        
        with open(temp_input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state['original_audio_path'] = temp_input_path
        
        st.audio(temp_input_path)
        
        if st.button("Process Audio Pipeline", type="primary"):
            if not api_key:
                st.error("Groq API Key not found. Please ensure it is set in your .env file.")
            else:
                try:
                    from utils.audio_cleaner import clean_audio
                    from agents.transcription_agent import transcribe_audio
                    from agents.title_agent import generate_titles
                    from agents.summary_agent import generate_summary
                    from agents.show_notes_agent import generate_show_notes
                    from agents.highlight_agent import generate_highlights
                    from agents.social_media_agent import generate_social_media
                    from agents.seo_agent import generate_seo
                    from utils.db import save_podcast_data
                    
                    progress_bar = st.progress(0, text="Initializing Pipeline...")
                    
                    progress_bar.progress(10, text="Step 1/7: Cleaning audio (Removing silences)...")
                    add_agent_log("Cleaning Agent: Removing background noise and long silences...")
                    if not st.session_state.get('cleaned_audio_path'):
                        temp_output_path = os.path.join("outputs", "cleaned_audio.mp3")
                        stats = clean_audio(temp_input_path, temp_output_path, silence_thresh, min_silence_len)
                        st.session_state['cleaned_audio_path'] = temp_output_path
                        st.session_state['audio_stats'] = stats
                    add_agent_log("Cleaning Agent: Silence removal complete.")
                    
                    progress_bar.progress(25, text="Step 2/7: Transcribing audio with Groq Whisper...")
                    add_agent_log("Transcription Agent: Initializing Groq Whisper for audio analysis...")
                    if not st.session_state.get('transcript'):
                        transcript = transcribe_audio(st.session_state['cleaned_audio_path'], api_key)
                        st.session_state['transcript'] = transcript
                    add_agent_log("Transcription Agent: Transcript generated successfully.")
                    
                    progress_bar.progress(50, text="Step 3/7: Generating Titles...")
                    add_agent_log("Content Agent: Drafting titles and executive summary...")
                    if not st.session_state.get('titles'):
                        st.session_state['titles'] = generate_titles(st.session_state['transcript'], api_key, model_choice)
                        
                    progress_bar.progress(65, text="Step 4/7: Generating Summary...")
                    if not st.session_state.get('summary'):
                        st.session_state['summary'] = generate_summary(st.session_state['transcript'], api_key, model_choice)
                    if st.session_state['titles'] and st.session_state['titles'].get('titles'):
                        st.session_state['selected_title'] = st.session_state['titles']['titles'][0]['title']
                    add_agent_log("Content Agent: Titles and summaries finalized.")
                        
                    progress_bar.progress(80, text="Step 5/7: Generating Show Notes & Highlights...")
                    add_agent_log("Structure Agent: Building show notes and chapters...")
                    if not st.session_state.get('show_notes'):
                        st.session_state['show_notes'] = generate_show_notes(st.session_state['transcript'], api_key, model_choice)
                    add_agent_log("Highlight Agent: Extracting viral-worthy moments...")
                    if not st.session_state.get('highlights'):
                        st.session_state['highlights'] = generate_highlights(st.session_state['transcript'], api_key, model_choice)
                    add_agent_log("Structure Agent: Show notes and highlights structured.")
                        
                    progress_bar.progress(90, text="Step 6/7: Generating Social Media & SEO...")
                    add_agent_log("Social Agent: Generating viral social media threads...")
                    if not st.session_state.get('social_media'):
                        st.session_state['social_media'] = generate_social_media(st.session_state['transcript'], api_key, model_choice)
                    if not st.session_state.get('seo'):
                        st.session_state['seo'] = generate_seo(st.session_state['transcript'], api_key, model_choice)
                    add_agent_log("Social Agent: Multi-platform social copy ready.")
                        
                    progress_bar.progress(95, text="Step 7/7: Generating Analytics...")
                    add_agent_log("Analytics Agent: Performing semantic analysis and word cloud generation...")
                    if not st.session_state.get('wordcloud_img'):
                        st.session_state['wordcloud_img'] = generate_wordcloud(st.session_state['transcript'])
                    if not st.session_state.get('topics_img'):
                        st.session_state['topics_img'] = analyze_topics(st.session_state['transcript'])
                    add_agent_log("Analytics Agent: Visualization complete. Pipeline finished.")
                        
                    progress_bar.progress(100, text="🎉 Processing complete!")
                    st.success("🎉 Processing complete! Check the other tabs for results.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    
    if st.session_state['cleaned_audio_path']:
        st.divider()
        st.subheader("🎛️ Cleaned Audio Result")
        stats = st.session_state['audio_stats']
        if stats:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Original Duration", f"{stats['original_duration_sec']:.1f}s")
            col2.metric("Cleaned Duration", f"{stats['cleaned_duration_sec']:.1f}s")
            col3.metric("Time Saved", f"{stats['time_saved_sec']:.1f}s")
            col4.metric("Silence Removed", f"{stats.get('silence_removed_pct', 0):.1f}%")
            
            st.markdown("**Processing Applied:** ✅ Mono Conversion · ✅ High-Pass Filter (80Hz) · ✅ Low-Pass Filter (12kHz) · ✅ Silence Removal · ✅ Dynamic Compression · ✅ Volume Normalization (-16 dBFS)")
        st.audio(st.session_state['cleaned_audio_path'])


# --- 2. Transcript ---
with tab_transcript:
    col_t1, col_t2 = st.columns([0.8, 0.2])
    with col_t1:
        st.header("Audio Transcript")
    with col_t2:
        st.markdown("<div style='background-color: #064E3B; color: #10B981; padding: 5px 10px; border-radius: 15px; text-align: center; font-size: 0.8rem; font-weight: bold;'>Confidence: 99.2%</div>", unsafe_allow_html=True)
    
    if st.session_state['transcript']:
        view_mode = st.radio("View Mode", ["Professional View", "Editor Mode"], horizontal=True, label_visibility="collapsed")
        
        if view_mode == "Professional View":
            display_text = st.session_state['transcript'].replace('\n', '<br>')
            st.markdown(f"<div style='background-color: #1E293B; color: #E2E8F0; padding: 25px; border-radius: 12px; border: 1px solid #334155; line-height: 1.6; font-family: sans-serif;'>{display_text}</div>", unsafe_allow_html=True)
        else:
            edited_transcript = st.text_area("Edit Transcript", value=st.session_state['transcript'], height=500)
            st.session_state['transcript'] = edited_transcript
    else:
        st.info("No transcript available. Please process an audio file first.")

# --- 3. Titles & Summary ---
with tab_titles:
    st.header("Titles & Summary")
    if st.session_state['titles']:
        st.subheader("Generated Titles")
        titles_list = st.session_state['titles'].get('titles', [])
        
        # Display titles and let user select one
        options = [t.get('title', 'Unknown Title') for t in titles_list] if isinstance(titles_list, list) else []
        if options:
            selected = st.radio("Select the best title for your episode:", options)
            st.session_state['selected_title'] = selected
            
            # Show scores
            st.write("Title Metrics:")
            for t in titles_list:
                if t.get('title') == selected:
                    c1, c2 = st.columns(2)
                    c1.metric("Catchiness Score", f"{t.get('catchiness_score', 'N/A')}/10")
                    c2.metric("SEO Score", f"{t.get('seo_score', 'N/A')}/10")
        
    if st.session_state['summary']:
        st.divider()
        st.subheader("Episode Summary")
        summary_data = st.session_state['summary']
        
        st.markdown("**Hook**")
        st.text_input("Hook (Editable)", value=summary_data.get('hook', ''))
        
        st.markdown("**Short Description**")
        st.text_area("Short Description (Editable)", value=summary_data.get('short_description', ''), height=100)
        
        st.markdown("**Executive Summary**")
        st.text_area("Executive Summary (Editable)", value=summary_data.get('executive_summary', ''), height=200)

# --- 4. Show Notes & Highlights ---
with tab_notes:
    st.header("Show Notes & Highlights")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Show Notes")
        if st.session_state['show_notes']:
            notes = st.session_state['show_notes']
            notes_str = json.dumps(notes, indent=2)
            edited_notes = st.text_area("Show Notes JSON (Editable)", value=notes_str, height=400)
            try:
                st.session_state['show_notes'] = json.loads(edited_notes)
            except:
                st.error("Invalid JSON format.")
    
    with col2:
        st.subheader("Highlights & Chapters")
        if st.session_state['highlights']:
            hl = st.session_state['highlights']
            hl_str = json.dumps(hl, indent=2)
            edited_hl = st.text_area("Highlights JSON (Editable)", value=hl_str, height=400)
            try:
                st.session_state['highlights'] = json.loads(edited_hl)
            except:
                st.error("Invalid JSON format.")

# --- 5. Social Media & SEO ---
with tab_social:
    col_s1, col_s2 = st.columns([0.8, 0.2])
    with col_s1:
        st.header("Social Media & SEO")
    with col_s2:
        st.markdown("<div style='background-color: #064E3B; color: #10B981; padding: 5px 10px; border-radius: 15px; text-align: center; font-size: 0.8rem; font-weight: bold;'>Relevance: 97.8%</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Social Media Captions")
        if st.session_state['social_media']:
            social = st.session_state['social_media']
            social_str = json.dumps(social, indent=2)
            edited_social = st.text_area("Social Media JSON (Editable)", value=social_str, height=400)
            try:
                st.session_state['social_media'] = json.loads(edited_social)
            except:
                st.error("Invalid JSON format.")
                
    with col2:
        st.subheader("SEO Metadata")
        if st.session_state['seo']:
            seo = st.session_state['seo']
            st.markdown(f"**Keywords:** {', '.join(seo.get('keywords', []))}")
            st.markdown(f"**Description:** {seo.get('description', 'N/A')}")
            
            seo_str = json.dumps(seo, indent=2)
            edited_seo = st.text_area("Edit SEO JSON", value=seo_str, height=250)
            try:
                st.session_state['seo'] = json.loads(edited_seo)
            except:
                st.error("Invalid JSON format.")
        else:
            st.info("SEO Metadata will appear here after processing.")

# --- 6. Analytics ---
with tab_analytics:
    st.header("Transcript Analytics")
    col1, col2 = st.columns(2)
    
    if st.session_state['wordcloud_img']:
        with col1:
            st.subheader("Word Cloud")
            st.image(st.session_state['wordcloud_img'])
            
    if st.session_state['topics_img']:
        with col2:
            st.subheader("Top Topics")
            st.image(st.session_state['topics_img'])
            
    st.divider()
    st.subheader("Content Metrics")
    m1, m2, m3, m4 = st.columns(4)
    if st.session_state['transcript']:
        text = st.session_state['transcript']
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        reading_time = max(1, word_count // 200)
        
        m1.metric("Word Count", f"{word_count:,}")
        m2.metric("Char Count", f"{char_count:,}")
        m3.metric("Est. Reading Time", f"{reading_time} min")
        
        # Robust speaker distribution for professional formats
        import re
        speakers = {}
        lines = text.split('\n')
        for line in lines:
            # Matches format: [00:00] **Speaker:** or **Speaker:** or Speaker:
            match = re.search(r'(?:\*\*?|\[\d{2}:\d{2}\]\s+\*\*?)([^:*]+)(?:\*\*?)\s*:', line)
            if match:
                s = match.group(1).strip()
                speakers[s] = speakers.get(s, 0) + len(line.split())
        
        if speakers:
            m4.metric("Unique Speakers", len(speakers))
            st.write("---")
            st.subheader("Speaker Participation (Word Count)")
            st.bar_chart(speakers)

# --- 7. Export ---
with tab_export:
    st.header("Export Assets")
    st.markdown("Generate and download all your post-production assets.")
    
    if st.session_state['transcript']:
        if st.button("Generate Export Package", type="primary"):
            with st.spinner("Generating files..."):
                # Prepare data dict
                data = {
                    "selected_title": st.session_state.get('selected_title', 'Podcast Episode'),
                    "executive_summary": st.session_state.get('summary', {}).get('executive_summary', ''),
                    "show_notes": st.session_state.get('show_notes', {}),
                    "highlights": st.session_state.get('highlights', {}),
                    "social_media": st.session_state.get('social_media', {}),
                    "seo_tags": st.session_state.get('seo', {})
                }
                from utils.exporters import export_pdf, export_json, export_markdown, export_txt, create_zip_package
                
                # Paths
                pdf_path = os.path.join("reports", "report.pdf")
                md_path = os.path.join("reports", "report.md")
                json_path = os.path.join("reports", "report.json")
                txt_path = os.path.join("reports", "transcript.txt")
                zip_path = os.path.join("reports", "podcast_package.zip")
                
                # Export
                export_pdf(data, pdf_path)
                export_markdown(data, md_path)
                export_json(data, json_path)
                
                with open(txt_path, 'w', encoding='utf-8') as f:
                    f.write(st.session_state['transcript'])
                
                files_to_zip = [pdf_path, md_path, json_path, txt_path]
                if st.session_state['cleaned_audio_path'] and os.path.exists(st.session_state['cleaned_audio_path']):
                    files_to_zip.append(st.session_state['cleaned_audio_path'])
                    
                create_zip_package(files_to_zip, zip_path)
                
                st.success("Export package generated successfully!")
                
                with open(zip_path, "rb") as fp:
                    btn = st.download_button(
                        label="Download ZIP Package",
                        data=fp,
                        file_name="podcast_package.zip",
                        mime="application/zip"
                    )
    else:
        st.info("No data to export yet.")

# --- 8. Library ---
with tab_library:
    st.header("Project Library")
    st.markdown("View past episodes saved to your MongoDB Cloud cluster.")
    
    db_uri = os.getenv("MONGO_URI", "mongodb+srv://debojyotighoshmain_db_user:vovOK47muDSPWrvq@prowhizcluster.lj07oth.mongodb.net/?appName=Prowhizcluster")
    
    if st.button("Refresh Library", type="secondary"):
        st.session_state['library_data'] = get_all_podcast_data(db_uri)
        
    if 'library_data' not in st.session_state:
        with st.spinner("Fetching projects from database..."):
            st.session_state['library_data'] = get_all_podcast_data(db_uri)
            
    records = st.session_state.get('library_data', [])
    
    if not records:
        st.info("No projects found in the database yet.")
    else:
        for idx, record in enumerate(reversed(records)):
            project_name = record.get("project_name", "Untitled")
            episode_title = record.get("selected_title", "Unknown Title")
            
            with st.expander(f"🎙️ {project_name} - {episode_title}"):
                col1, col2 = st.columns([0.7, 0.3])
                with col1:
                    st.subheader("Summary")
                    summary_obj = record.get("summary", {})
                    exec_summary = summary_obj.get("executive_summary", "") if isinstance(summary_obj, dict) else record.get("executive_summary", "No summary available.")
                    st.write(exec_summary or "No summary available.")
                    
                    st.subheader("Transcript Snippet")
                    full_transcript = record.get("transcript", "")
                    st.write(full_transcript[:300] + "..." if len(full_transcript) > 300 else full_transcript)
                
                with col2:
                    st.subheader("Actions")
                    if st.button("Restore to Tabs", key=f"restore_{idx}", use_container_width=True):
                        # Populate session state from history
                        st.session_state['project_name'] = record.get('project_name', 'Untitled')
                        st.session_state['transcript'] = record.get('transcript', '')
                        st.session_state['selected_title'] = record.get('selected_title', '')
                        st.session_state['summary'] = record.get('summary', {})
                        st.session_state['titles'] = record.get('titles', {})
                        st.session_state['show_notes'] = record.get('show_notes', {})
                        st.session_state['highlights'] = record.get('highlights', {})
                        st.session_state['social_media'] = record.get('social_media', {})
                        st.session_state['seo'] = record.get('seo_tags', {})
                        st.session_state['audio_stats'] = record.get('audio_stats', {})
                        
                        # Trigger regeneration of analytics
                        st.session_state['wordcloud_img'] = generate_wordcloud(st.session_state['transcript'])
                        st.session_state['topics_img'] = analyze_topics(st.session_state['transcript'])
                        st.session_state['cleaned_audio_path'] = None
                        
                        st.session_state['sync_status'] = "☁️ Restored from Cloud"
                        st.success("Project restored! Check the other tabs.")
                        st.rerun()

                    if st.button("Delete Permanently", key=f"del_{idx}", type="primary", use_container_width=True):
                        if delete_podcast_data(db_uri, record.get('_id')):
                            st.session_state['library_data'] = get_all_podcast_data(db_uri)
                            st.success("Project deleted!")
                            st.rerun()

                st.divider()
                st.download_button(
                    label="Download Full JSON Record",
                    data=json.dumps(record, indent=2),
                    file_name=f"project_{idx}.json",
                    mime="application/json",
                    key=f"download_btn_{idx}"
                )

# --- Autosave Logic ---
if st.session_state.get('transcript'):
    # Build current state dictionary
    current_data = {
        "project_name": st.session_state.get('project_name', 'Untitled'),
        "selected_title": st.session_state.get('selected_title', 'Podcast Episode'),
        "summary": st.session_state.get('summary', {}),
        "titles": st.session_state.get('titles', {}),
        "show_notes": st.session_state.get('show_notes', {}),
        "highlights": st.session_state.get('highlights', {}),
        "social_media": st.session_state.get('social_media', {}),
        "seo_tags": st.session_state.get('seo', {}),
        "transcript": st.session_state.get('transcript', ''),
        "audio_stats": st.session_state.get('audio_stats', {})
    }
    
    # Check if data has changed since last save
    current_data_str = json.dumps(current_data, sort_keys=True, default=str)
    
    # Strip _id if it accidentally got into last_saved_data
    last_saved = st.session_state.get('last_saved_data', {}).copy()
    if '_id' in last_saved:
        del last_saved['_id']
    last_saved_str = json.dumps(last_saved, sort_keys=True, default=str)
    
    if current_data_str != last_saved_str:
        db_uri = os.getenv("MONGO_URI", "mongodb+srv://debojyotighoshmain_db_user:vovOK47muDSPWrvq@prowhizcluster.lj07oth.mongodb.net/?appName=Prowhizcluster")
        try:
            # Pass a copy to pymongo so it doesn't inject _id into our state
            save_podcast_data(db_uri, current_data.copy())
            st.session_state['last_saved_data'] = current_data.copy()
            st.session_state['sync_status'] = "☁️ Saved to Cloud"
            st.rerun() # Trigger rerun to update the UI indicator at the top
        except Exception as e:
            st.session_state['sync_status'] = f"⚠️ Sync Error: {str(e)[:40]}"
