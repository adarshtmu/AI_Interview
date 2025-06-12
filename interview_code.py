import streamlit as st
import time
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Data Science Interview Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #2c3e50, #3498db);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .question-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin: 1rem 0;
    }
    
    .sql-table {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #ddd;
        margin: 1rem 0;
    }
    
    .score-card {
        background: linear-gradient(135deg, #3498db, #2c3e50);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .section-score {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    
    .stTextArea textarea {
        background-color: #1e1e1e;
        color: #d4d4d4;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'interview_started' not in st.session_state:
    st.session_state.interview_started = False
if 'interview_completed' not in st.session_state:
    st.session_state.interview_completed = False

# Questions data
questions = [
    {
        "section": "SQL",
        "type": "sql",
        "question": "Write a SQL query to find the top 3 customers by total order amount from the given tables.",
        "context": """
        **customers table:**
        | customer_id | name | email |
        |-------------|------|-------|
        | 1 | John Doe | john@email.com |
        | 2 | Jane Smith | jane@email.com |
        | 3 | Bob Johnson | bob@email.com |
        
        **orders table:**
        | order_id | customer_id | amount | order_date |
        |----------|-------------|--------|------------|
        | 101 | 1 | 500.00 | 2024-01-15 |
        | 102 | 2 | 750.00 | 2024-01-16 |
        | 103 | 1 | 300.00 | 2024-01-17 |
        """,
        "hint": "You'll need to JOIN the tables and use GROUP BY with SUM() and ORDER BY with LIMIT."
    },
    {
        "section": "SQL",
        "type": "sql",
        "question": "Write a query to find employees who earn more than the average salary in their department.",
        "context": """
        **employees table:**
        | emp_id | name | department | salary |
        |--------|------|------------|--------|
        | 1 | Alice | Engineering | 90000 |
        | 2 | Bob | Engineering | 85000 |
        | 3 | Carol | Sales | 70000 |
        | 4 | Dave | Sales | 65000 |
        """,
        "hint": "Use a subquery or window function to compare each employee's salary with their department average."
    },
    {
        "section": "Python",
        "type": "python",
        "question": "Write a Python function to find the second largest number in a list. Handle edge cases.",
        "context": """
        **Example:**
        ```python
        find_second_largest([1, 3, 4, 5, 2]) → 4
        find_second_largest([1, 1, 1]) → None
        ```
        """,
        "hint": "Consider using set() to handle duplicates and check list length."
    },
    {
        "section": "Python",
        "type": "python",
        "question": "Implement a function to reverse words in a sentence while keeping the word order intact.",
        "context": """
        **Example:**
        ```python
        reverse_words("Hello World Python") → "olleH dlroW nohtyP"
        ```
        """,
        "hint": "Split the sentence, reverse each word individually, then join them back."
    },
    {
        "section": "Machine Learning",
        "type": "ml",
        "question": "Explain the difference between supervised and unsupervised learning with examples.",
        "context": """
        **Think about:**
        - Key differences between the two approaches
        - Real-world examples of each
        - When to use each type
        """,
        "hint": "Consider labeled vs unlabeled data, and specific algorithms for each type."
    },
    {
        "section": "Machine Learning",
        "type": "ml",
        "question": "What is overfitting in machine learning and how can you prevent it?",
        "context": """
        **Consider discussing:**
        - Definition of overfitting
        - How to detect it
        - Prevention techniques
        - Validation strategies
        """,
        "hint": "Think about model complexity, training vs validation performance, and regularization techniques."
    }
]

def display_welcome():
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Data Science Interview Bot</h1>
        <p>Your AI-powered technical interview experience</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Welcome to Your Data Science Interview!
    
    I'm your AI interviewer today. We'll test your skills in Python, SQL, and Machine Learning.
    The interview consists of 6 questions total:
    
    - **2 SQL Questions** - Database querying and joins
    - **2 Python Questions** - Programming logic and algorithms  
    - **2 ML Questions** - Conceptual understanding
    
    Each question includes hints and context to guide you. Take your time and explain your reasoning!
    """)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Start Interview", type="primary", use_container_width=True):
            st.session_state.interview_started = True
            st.session_state.current_question = 0
            st.rerun()

def display_question():
    question = questions[st.session_state.current_question]
    
    # Progress bar
    progress = (st.session_state.current_question + 1) / len(questions)
    st.progress(progress, text=f"Question {st.session_state.current_question + 1} of {len(questions)} - {question['section']} Section")
    
    # Question container
    st.markdown(f"""
    <div class="question-container">
        <h3>📝 {question['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Context/Tables
    if question['context']:
        st.markdown("**Context:**")
        st.markdown(question['context'])
    
    # Answer input
    answer_key = f"answer_{st.session_state.current_question}"
    current_answer = st.session_state.user_answers.get(st.session_state.current_question, "")
    
    if question['type'] in ['sql', 'python']:
        answer = st.text_area(
            f"Your {question['type'].upper()} code:",
            value=current_answer,
            height=200,
            key=answer_key,
            placeholder=f"Write your {question['type'].upper()} code here..."
        )
    else:  # ML questions
        answer = st.text_area(
            "Your answer:",
            value=current_answer,
            height=150,
            key=answer_key,
            placeholder="Explain your answer in detail..."
        )
    
    # Save answer
    st.session_state.user_answers[st.session_state.current_question] = answer
    
    # Hint expander
    with st.expander("💡 Need a hint?"):
        st.info(question['hint'])
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_question < len(questions) - 1:
            if st.button("Next ➡️", type="primary", use_container_width=True):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("🏁 Finish Interview", type="primary", use_container_width=True):
                st.session_state.interview_completed = True
                st.rerun()

def calculate_scores():
    """Simulate scoring based on answer length and keywords"""
    scores = {}
    
    for i, question in enumerate(questions):
        answer = st.session_state.user_answers.get(i, "")
        base_score = min(len(answer.split()) * 5, 100)  # Basic scoring
        
        # Add keyword bonuses
        if question['section'] == 'SQL':
            keywords = ['SELECT', 'FROM', 'JOIN', 'GROUP BY', 'ORDER BY', 'WHERE']
            bonus = sum(10 for kw in keywords if kw.lower() in answer.lower())
            scores[i] = min(base_score + bonus, 100)
        elif question['section'] == 'Python':
            keywords = ['def', 'return', 'if', 'for', 'while', 'try', 'except']
            bonus = sum(8 for kw in keywords if kw in answer)
            scores[i] = min(base_score + bonus, 100)
        else:  # ML
            keywords = ['supervised', 'unsupervised', 'training', 'validation', 'overfitting']
            bonus = sum(12 for kw in keywords if kw.lower() in answer.lower())
            scores[i] = min(base_score + bonus, 100)
    
    return scores

def display_analysis():
    st.markdown("""
    <div class="main-header">
        <h1>📊 Interview Analysis</h1>
        <p>Your performance breakdown and feedback</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate scores
    scores = calculate_scores()
    
    # Section averages
    sql_scores = [scores.get(i, 0) for i in range(2)]
    python_scores = [scores.get(i, 0) for i in range(2, 4)]
    ml_scores = [scores.get(i, 0) for i in range(4, 6)]
    
    avg_sql = sum(sql_scores) / len(sql_scores) if sql_scores else 0
    avg_python = sum(python_scores) / len(python_scores) if python_scores else 0
    avg_ml = sum(ml_scores) / len(ml_scores) if ml_scores else 0
    overall = (avg_sql + avg_python + avg_ml) / 3
    
    # Overall score card
    st.markdown(f"""
    <div class="score-card">
        <h1 style="font-size: 4em; margin: 0;">{overall:.0f}%</h1>
        <p style="font-size: 1.5em; margin: 0;">Overall Performance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Section scores
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="section-score">
            <h3>🐍 Python Skills</h3>
            <h2>{avg_python:.0f}%</h2>
            <p>Code quality and logic</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_python/100)
    
    with col2:
        st.markdown(f"""
        <div class="section-score">
            <h3>🗃️ SQL Knowledge</h3>
            <h2>{avg_sql:.0f}%</h2>
            <p>Query writing skills</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_sql/100)
    
    with col3:
        st.markdown(f"""
        <div class="section-score">
            <h3>🤖 Machine Learning</h3>
            <h2>{avg_ml:.0f}%</h2>
            <p>Conceptual understanding</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_ml/100)
    
    # Detailed feedback
    st.markdown("### 📝 Detailed Feedback")
    
    feedback = []
    if avg_sql >= 70:
        feedback.append("✅ Strong SQL skills demonstrated with proper query structure")
    else:
        feedback.append("📝 SQL queries need improvement in optimization and structure")
    
    if avg_python >= 70:
        feedback.append("✅ Good Python programming logic and code organization")
    else:
        feedback.append("📝 Python solutions could benefit from better error handling")
    
    if avg_ml >= 70:
        feedback.append("✅ Solid understanding of ML concepts and practical applications")
    else:
        feedback.append("📝 Machine learning concepts need deeper understanding")
    
    feedback.append("🎯 Overall performance shows good technical foundation")
    feedback.append("💡 Continue practicing coding problems and ML theory")
    
    for item in feedback:
        st.markdown(f"- {item}")
    
    # Question by question breakdown
    with st.expander("📋 Question-by-Question Breakdown"):
        for i, question in enumerate(questions):
            score = scores.get(i, 0)
            answer = st.session_state.user_answers.get(i, "No answer provided")
            
            st.markdown(f"**Q{i+1}: {question['section']} - Score: {score:.0f}%**")
            st.markdown(f"*{question['question'][:100]}...*")
            st.code(answer[:200] + "..." if len(answer) > 200 else answer)
            st.divider()
    
    # Restart button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Take Interview Again", type="primary", use_container_width=True):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Main app logic
def main():
    if not st.session_state.interview_started:
        display_welcome()
    elif not st.session_state.interview_completed:
        display_question()
    else:
        display_analysis()

if __name__ == "__main__":
    main()
