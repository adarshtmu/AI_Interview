import streamlit as st
import requests
import json
import time

# --- CONFIGURATION ---
# IMPORTANT: Replace with your actual Gemini API Key.
# Keeping API keys in code is not recommended for production. Consider using environment variables or Streamlit secrets.
GEMINI_API_KEY = "AIzaSyAfzl_66GZsgaYjAM7cT2djVCBCAr86t2k"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"


# --- PAGE SETUP ---
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    /* Base styling for dark theme */
    .stApp {
        background-color: #0f172a; /* slate-900 */
        color: #f8fafc; /* slate-50 */
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc;
    }

    .stButton>button {
        transition: all 0.3s ease;
        border-radius: 9999px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        border: none;
    }

    /* Primary Button Style */
    .stButton>button[kind="primary"] {
        background: linear-gradient(135deg, #38bdf8, #3b82f6);
        color: white;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    .stButton>button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }

    /* Secondary Button Style */
    .stButton>button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    .stButton>button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .stTextArea textarea {
        background-color: #1e293b; /* slate-800 */
        color: #f8fafc;
        border-color: #334155; /* slate-700 */
    }

    /* Glassmorphism Container */
    .glassmorphism {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 1rem;
        padding: 2rem;
        margin-bottom: 2rem;
    }

    /* Custom Header */
    .main-header {
        text-align: center;
        padding: 2rem;
    }
    .main-header h1 {
        font-size: 3rem;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #38bdf8, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* AI Voice Simulation */
    .ai-voice {
        background-color: #1e293b;
        border-left: 5px solid #38bdf8;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    
    /* Feedback container */
    .feedback-container {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 0.75rem;
    }
    
</style>
""", unsafe_allow_html=True)


# --- QUESTIONS DATA ---
questions = [
    {
        "section": "SQL", "type": "sql", "question": "Write a SQL query to find the top 3 customers by total order amount from the given tables.",
        "context": """<p class="mb-2 font-semibold">customers table:</p><pre>customer_id | name\n1 | John Doe\n2 | Jane Smith\n...</pre><p class="mt-4 mb-2 font-semibold">orders table:</p><pre>order_id | customer_id | amount\n101 | 1 | 500.00\n102 | 2 | 750.00\n...</pre>""",
        "voice_text": "For your first question: Write a SQL query to find the top 3 customers by total order amount. You'll need to join the customer and order tables, and use aggregation.",
    },
    {
        "section": "SQL", "type": "sql", "question": "Write a query to find employees who earn more than the average salary in their department.",
        "context": """<p class="font-semibold">employees table:</p><pre>emp_id | name | department | salary\n1 | Alice | Engineering | 90000\n2 | Bob | Engineering | 85000\n...</pre>""",
        "voice_text": "Next SQL question: Write a query to find employees who earn more than the average salary in their respective departments. Consider using a subquery or a window function.",
    },
    {
        "section": "Python", "type": "python", "question": "Write a Python function to find the second largest number in a list. Handle edge cases.",
        "context": """<pre><code>find_second_largest([1, 3, 4, 5, 2]) → 4\nfind_second_largest([1, 1, 1]) → None</code></pre>""",
        "voice_text": "Let's move to Python. Write a function to find the second largest number in a list. Remember to handle edge cases like lists with duplicates or fewer than two unique elements.",
    },
    {
        "section": "Python", "type": "python", "question": "Implement a function to reverse words in a sentence while keeping the word order intact.",
        "context": """<pre><code>reverse_words("Hello World Python") → "olleH dlroW nohtyP"</code></pre>""",
        "voice_text": "Another Python challenge: Implement a function that reverses each word in a sentence but keeps the order of the words the same.",
    },
    {
        "section": "Machine Learning", "type": "ml", "question": "Explain the difference between supervised and unsupervised learning with examples.",
        "context": "<p>Discuss data (labeled vs. unlabeled), goals (prediction vs. discovery), and provide examples of common algorithms for each.</p>",
        "voice_text": "Now for Machine Learning. Please explain the core differences between supervised and unsupervised learning. Include examples of algorithms and problems each type is suited for.",
    },
    {
        "section": "Machine Learning", "type": "ml", "question": "What is overfitting in machine learning and how can you prevent it?",
        "context": "<p>Describe what overfitting is, and discuss at least three common techniques to prevent it (e.g., regularization, cross-validation, dropout).</p>",
        "voice_text": "Final question: What is overfitting in machine learning? Explain how you would detect it and describe several common techniques used to prevent it.",
    }
]


# --- SESSION STATE INITIALIZATION ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {} # { 0: { "answer": "...", "score": 85, "feedback": "..." } }
if 'interview_started' not in st.session_state:
    st.session_state.interview_started = False
if 'interview_completed' not in st.session_state:
    st.session_state.interview_completed = False


# --- API CALL ---
def get_llm_feedback(question_text, answer):
    prompt = f"""
        You are an expert data science interview coach. Your role is to provide clear, constructive, and encouraging feedback to a student.
        The user was asked the following question:
        Question: "{question_text}"
        
        The user provided this answer:
        Answer: "{answer}"

        Your task is to analyze the user's answer.
        Please provide your response as a single, valid JSON object with two keys: "score" and "feedback".
        1.  "score": An integer between 0 and 100, representing the quality of the answer. A perfect answer is 100. A completely wrong or empty answer is 0.
        2.  "feedback": A string containing detailed, constructive feedback in Markdown format. The feedback should:
            - Start with a brief, one-sentence summary of the answer's quality.
            - Create a "Strengths" section listing what the user did well.
            - Create an "Areas for Improvement" section with specific, actionable suggestions.
            - Be encouraging and educational in tone.
    """
    
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"contents": [{"role": "user", "parts": [{"text": prompt}]}]})
    
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, data=payload)
        response.raise_for_status()
        result_json = response.json()
        
        feedback_text = result_json['candidates'][0]['content']['parts'][0]['text']
        feedback_text = feedback_text.replace('```json', '').replace('```', '').strip()
        
        return json.loads(feedback_text)
        
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: Could not connect to the API. Please check your connection. Details: {e}")
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        st.error(f"API response is not in the expected format. Please check your API key and the model's availability. Details: {e}")
        # Return a default error feedback structure
        return {"score": 0, "feedback": f"Could not parse the feedback from the AI. Error: {e}"}
    return None


# --- UI RENDERING FUNCTIONS ---
def display_welcome():
    st.markdown("""
    <div class="main-header">
        <h1>Advanced AI Interview Coach</h1>
        <p style="font-size: 1.2rem; color: #cbd5e1;">Hone your Data Science skills with AI-powered interviews and real-time, LLM-driven feedback.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="glassmorphism">', unsafe_allow_html=True)
        st.markdown("### 🎯 Interview Structure")
        st.markdown("""
        - **📊 2 SQL questions** on database querying and joins.
        - **🐍 2 Python questions** on logic and algorithms.
        - **🤖 2 Machine Learning questions** on core concepts.
        """)

        st.markdown('<p style="text-align: center; margin-top: 2rem;">Are you ready to begin?</p>', unsafe_allow_html=True)
        
        cols = st.columns([1, 1, 1])
        if cols[1].button("🚀 Start Interview", type="primary", use_container_width=True):
            st.session_state.interview_started = True
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)


def display_question():
    idx = st.session_state.current_question
    question = questions[idx]
    
    # Progress Bar
    progress = (idx + 1) / len(questions)
    st.progress(progress, text=f"Question {idx + 1} of {len(questions)} - {question['section']} Section")

    with st.container():
        st.markdown('<div class="glassmorphism">', unsafe_allow_html=True)
        
        # AI Voice Simulation
        st.markdown(f'<div class="ai-voice">🎤 <strong>AI Interviewer:</strong> <em>"{question["voice_text"]}"</em></div>', unsafe_allow_html=True)

        # Question Details
        st.markdown(f"### {question['question']}")
        st.markdown(question['context'], unsafe_allow_html=True)
        
        # Answer Area
        answer_key = f"answer_{idx}"
        saved_answer = st.session_state.user_answers.get(idx, {}).get("answer", "")
        answer = st.text_area("Your Answer:", value=saved_answer, height=200, key=answer_key, placeholder="Type your answer here...")

        # Update answer in session state as user types
        st.session_state.user_answers[idx] = st.session_state.user_answers.get(idx, {})
        st.session_state.user_answers[idx]['answer'] = answer
        
        # Buttons and Feedback
        submitted = (st.session_state.user_answers.get(idx, {}).get("score") is not None)
        
        if submitted:
            feedback_data = st.session_state.user_answers[idx]
            st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
            st.markdown(f"#### 🤖 AI Feedback (Score: {feedback_data['score']}/100)")
            st.markdown(feedback_data['feedback'])
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button("Get Feedback 🤖", type="primary"):
                if not answer.strip():
                    st.warning("Please provide an answer before getting feedback.")
                else:
                    with st.spinner("Analyzing your answer..."):
                        feedback = get_llm_feedback(question['question'], answer)
                        if feedback:
                            st.session_state.user_answers[idx].update(feedback)
                            st.rerun()
        
        # Navigation
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns([1, 5, 1])
        if idx > 0:
            if cols[0].button("⬅️ Previous", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
        
        if submitted:
            button_text = "Finish Interview 🏁" if idx == len(questions) - 1 else "Next ➡️"
            if cols[2].button(button_text, use_container_width=True):
                if idx == len(questions) - 1:
                    st.session_state.interview_completed = True
                else:
                    st.session_state.current_question += 1
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)


def display_analysis():
    st.markdown('<div class="main-header"><h1>📊 Interview Analysis</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="glassmorphism">', unsafe_allow_html=True)

    total_score = 0
    section_scores = {'SQL': [], 'Python': [], 'Machine Learning': []}
    
    for i in range(len(questions)):
        data = st.session_state.user_answers.get(i, {'score': 0})
        score = data.get('score', 0)
        total_score += score
        section_scores[questions[i]['section']].append(score)
        
    overall_score = total_score / len(questions)

    # Overall Score
    st.markdown(f'<h2 style="text-align: center;">Overall Performance: <span style="color:#38bdf8;">{overall_score:.0f}%</span></h2>', unsafe_allow_html=True)
    st.progress(overall_score / 100)

    # Section Scores
    st.markdown("### Performance by Section")
    cols = st.columns(3)
    icons = {'SQL': '📊', 'Python': '🐍', 'Machine Learning': '🤖'}
    for i, section in enumerate(section_scores):
        avg_score = sum(section_scores[section]) / len(section_scores[section])
        with cols[i]:
            st.markdown(f"**{icons[section]} {section}**")
            st.markdown(f"<h3 style='color:#818cf8;'>{avg_score:.0f}%</h3>", unsafe_allow_html=True)
            st.progress(avg_score/100)
    
    st.divider()

    # Detailed Analysis
    st.markdown("### Detailed Question Analysis")
    for i, q in enumerate(questions):
        data = st.session_state.user_answers.get(i, {})
        answer = data.get('answer', 'No answer provided.')
        score = data.get('score', 0)
        feedback = data.get('feedback', 'No feedback generated.')

        with st.expander(f"Q{i+1}: {q['section']} - {q['question']} (Score: {score})"):
            st.markdown("**Your Answer:**")
            st.info(answer)
            st.markdown("**AI Feedback:**")
            st.success(feedback)

    st.markdown('</div>', unsafe_allow_html=True)

    # Restart Button
    cols = st.columns([1, 1, 1])
    if cols[1].button("🔄 Take Interview Again", type="primary", use_container_width=True):
        # Reset session state
        st.session_state.clear()
        st.rerun()


# --- MAIN APP LOGIC ---
if not st.session_state.interview_started:
    display_welcome()
elif not st.session_state.interview_completed:
    display_question()
else:
    display_analysis()
