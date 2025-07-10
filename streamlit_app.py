import streamlit as st
from PIL import Image
import datetime
import random

# Set page configuration
st.set_page_config(
    page_title="My Love for Jeni",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
    }
    .title {
        font-family: 'Brush Script MT', cursive;
        font-size: 48px !important;
        color: #d23669;
        text-align: center;
        text-shadow: 2px 2px 4px #ffffff;
    }
    .message {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #333;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .heart {
        color: #ff4757;
        font-size: 24px;
    }
    .special-date {
        background-color: rgba(255, 107, 129, 0.3);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .stButton>button {
        background-color: #ff6b81;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff4757;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header with title
st.markdown('<p class="title">My Eternal Love for Jeni ❤️</p>', unsafe_allow_html=True)

# Sidebar with personal touch
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80", 
             caption="Every moment with you is special", use_column_width=True)
    st.markdown("### Our Journey")
    
    # Important dates (replace with your actual dates)
    important_dates = {
        "First Met": "2020-05-15",
        "First Date": "2020-06-20",
        "First Kiss": "2020-07-04",
        "Official Relationship": "2020-08-15"
    }
    
    for event, date in important_dates.items():
        st.markdown(f"**{event}**: {date}")

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["Love Letters", "Our Memories", "Why I Love You", "Future Together"])

with tab1:
    st.markdown("""
    <div class="message">
        <h3>My Dearest Jeni,</h3>
        <p>From the moment I met you, I knew there was something extraordinary about you. 
        Your smile lights up my world, your laughter is my favorite melody, and your love 
        is the greatest gift I've ever received.</p>
        <p>Every day with you is an adventure, whether we're exploring new places or just 
        cuddling on the couch. You make ordinary moments magical and difficult times easier 
        to bear.</p>
        <p>I promise to cherish you, support you, and love you more each day than the day before.</p>
        <p>Forever yours,</p>
        <p>[Your Name]</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Date countdown calculator
    st.subheader("Our Special Day Countdown")
    special_date = st.date_input("When is your next special date?", datetime.date(2023, 12, 25))
    today = datetime.date.today()
    delta = special_date - today
    st.write(f"Only {delta.days} days until our next special day together!")

with tab2:
    # Photo gallery (replace with your actual images)
    st.subheader("Our Beautiful Memories Together")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
                 caption="Our first vacation together")
    with col2:
        st.image("https://images.unsplash.com/photo-1494774157365-9e04c6720e47?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
                 caption="Celebrating our anniversary")
    with col3:
        st.image("https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", 
                 caption="Just being us")
    
    # Memory description
    st.markdown("""
    <div class="message">
        <p>Every photo with you tells a story - a story of love, laughter, and happiness. 
        I treasure each memory we've created together and look forward to making countless more.</p>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    # Reasons I love you
    st.subheader("101 Reasons Why I Love You")
    
    reasons = [
        "Your beautiful smile that brightens my darkest days",
        "The way you understand me without words",
        "Your kindness that touches everyone around you",
        "Your intelligence and the way you see the world",
        "How safe and loved I feel in your arms",
        "Your passion for life that inspires me",
        "The way you make me want to be a better person",
        "Your laugh that I can recognize anywhere",
        "How you remember the little things about me",
        "Your strength in facing challenges",
        "The way you look at me like I'm your whole world"
    ]
    
    # Display random reasons
    if st.button("Show me a reason why I love you"):
        reason = random.choice(reasons)
        st.markdown(f'<div class="message"><span class="heart">❤️</span> {reason}</div>', 
                    unsafe_allow_html=True)
    
    # Love meter (just for fun)
    st.subheader("Our Love Meter")
    love_level = st.slider("How much do I love Jeni?", 0, 100, 100)
    st.write(f"I love Jeni {love_level}%! (Actually it's infinite ♾️)")

with tab4:
    # Future plans
    st.markdown("""
    <div class="message">
        <h3>Our Future Together</h3>
        <p>With you by my side, I know the future will be beautiful. Here's what I dream for us:</p>
        <ul>
            <li>Growing old together, hand in hand</li>
            <li>Building a home filled with love and laughter</li>
            <li>Traveling the world and creating unforgettable memories</li>
            <li>Supporting each other's dreams and aspirations</li>
            <li>Facing life's challenges together, stronger as a team</li>
            <li>Creating our own little traditions and inside jokes</li>
            <li>Always finding new reasons to fall in love with each other</li>
        </ul>
        <p>No matter what the future holds, I know it will be wonderful because I'll be with you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Promise button
    if st.button("Make a Promise to Jeni"):
        st.balloons()
        st.success("I promise to love you unconditionally, today, tomorrow, and forever.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #d23669;">
        <p>Created with love for the most amazing person in my life ❤️</p>
        <p>Every day with you is a blessing I don't take for granted</p>
    </div>
""", unsafe_allow_html=True)
