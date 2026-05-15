import matplotlib.pyplot as plt
import io
import re
from collections import Counter
from wordcloud import WordCloud

def generate_wordcloud(text: str) -> io.BytesIO:
    """Generate a wordcloud image from text."""
    # Basic error handling for empty text
    if not text or len(text.strip()) == 0:
        text = "No transcript available"
        
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    return img_buffer

def analyze_topics(text: str) -> io.BytesIO:
    """Generate a simple bar chart of top keyword frequencies."""
    if not text or len(text.strip()) == 0:
        text = "None"
        
    stop_words = set(["the", "and", "a", "to", "of", "in", "i", "is", "that", "it", "on", "you", "this", "for", "but", "with", "are", "have", "be", "at", "or", "as", "was", "so", "if", "out", "not", "we", "they", "he", "she", "it's", "that's", "can", "about", "what", "just", "like", "know", "how"])
    
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    filtered_words = [w for w in words if w not in stop_words]
    
    word_counts = Counter(filtered_words)
    top_words = dict(word_counts.most_common(10))
    
    if not top_words:
        top_words = {"none": 1}
        
    plt.figure(figsize=(10, 5))
    plt.bar(top_words.keys(), top_words.values(), color='#1f77b4')
    plt.title('Top 10 Topic Keywords')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    return img_buffer
