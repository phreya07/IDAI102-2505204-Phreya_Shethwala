import streamlit as st
from datetime import datetime, timedelta
import json
import random

# Page configuration
st.set_page_config(
    page_title="MedTimer - Welcome",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd 0%, #b3e5fc 100%);
    }
    
    /* Center and limit width for onboarding screens */
    .block-container {
        max-width: 800px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Center text inputs and make them wider */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        text-align: center;
        font-size: 1.1rem;
        padding: 12px;
    }
    
    /* Make buttons full width and nicely styled */
    .stButton > button {
        width: 100%;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: 500;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Style primary buttons */
    .stButton > button[kind="primary"] {
        background: #4a90e2;
        color: white;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: #357abd;
    }
    
    /* Center form elements */
    .stForm {
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Style time input */
    .stTimeInput > div {
        justify-content: center;
    }
    
    .main-header {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 20px;
        margin-bottom: 20px;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 300;
    }
    
    .main-header p {
        margin: 10px 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .welcome-header {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        padding: 40px 30px;
        text-align: center;
        border-radius: 20px;
        margin-bottom: 30px;
    }
    
    .welcome-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 300;
    }
    
    .welcome-header p {
        margin: 10px 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .medicine-item {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid;
    }
    
    .medicine-taken {
        background: #d5f4e6;
        border-left-color: #27ae60;
    }
    
    .medicine-upcoming {
        background: #fff3cd;
        border-left-color: #f39c12;
    }
    
    .medicine-missed {
        background: #f8d7da;
        border-left-color: #e74c3c;
    }
    
    .status-badge {
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 500;
        display: inline-block;
    }
    
    .status-taken {
        background: #27ae60;
        color: white;
    }
    
    .status-upcoming {
        background: #f39c12;
        color: white;
    }
    
    .status-missed {
        background: #e74c3c;
        color: white;
    }
    
    .adherence-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #e9ecef;
        text-align: center;
    }
    
    .adherence-score {
        font-size: 3rem;
        font-weight: bold;
        margin: 15px 0;
    }
    
    .score-excellent {
        color: #27ae60;
    }
    
    .score-good {
        color: #f39c12;
    }
    
    .score-needs-improvement {
        color: #e74c3c;
    }
    
    .celebration-banner {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        color: #8e24aa;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .streak-counter {
        background: #e8f5e8;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #4caf50;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .streak-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2e7d32;
        margin: 10px 0;
    }
    
    .motivation-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
    }
    
    .companion-display {
        min-height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4rem;
        margin: 20px 0;
    }
    
    .emergency-contact {
        background: #ffebee;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #f44336;
    }
    
    /* Option buttons for gender and companion selection */
    .option-button {
        background: white;
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .option-button:hover {
        border-color: #4a90e2;
        background: #f0f8ff;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.2);
    }
    
    div[data-testid="stHorizontalBlock"] {
        gap: 15px;
    }
    
    /* Center column content for onboarding */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }
</style>
""", unsafe_allow_html=True)

# Motivational quotes
MOTIVATIONAL_QUOTES = [
    "Taking care of yourself is the first step to taking care of others.",
    "Every small step towards health is a victory worth celebrating.",
    "Your health is an investment, not an expense.",
    "Consistency in small things leads to great achievements.",
    "You are stronger than you think, and more capable than you imagine.",
    "Health is not about being perfect, it's about being consistent.",
    "Each day is a new opportunity to care for yourself.",
    "Your future self will thank you for the care you show today.",
    "You're doing wonderfully! Each medicine taken is an act of self-love.",
    "Your dedication to your health inspires everyone around you.",
    "Small daily improvements lead to stunning yearly results.",
    "You have the power to make today better than yesterday.",
    "A healthy outside starts from the inside.",
    "Progress, not perfection, is the goal.",
    "Your body is your temple. Keep it pure and clean for the soul to reside in.",
    "Healing is a matter of time, but it is sometimes also a matter of opportunity.",
    "The greatest wealth is health.",
    "Take care of your body. It's the only place you have to live.",
    "Health is a state of complete harmony of the body, mind and spirit.",
    "An apple a day keeps the doctor away, but medicine on time keeps worry away.",
    "Your health journey is a marathon, not a sprint.",
    "Every pill taken with purpose is a step toward wellness.",
    "Believe in your ability to heal and grow stronger each day.",
    "Self-care isn't selfish, it's essential.",
    "You are worth the effort it takes to stay healthy.",
    "Today's medicine is tomorrow's strength.",
    "Caring for yourself gives you the energy to care for others.",
    "Your commitment to health today shapes your tomorrow.",
    "Small acts of self-care lead to big changes in well-being.",
    "Every dose taken is a promise to yourself to feel better.",
]
quote = random.choice(MOTIVATIONAL_QUOTES)


# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None
if 'medicines' not in st.session_state:
    st.session_state.medicines = []
if 'daily_streak' not in st.session_state:
    st.session_state.daily_streak = 0
if 'last_completed_date' not in st.session_state:
    st.session_state.last_completed_date = None
if 'reminders_enabled' not in st.session_state:
    st.session_state.reminders_enabled = False
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'motivation_quote' not in st.session_state:
    st.session_state.motivation_quote = random.choice(MOTIVATIONAL_QUOTES)

# Helper functions
def get_medicine_status(medicine):
    now = datetime.now()
    current_time = now.hour * 60 + now.minute
    med_time = datetime.strptime(medicine['time'], '%H:%M')
    medicine_time = med_time.hour * 60 + med_time.minute
    
    if medicine['taken']:
        return 'taken'
    elif current_time < medicine_time:
        return 'upcoming'
    else:
        return 'missed'

def format_time(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M')
    return time_obj.strftime('%I:%M %p')

def calculate_adherence():
    if not st.session_state.medicines:
        return 0
    taken = sum(1 for med in st.session_state.medicines if med['taken'])
    return round((taken / len(st.session_state.medicines)) * 100)

def update_daily_streak():
    today = datetime.now().date().isoformat()
    if st.session_state.last_completed_date != today:
        yesterday = (datetime.now().date() - timedelta(days=1)).isoformat()
        if st.session_state.last_completed_date == yesterday:
            st.session_state.daily_streak += 1
        else:
            st.session_state.daily_streak = 1
        st.session_state.last_completed_date = today

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return 'Good morning'
    elif hour < 17:
        return 'Good afternoon'
    else:
        return 'Good evening'

# Welcome Screen
if st.session_state.user_profile is None:
    st.markdown("""
    <div class="welcome-header">
        <h1>🏥 Welcome to MedTimer</h1>
        <p>Your Personal Medicine Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; color: #4a90e2;'>Let's get to know you better!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem;'>We'll create a personalized experience just for you. This information helps us provide better care reminders.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Step 1: Name
    if st.session_state.current_step == 1:
        st.markdown("<h3 style='text-align: center;'>Step 1 of 4: What's your name?</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        user_name = st.text_input("Your Name", placeholder="Enter your first name", key="user_name_input", label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Continue", type="primary", use_container_width=True):
                if user_name:
                    st.session_state.temp_name = user_name
                    st.session_state.current_step = 2
                    st.rerun()
                else:
                    st.error("Please enter your name to continue.")
    
    # Step 2: Age
    elif st.session_state.current_step == 2:
        st.markdown("<h3 style='text-align: center;'>Step 2 of 4: How old are you?</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        user_age = st.number_input("Your Age", min_value=1, max_value=120, placeholder="Enter your age", key="user_age_input", label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("Back", use_container_width=True):
                st.session_state.current_step = 1
                st.rerun()
        with col3:
            if st.button("Continue", type="primary", use_container_width=True):
                if user_age > 0:
                    st.session_state.temp_age = user_age
                    st.session_state.current_step = 3
                    st.rerun()
                else:
                    st.error("Please enter your age to continue.")
    
    # Step 3: Gender
    elif st.session_state.current_step == 3:
        st.markdown("<h3 style='text-align: center;'>Step 3 of 4: Gender</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("👨\n\nMale", use_container_width=True):
                st.session_state.temp_gender = "male"

        with col2:
            if st.button("👩\n\nFemale", use_container_width=True):
                st.session_state.temp_gender = "female"
        with col3:
            if st.button("👤\n\nOther", use_container_width=True):
                st.session_state.temp_gender = "other"
        with col4:
            if st.button("🤝\n\nPrefer not to say", use_container_width=True):
                st.session_state.temp_gender = "prefer-not-to-say"
        
        if 'temp_gender' not in st.session_state:
            st.session_state.temp_gender = "prefer-not-to-say"
        


        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("Back ", use_container_width=True):
                st.session_state.current_step = 2
                st.rerun()
        with col3:
            if st.button("Continue ", type="primary", use_container_width=True):
                st.session_state.current_step = 4
                st.rerun()
    
    # Step 4: Companion
    elif st.session_state.current_step == 4:
        st.markdown("<h3 style='text-align: center;'>Step 4 of 4: Choose your companion!</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Pick a friendly companion to encourage you on your health journey:</p>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("🐢\n\nWise Turtle\n\nSteady and encouraging", use_container_width=True):
                st.session_state.temp_companion = "turtle"
        with col2:
            if st.button("🐱\n\nCaring Cat\n\nGentle and supportive", use_container_width=True):
                st.session_state.temp_companion = "cat"
        with col3:
            if st.button("🐕\n\nLoyal Dog\n\nEnthusiastic and loyal", use_container_width=True):
                st.session_state.temp_companion = "dog"
        with col4:
            if st.button("🐦\n\nCheerful Bird\n\nUplifting and bright", use_container_width=True):
                st.session_state.temp_companion = "bird"
        
        if 'temp_companion' not in st.session_state:
            st.session_state.temp_companion = "turtle"
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("Back  ", use_container_width=True):
                st.session_state.current_step = 3
                st.rerun()
        with col3:
            if st.button("Start My Journey!", type="primary", use_container_width=True):
                st.session_state.user_profile = {
                    'name': st.session_state.temp_name,
                    'age': st.session_state.temp_age,
                    'gender': st.session_state.temp_gender,
                    'companion': st.session_state.temp_companion,
                    'join_date': datetime.now().isoformat()
                }
                st.rerun()

# Main App Screen
else:
    # Header
    st.markdown(f"""
    <div class="main-header">
        <h1>🏥 MedTimer</h1>
        <p>{get_greeting()}, {st.session_state.user_profile['name']}! Your health companion is here.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Current time
    current_time = datetime.now()
    time_string = current_time.strftime('%I:%M %p')
    date_string = current_time.strftime('%A, %B %d, %Y')
    
    # Main content
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Add Medicine Form
        with st.container():
            st.markdown("### 💊 Add New Medicine")
            with st.form("medicine_form"):
                medicine_name = st.text_input("Medicine Name", placeholder="e.g., Aspirin, Vitamin D")
                medicine_time = st.time_input("Time")
                submitted = st.form_submit_button("Add Medicine", type="primary")
                
                if submitted and medicine_name:
                    new_medicine = {
                        'id': int(datetime.now().timestamp() * 1000),
                        'name': medicine_name,
                        'time': medicine_time.strftime('%H:%M'),
                        'taken': False,
                        'dateAdded': datetime.now().date().isoformat()
                    }
                    st.session_state.medicines.append(new_medicine)
                    st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Medicine List
        with st.container():
            st.markdown("### 📋 Today's Medicines")
            st.markdown(f"<p style='color: #7f8c8d; font-size: 1.1rem;'>{date_string} • {time_string}</p>", unsafe_allow_html=True)
            
            if not st.session_state.medicines:
                st.markdown("""
                <div style='text-align: center; padding: 40px; color: #7f8c8d;'>
                    <h3>No medicines added yet</h3>
                    <p>Add your first medicine above to get started!</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                sorted_medicines = sorted(st.session_state.medicines, key=lambda x: x['time'])
                for medicine in sorted_medicines:
                    status = get_medicine_status(medicine)
                    status_class = f"medicine-{status}"
                    status_text = {'taken': 'Taken ✓', 'upcoming': 'Upcoming', 'missed': 'Missed'}[status]
                    status_badge_class = f"status-{status}"
                    
                    st.markdown(f"""
                    <div class="medicine-item {status_class}">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <div style="font-size: 1.2rem; font-weight: 500; margin-bottom: 5px;">{medicine['name']}</div>
                                <div style="font-size: 1rem; color: #7f8c8d;">{format_time(medicine['time'])}</div>
                            </div>
                            <div>
                                <span class="status-badge {status_badge_class}">{status_text}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col2:
                        if not medicine['taken']:
                            if st.button("Mark Taken", key=f"take_{medicine['id']}", type="primary"):
                                for med in st.session_state.medicines:
                                    if med['id'] == medicine['id']:
                                        med['taken'] = True
                                        # Check if all medicines are taken
                                        if all(m['taken'] for m in st.session_state.medicines):
                                            update_daily_streak()
                                        break
                                st.rerun()
                    with col3:
                        if st.button("Del", key=f"delete_{medicine['id']}"):
                            st.session_state.medicines = [m for m in st.session_state.medicines if m['id'] != medicine['id']]
                            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Motivation Card
        st.markdown(f"""
        <div class="motivation-card">
            <h3>💪 Daily Motivation</h3>
            <div style="font-style: italic; font-size: 1.1rem; line-height: 1.4;" >
                "{st.session_state.motivation_quote}"
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        

        if st.button("New Quote", key="new_quote"):
            st.session_state.motivation_quote = random.choice(MOTIVATIONAL_QUOTES)
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Emergency Contact
        st.markdown("""
        <div class="emergency-contact">
            <h4 style='text-align: center; color: #c62828;'>🚨 Need Help?</h4>
            <p style='text-align: center; font-size: 1.1rem;'>If you feel unwell or have concerns about your medicines, contact your doctor or call emergency services.</p>
            <div style='margin-top: 15px;'>
                <div style='margin-bottom: 10px;'>
                    <strong>👨‍⚕️ Your Doctor:</strong>
                    <div style='margin-left: 20px; color: #666;'>
                        <div>📞 Phone: <span style='color: #4a90e2;'>Call your doctor</span></div>
                        <div>📧 Email: <span style='color: #4a90e2;'>doctor@clinic.com</span></div>
                    </div>
                </div>
                <div style='margin-bottom: 10px;'>
                    <strong>🏥 Emergency:</strong>
                    <div style='margin-left: 20px; color: #666;'>
                        <div>🚨 Emergency: <span style='color: #e74c3c; font-weight: bold;'>911</span></div>
                        <div>🏥 Hospital: <span style='color: #4a90e2;'>Your local hospital</span></div>
                    </div>
                </div>
                <div>
                    <strong>👨‍👩‍👧‍👦 Family Contact:</strong>
                    <div style='margin-left: 20px; color: #666;'>
                        <div>📱 Family: <span style='color: #4a90e2;'>Add family contact</span></div>
                        <div>📧 Email: <span style='color: #4a90e2;'>family@email.com</span></div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        # Celebration Banner
        adherence = calculate_adherence()
        if adherence == 100 and st.session_state.medicines:
            st.markdown("""
            <div class="celebration-banner">
                <h3>🎉 Wonderful! All medicines taken today! 🎉</h3>
                <p>You're taking excellent care of yourself!</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Streak Counter
        st.markdown(f"""
        <div class="streak-counter">
            <h4>🔥 Daily Streak</h4>
            <div class="streak-number">{st.session_state.daily_streak}</div>
            <p>days of great care</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reminder Settings
        st.markdown("### 🔔 Gentle Reminders")
        st.session_state.reminders_enabled = st.toggle("Soft chime reminders", value=st.session_state.reminders_enabled)
        st.caption("Get a gentle sound when it's time for medicine")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Adherence Card
        adherence = calculate_adherence()
        if adherence >= 90:
            score_class = "score-excellent"
            message = "Excellent! You're doing amazing! 🌟"
        elif adherence >= 70:
            score_class = "score-good"
            message = "Good job! Keep up the great work! 👍"
        elif adherence > 0:
            score_class = "score-needs-improvement"
            message = "You can do this! Every step counts! 💪"
        else:
            score_class = ""
            message = "Start adding medicines to track your progress!"
        
        st.markdown(f"""
        <div class="adherence-card">
            <h3>📊 Weekly Adherence</h3>
            <div class="adherence-score {score_class}">{adherence}%</div>
            <p>{message}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Companion Display
        companion = st.session_state.user_profile['companion']
        companion_emoji = {'turtle': '🐢', 'cat': '🐱', 'dog': '🐕', 'bird': '🐦'}[companion]
        companion_name = {'turtle': 'Wise Turtle', 'cat': 'Caring Cat', 'dog': 'Loyal Dog', 'bird': 'Cheerful Bird'}[companion]
        
        if adherence >= 90:
            achievement_emoji = '🏆✨'
            companion_message = f"Outstanding! Your {companion_name} earned a golden trophy!"
        elif adherence >= 80:
            achievement_emoji = '🥇💫'
            companion_message = f"Excellent! Your {companion_name} is celebrating with you!"
        elif adherence >= 60:
            achievement_emoji = '🌟💚'
            companion_message = f"Great job! Your {companion_name} is so proud of you!"
        elif adherence > 0:
            achievement_emoji = '💪🌱'
            companion_message = f"You're doing great! Your {companion_name} believes in you!"
        else:
            achievement_emoji = '😴💤'
            companion_message = f"Add medicines to wake up your {companion_name}!"
        
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 15px; border: 2px solid #e9ecef; text-align: center;">
            <h3 style="color: #4a90e2;">🎉 Your {companion_name}</h3>
            <div class="companion-display">
                <span style="font-size: 4rem;">{companion_emoji}</span>
                <span style="font-size: 2rem;">{achievement_emoji}</span>
            </div>
            <p>{companion_message}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Comfort Features
        st.markdown("""
        <div style="background: #f0f8ff; padding: 25px; border-radius: 15px; border: 2px solid #b3d9ff;">
            <h3 style="color: #1976d2;">💙 Comfort Features</h3>
            <div style="margin-bottom: 10px;">
                <span>🌅</span> <span style="font-size: 1.1rem;">Large, clear text for easy reading</span>
            </div>
            <div style="margin-bottom: 10px;">
                <span>🎨</span> <span style="font-size: 1.1rem;">Calming colors to reduce stress</span>
            </div>
            <div style="margin-bottom: 10px;">
                <span>🏆</span> <span style="font-size: 1.1rem;">Celebrations for your achievements</span>
            </div>
            <div>
                <span>💾</span> <span style="font-size: 1.1rem;">Remembers your medicines safely</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Reset button (optional, for testing)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Reset Profile", key="reset_profile"):
        st.session_state.user_profile = None
        st.session_state.medicines = []
        st.session_state.daily_streak = 0
        st.session_state.last_completed_date = None
        st.session_state.current_step = 1
        st.rerun()