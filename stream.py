import streamlit as st
from PIL import Image
import base64
import time
import random

# Set page configuration
st.set_page_config(
    page_title="Happy Birthday Jeni!",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Background music
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Heart animation with HTML
def heart_animation():
    heart_html = """
    <div style="display: flex; justify-content: center; align-items: center; height: 100px;">
        <div style="background-color: red; height: 50px; width: 50px; position: relative; 
                    transform: rotate(-45deg); animation: heartbeat 1.5s infinite;">
            <div style="content: ''; background-color: red; border-radius: 50%; height: 50px; 
                        width: 50px; position: absolute; top: -25px; left: 0;"></div>
            <div style="content: ''; background-color: red; border-radius: 50%; height: 50px; 
                        width: 50px; position: absolute; left: 25px; top: 0;"></div>
        </div>
    </div>
    <style>
        @keyframes heartbeat {
            0% { transform: rotate(-45deg) scale(1); }
            25% { transform: rotate(-45deg) scale(1.1); }
            50% { transform: rotate(-45deg) scale(1); }
            75% { transform: rotate(-45deg) scale(1.1); }
            100% { transform: rotate(-45deg) scale(1); }
        }
    </style>
    """
    st.components.v1.html(heart_html, height=150)

# Confetti animation using streamlit components
def confetti_animation():
    confetti_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    </head>
    <body>
        <script>
            var duration = 3 * 1000;
            var animationEnd = Date.now() + duration;
            var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

            function randomInRange(min, max) {
                return Math.random() * (max - min) + min;
            }

            var interval = setInterval(function() {
                var timeLeft = animationEnd - Date.now();

                if (timeLeft <= 0) {
                    return clearInterval(interval);
                }

                var particleCount = 50 * (timeLeft / duration);
                confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
                confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
            }, 250);
        </script>
    </body>
    </html>
    """
    st.components.v1.html(confetti_html, height=0)

# Love letter animation with white text
def love_letter_animation():
    letter_html = """
    <div style="position: relative; width: 200px; height: 200px; margin: 0 auto;">
        <div style="position: relative; width: 200px; height: 120px; background-color: #ff6b6b; 
                    border-radius: 5px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); 
                    animation: float 3s ease-in-out infinite;">
            <div style="position: absolute; width: 180px; height: 200px; background-color: #333; 
                        top: 0; left: 10px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
                        z-index: 2; padding: 10px; transform: translateY(-100px);">
                <div style="color: white; text-align: center;">
                    <strong>Dear Jeni,</strong>
                    <p>You make my world brighter every day. Happy Birthday my love!</p>
                </div>
            </div>
        </div>
        <div style="position: absolute; width: 30px; height: 30px; background-color: #ff4b4b; 
                    transform: rotate(-45deg); top: 50px; left: 85px; z-index: 4; 
                    animation: heartbeat 1.5s infinite;">
            <div style="content: ''; background-color: #ff4b4b; border-radius: 50%; height: 30px; 
                        width: 30px; position: absolute; top: -15px; left: 0;"></div>
            <div style="content: ''; background-color: #ff4b4b; border-radius: 50%; height: 30px; 
                        width: 30px; position: absolute; left: 15px; top: 0;"></div>
        </div>
    </div>
    <style>
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        @keyframes heartbeat {
            0% { transform: rotate(-45deg) scale(1); }
            25% { transform: rotate(-45deg) scale(1.1); }
            50% { transform: rotate(-45deg) scale(1); }
            75% { transform: rotate(-45deg) scale(1.1); }
            100% { transform: rotate(-45deg) scale(1); }
        }
    </style>
    """
    st.components.v1.html(letter_html, height=300)

# Function to resize images to consistent portrait size
def resize_portrait(image, target_height=400):
    width, height = image.size
    # Calculate new width maintaining aspect ratio
    new_width = int(width * (target_height / height))
    return image.resize((new_width, target_height), Image.ANTIALIAS)

# Main app
def main():
    # Header
    st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎉 Happy Birthday Jeni! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ff85a2;'>From Jaswanth with Love ❤️</h3>", unsafe_allow_html=True)
    
    # Age calculation
    birth_year = 2001
    current_year = 2025  # Update this as needed
    age = current_year - birth_year
    
    st.markdown(f"<h2 style='text-align: center; color: #ff6b6b;'>Today you turn {age}!</h2>", unsafe_allow_html=True)
    
    # Play background music (replace with your actual song file)
    try:
        autoplay_audio("D:/Downloads/கண்  திறக்கும் போது என் வெளிச்சம் நீ (1).mp3")
    except:
        st.warning("Couldn't load the birthday song")
    
    # Photo gallery
    st.markdown("<h2 style='text-align: center; color: #ff85a2;'>Our Beautiful Memories</h2>", unsafe_allow_html=True)
    
    # Replace these with your actual images
    image_paths = ["C:/Users/USER/OneDrive/Pictures/IMG-20230115-WA0040.jpg", "C:/Users/USER/OneDrive/Pictures/IMG-20221231-WA0123.jpg", "C:/Users/USER/OneDrive/Pictures/IMG-20211212-WA0001.jpg", "C:/Users/USER/OneDrive/Pictures/IMG-20221224-WA0035.jpg", "C:/Users/USER/OneDrive/Pictures/IMG20220811133415.jpg", "C:/Users/USER/OneDrive/Pictures/IMG-20221229-WA0007.jpg"]
    # Romantic quotes for each image
    romantic_quotes = [
        "Your love is the melody of my life's song",
        "In your eyes I found my paradise",
        "Every moment with you becomes a beautiful memory",
        "Your smile lights up my world",
        "You're the missing piece to my puzzle",
        "My heart found its home in you"
    ]
    
    images = []
    for path in image_paths:
        try:
            img = Image.open(path)
            # # Resize to consistent portrait size
            # img_resized = resize_portrait(img)
            # images.append(img_resized)
            images.append(img)
        except:
            # If images not found, use placeholder
            st.warning(f"Image {path} not found")
            continue
    
    if images:
        # Display images in 2 columns with 3 rows for better layout
        cols = st.columns(2)
        for idx, (img, quote) in enumerate(zip(images, romantic_quotes)):
            with cols[idx % 2]:
                st.image(img, use_column_width=True, caption=quote)
    
    # Love notes section with black text
    st.markdown("<h2 style='text-align: center; color: #ff85a2;'>My Love Notes for You</h2>", unsafe_allow_html=True)
    
    love_notes = [
        "Every moment with you feels like a beautiful dream I never want to wake up from.",
        "Your smile is my favorite thing in the world. Keep smiling always!",
        "I fall in love with you more every day, if that's even possible.",
        "You're not just my lover, you're my best friend, my partner, and my soulmate.",
        "Happy Birthday to the most amazing woman I've ever known. I'm so lucky to have you.",
        "I promise to love you, cherish you, and make you happy for all the birthdays to come."
    ]
    
    for note in love_notes:
        st.markdown(f"""
        <div style="background-color: white; border-radius: 15px; padding: 15px; 
                    margin: 10px 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                    border-left: 5px solid #ff4b4b; animation: fadeIn 0.5s ease-in;">
            <p style="color: black;">💌 {note}</p>
        </div>
        <style>
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
        """, unsafe_allow_html=True)
        time.sleep(0.3)
    
    # Interactive buttons with animations
    st.markdown("<h2 style='text-align: center; color: #ff85a2;'>Special Birthday Wishes</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎈 Send Balloons"):
            st.balloons()
            st.success("Balloons for my beautiful Jeni! May your life be as colorful as these balloons!")
    
    with col2:
        if st.button("💖 Heart Animation"):
            heart_animation()
            st.success("My heart beats only for you Jeni! Happy Birthday my love!")
    
    with col3:
        if st.button("🎊 Confetti Celebration"):
            confetti_animation()
            st.success("Let's celebrate your special day with a bang! You deserve all the happiness!")
    
    # Additional surprise button
    if st.button("💌 Open Love Letter", key="love_letter"):
        love_letter_animation()
        st.markdown("""
        <div style="text-align: center; background-color: #333; color: white; 
                    border-radius: 15px; padding: 20px; margin-top: 20px;">
            <h3>My Dearest Jeni,</h3>
            <p>On your special day, I want you to know how much you mean to me.</p>
            <p>You've brought so much joy and love into my life, and I can't imagine my world without you in it.</p>
            <p>May this year bring you all the happiness, success, and love you deserve.</p>
            <p>I look forward to creating many more beautiful memories with you.</p>
            <p>Forever yours,</p>
            <p><strong>Jaswanth</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Final birthday message
    st.markdown("""
    <div style="text-align: center; margin-top: 30px; padding: 20px; 
                background: linear-gradient(45deg, #ff9a9e, #fad0c4); 
                border-radius: 15px; color: white; animation: pulse 2s infinite;">
        <h2>Happy 24th Birthday Jeni!</h2>
        <p>May your day be as wonderful and special as you are!</p>
        <p>With all my love,</p>
        <p>Jaswanth ❤️</p>
    </div>
    <style>
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
