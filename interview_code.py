import streamlit as st
import time
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    }
    
    .question-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 1rem;
    }
    
    .score-display {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #065f46, #047857);
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    .section-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .sql-badge { background: linear-gradient(135deg, #f59e0b, #d97706); }
    .python-badge { background: linear-gradient(135deg, #10b981, #059669); }
    .ml-badge { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
</style>
""", unsafe_allow_html=True)

# Interview questions data
QUESTIONS = [
    {
        "section": "SQL",
        "type": "sql",
        "question": "Write a SQL query to find the top 3 customers by total order amount from the given tables.",
        "context": """**customers table:**
```
customer_id | name
1 | John Doe
2 | Jane Smith
...
```

**orders table:**
```
order_id | customer_id | amount
101 | 1 | 500.00
102 | 2 | 750.00
...
```""",
    },
    {
        "section": "SQL",
        "type": "sql", 
        "question": "Write a query to find employees who earn more than the average salary in their department.",
        "context": """**employees table:**
```
emp_id | name | department | salary
1 | Alice | Engineering | 90000
2 | Bob | Engineering | 85000
...
```""",
    },
    {
        "section": "Python",
        "type": "python",
        "question": "Write a Python function to find the second largest number in a list. Handle edge cases.",
        "context": """```python
find_second_largest([1, 3, 4, 5, 2]) → 4
find_second_largest([1, 1, 1]) → None
```""",
    },
    {
        "section": "Python", 
        "type": "python",
        "question": "Implement a function to reverse words in a sentence while keeping the word order intact.",
        "context": """```python
reverse_words("Hello World Python") → "olleH dlroW nohtyP"
```""",
    },
    {
        "section": "Machine Learning",
        "type": "ml",
        "question": "Explain the difference between supervised and unsupervised learning with examples.",
        "context": "Discuss data (labeled vs. unlabeled), goals (prediction vs. discovery), and provide examples of common algorithms for each.",
    },
    {
        "section": "Machine Learning",
        "type": "ml", 
        "question": "What is overfitting in machine learning and how can you prevent it?",
        "context": "Describe what overfitting is, and discuss at least three common techniques to prevent it (e.g., regularization, cross-validation, dropout).",
    }
]

def generate_feedback(question, answer):
    """Generate mock AI feedback"""
    score = random.randint(60, 100)
    
    feedbacks = {
        "SQL": {
            "high": "**Excellent SQL Skills!** ✨\n\n**Strengths:**\n- Proper use of JOIN operations\n- Correct aggregation functions\n- Good understanding of GROUP BY and ORDER BY",
            "medium": "**Good SQL Foundation** 📊\n\n**Strengths:**\n- Basic query structure is correct\n- Shows understanding of table relationships",
            "low": "**Keep Learning SQL** 💪\n\n**Strengths:**\n- Shows effort and basic understanding"
        },
        "Python": {
            "high": "**Outstanding Python Code!** 🐍\n\n**Strengths:**\n- Clean, readable code\n- Proper error handling\n- Efficient algorithm choice",
            "medium": "**Solid Python Skills** 🔧\n\n**Strengths:**\n- Logic is mostly correct\n- Shows problem-solving ability",
            "low": "**Python Practice Needed** 📚\n\n**Strengths:**\n- Shows understanding of basic concepts"
        },
        "Machine Learning": {
            "high": "**Excellent ML Knowledge!** 🧠\n\n**Strengths:**\n- Deep understanding of concepts\n- Good real-world examples",
            "medium": "**Good ML Foundation** 📈\n\n**Strengths:**\n- Understands core concepts\n- Provides relevant examples",
            "low": "**ML Learning Journey** 🚀\n\n**Strengths:**\n- Shows interest in the field"
        }
    }
    
    level = "high" if score >= 80 else "medium" if score >= 65 else "low"
    section = question["section"]
    
    return {
        "score": score,
        "feedback": feedbacks[section][level]
    }

def main():
    # Initialize session state
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.started = False
        st.session_state.completed = False
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Advanced AI Interview Coach</h1>
        <p>Master Data Science with AI-Powered Feedback & Real-Time Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.started:
        show_welcome_screen()
    elif st.session_state.completed:
        show_results_screen()
    else:
        show_interview_screen()

def show_welcome_screen():
    st.markdown("## 🎯 Interview Structure")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🗄️ SQL Mastery
        2 Advanced database queries and optimization challenges
        """)
    
    with col2:
        st.markdown("""
        ### 🐍 Python Expertise  
        2 Algorithm and data structure problems
        """)
    
    with col3:
        st.markdown("""
        ### 🧠 ML Concepts
        2 Machine learning theory and applications
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📊 Real-time Analysis
        Instant AI feedback with detailed scoring
        """)
    
    with col2:
        st.markdown("""
        ### 🏆 Performance Tracking
        Comprehensive analytics and improvement tips
        """)
    
    with col3:
        st.markdown("""
        ### 🚀 Interactive Experience
        Streamlined interface for optimal learning
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Launch Interview Experience", type="primary", use_container_width=True):
            st.session_state.started = True
            st.rerun()

def show_interview_screen():
    current_q = st.session_state.current_question
    question = QUESTIONS[current_q]
    
    # Progress bar
    progress = (current_q + 1) / len(QUESTIONS)
    st.progress(progress, text=f"Question {current_q + 1} of {len(QUESTIONS)} - {question['section']} Section")
    
    # Section badge
    badge_class = f"{question['section'].lower().replace(' ', '-')}-badge"
    st.markdown(f"""
    <div class="section-badge {badge_class}">
        {question['section']}
    </div>
    """, unsafe_allow_html=True)
    
    # Question display
    st.markdown(f"## {question['question']}")
    
    with st.expander("📋 Context & Requirements", expanded=True):
        st.markdown(question['context'])
    
    # Answer input
    answer_key = f"answer_{current_q}"
    answer = st.text_area(
        "✍️ Your Solution:",
        height=200,
        placeholder="Type your detailed answer here... The AI will analyze your response for technical accuracy, clarity, and completeness.",
        key=answer_key,
        value=st.session_state.answers.get(current_q, {}).get('answer', '')
    )
    
    # Save answer
    if current_q not in st.session_state.answers:
        st.session_state.answers[current_q] = {}
    st.session_state.answers[current_q]['answer'] = answer
    
    # Feedback button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🧠 Get AI Analysis", type="primary", use_container_width=True):
            if answer.strip():
                with st.spinner("🔍 AI is analyzing your response..."):
                    time.sleep(2)  # Simulate AI processing
                    feedback = generate_feedback(question, answer)
                    st.session_state.answers[current_q].update(feedback)
                    st.rerun()
            else:
                st.error("Please provide an answer before getting feedback.")
    
    # Display feedback if available
    if 'score' in st.session_state.answers.get(current_q, {}):
        feedback_data = st.session_state.answers[current_q]
        
        st.markdown(f"""
        <div class="score-display">
            <h2>🎯 AI Analysis Complete</h2>
            <h1 style="color: #10b981; font-size: 3rem;">{feedback_data['score']}%</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(feedback_data['feedback'])
    
    # Navigation
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if current_q > 0:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col3:
        if 'score' in st.session_state.answers.get(current_q, {}):
            if current_q < len(QUESTIONS) - 1:
                if st.button("Next ➡️", type="primary", use_container_width=True):
                    st.session_state.current_question += 1
                    st.rerun()
            else:
                if st.button("🏁 Complete Interview", type="primary", use_container_width=True):
                    st.session_state.completed = True
                    st.rerun()

def show_results_screen():
    st.markdown("# 📊 Interview Analysis Report")
    st.markdown("### Comprehensive AI-Generated Performance Assessment")
    
    # Calculate overall score
    scores = [data.get('score', 0) for data in st.session_state.answers.values() if 'score' in data]
    overall_score = sum(scores) / len(scores) if scores else 0
    
    # Overall score display
    st.markdown(f"""
    <div class="score-display">
        <h2>🎯 Overall Performance</h2>
        <h1 style="color: #10b981; font-size: 4rem;">{overall_score:.0f}%</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Section breakdown
    st.markdown("## 📈 Section Performance")
    
    sections = {"SQL": [], "Python": [], "Machine Learning": []}
    
    for i, question in enumerate(QUESTIONS):
        if i in st.session_state.answers and 'score' in st.session_state.answers[i]:
            sections[question['section']].append(st.session_state.answers[i]['score'])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sql_avg = sum(sections["SQL"]) / len(sections["SQL"]) if sections["SQL"] else 0
        st.metric("🗄️ SQL", f"{sql_avg:.0f}%")
    
    with col2:
        python_avg = sum(sections["Python"]) / len(sections["Python"]) if sections["Python"] else 0
        st.metric("🐍 Python", f"{python_avg:.0f}%")
    
    with col3:
        ml_avg = sum(sections["Machine Learning"]) / len(sections["Machine Learning"]) if sections["Machine Learning"] else 0
        st.metric("🧠 ML", f"{ml_avg:.0f}%")
    
    # Detailed results
    with st.expander("📋 Detailed Question Analysis"):
        for i, question in enumerate(QUESTIONS):
            if i in st.session_state.answers and 'score' in st.session_state.answers[i]:
                st.markdown(f"**Question {i+1} ({question['section']}):** {st.session_state.answers[i]['score']}%")
                st.markdown(f"*{question['question']}*")
                st.markdown("---")
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Take Another Interview", use_container_width=True):
            # Reset session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    with col2:
        if st.button("📄 Download Report", use_container_width=True):
            report = generate_report()
            st.download_button(
                label="💾 Download Text Report",
                data=report,
                file_name=f"interview-report-{datetime.now().strftime('%Y-%m-%d')}.txt",
                mime="text/plain"
            )

def generate_report():
    """Generate a text report"""
    report = "AI Interview Coach - Performance Report\n"
    report += "=====================================\n\n"
    
    scores = [data.get('score', 0) for data in st.session_state.answers.values() if 'score' in data]
    overall_score = sum(scores) / len(scores) if scores else 0
    
    report += f"Overall Score: {overall_score:.0f}%\n"
    report += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    for i, question in enumerate(QUESTIONS):
        if i in st.session_state.answers:
            answer_data = st.session_state.answers[i]
            report += f"Question {i+1} ({question['section']}):\n"
            report += f"{question['question']}\n\n"
            report += f"Your Answer:\n{answer_data.get('answer', 'No answer provided')}\n\n"
            if 'score' in answer_data:
                report += f"Score: {answer_data['score']}/100\n"
                report += f"Feedback: {answer_data['feedback']}\n\n"
            report += "---\n\n"
    
    return report

if __name__ == "__main__":
    main()
