import streamlit as st
import time
import random
from datetime import datetime
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Data Science Interview Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling and visibility
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
        background: #ffffff;
        color: #2c3e50;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .question-container h3 {
        color: #2c3e50 !important;
        font-size: 1.3em;
        margin-bottom: 1rem;
    }
    
    .sql-table-container {
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
        color: #2c3e50;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 0.5rem 0;
    }
    
    .voice-container {
        background: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #3498db;
    }
    
    .ai-feedback {
        background: #f0f8f0;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #27ae60;
    }
    
    /* Fix text visibility */
    .stMarkdown, .stText {
        color: #2c3e50 !important;
    }
    
    .element-container {
        color: #2c3e50 !important;
    }
    
    /* Make sure tables are visible */
    table {
        background: white !important;
        color: #2c3e50 !important;
    }
    
    th {
        background: #3498db !important;
        color: white !important;
    }
    
    td {
        background: white !important;
        color: #2c3e50 !important;
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
if 'ai_feedback' not in st.session_state:
    st.session_state.ai_feedback = {}

# Questions data
questions = [
    {
        "section": "SQL",
        "type": "sql",
        "question": "Write a SQL query to find the top 3 customers by total order amount from the given tables.",
        "context": {
            "customers": [
                {"customer_id": 1, "name": "John Doe", "email": "john@email.com"},
                {"customer_id": 2, "name": "Jane Smith", "email": "jane@email.com"},
                {"customer_id": 3, "name": "Bob Johnson", "email": "bob@email.com"},
                {"customer_id": 4, "name": "Alice Brown", "email": "alice@email.com"}
            ],
            "orders": [
                {"order_id": 101, "customer_id": 1, "amount": 500.00, "order_date": "2024-01-15"},
                {"order_id": 102, "customer_id": 2, "amount": 750.00, "order_date": "2024-01-16"},
                {"order_id": 103, "customer_id": 1, "amount": 300.00, "order_date": "2024-01-17"},
                {"order_id": 104, "customer_id": 3, "amount": 900.00, "order_date": "2024-01-18"},
                {"order_id": 105, "customer_id": 2, "amount": 400.00, "order_date": "2024-01-19"}
            ]
        },
        "hint": "You'll need to JOIN the tables and use GROUP BY with SUM() and ORDER BY with LIMIT.",
        "voice_text": "For this SQL question, examine the customers and orders tables shown. Write a query to find the top 3 customers by their total order amount. You'll need to join the tables and use aggregation functions.",
        "expected_keywords": ["SELECT", "FROM", "JOIN", "GROUP BY", "SUM", "ORDER BY", "LIMIT"]
    },
    {
        "section": "SQL",
        "type": "sql",
        "question": "Write a query to find employees who earn more than the average salary in their department.",
        "context": {
            "employees": [
                {"emp_id": 1, "name": "Alice", "department": "Engineering", "salary": 90000},
                {"emp_id": 2, "name": "Bob", "department": "Engineering", "salary": 85000},
                {"emp_id": 3, "name": "Carol", "department": "Sales", "salary": 70000},
                {"emp_id": 4, "name": "Dave", "department": "Sales", "salary": 65000},
                {"emp_id": 5, "name": "Eve", "department": "Engineering", "salary": 95000},
                {"emp_id": 6, "name": "Frank", "department": "Sales", "salary": 72000}
            ]
        },
        "hint": "Use a subquery or window function to compare each employee's salary with their department average.",
        "voice_text": "This SQL question requires you to find employees earning above their department's average salary. You'll need to use a subquery or window function to compare each employee's salary with their department average.",
        "expected_keywords": ["SELECT", "FROM", "WHERE", "AVG", "GROUP BY", "HAVING", "subquery"]
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
find_second_largest([5]) → None
```
        """,
        "hint": "Consider using set() to handle duplicates and check list length.",
        "voice_text": "Write a Python function called find_second_largest that takes a list of numbers and returns the second largest unique number. Make sure to handle edge cases like duplicate numbers or lists with fewer than 2 unique elements.",
        "expected_keywords": ["def", "return", "if", "len", "set", "sorted", "max"]
    },
    {
        "section": "Python",
        "type": "python",
        "question": "Implement a function to reverse words in a sentence while keeping the word order intact.",
        "context": """
**Example:**
```python
reverse_words("Hello World Python") → "olleH dlroW nohtyP"
reverse_words("Data Science") → "ataD ecneicS"
```
        """,
        "hint": "Split the sentence, reverse each word individually, then join them back.",
        "voice_text": "Create a Python function that reverses each individual word in a sentence while maintaining the original word order. So 'Hello World' becomes 'olleH dlroW'.",
        "expected_keywords": ["def", "split", "join", "return", "for", "reversed"]
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
- Types of problems each solves
        """,
        "hint": "Consider labeled vs unlabeled data, and specific algorithms for each type.",
        "voice_text": "Let's discuss machine learning concepts. Explain the key differences between supervised and unsupervised learning. Provide examples of each and describe when you would use one approach over the other.",
        "expected_keywords": ["supervised", "unsupervised", "labeled", "unlabeled", "classification", "regression", "clustering"]
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
- Impact on model performance
        """,
        "hint": "Think about model complexity, training vs validation performance, and regularization techniques.",
        "voice_text": "Now let's talk about overfitting. Explain what overfitting means in machine learning, how you can detect it, and what techniques you would use to prevent it. Include your thoughts on validation strategies.",
        "expected_keywords": ["overfitting", "validation", "regularization", "cross-validation", "dropout", "early stopping"]
    }
]

def text_to_speech_simulation(text):
    """Simulate text-to-speech with visual feedback"""
    with st.container():
        st.markdown(f"""
        <div class="voice-container">
            <h4>🎤 AI Interviewer Says:</h4>
            <p><em>"{text}"</em></p>
            <small>🔊 Voice guidance (simulated)</small>
        </div>
        """, unsafe_allow_html=True)

def generate_ai_feedback(question, answer):
    """Generate AI feedback for the answer"""
    if not answer.strip():
        return "⚠️ No answer provided. Please attempt the question to receive feedback."
    
    question_data = questions[question]
    keywords_found = sum(1 for keyword in question_data["expected_keywords"] 
                        if keyword.lower() in answer.lower())
    
    feedback_parts = []
    
    # Basic assessment
    if len(answer.split()) < 10:
        feedback_parts.append("📝 **Length**: Your answer seems quite brief. Consider providing more detailed explanation.")
    else:
        feedback_parts.append("✅ **Length**: Good detailed response.")
    
    # Keyword analysis
    keyword_score = (keywords_found / len(question_data["expected_keywords"])) * 100
    if keyword_score >= 60:
        feedback_parts.append(f"✅ **Keywords**: Strong use of relevant terminology ({keywords_found}/{len(question_data['expected_keywords'])} key concepts)")
    elif keyword_score >= 30:
        feedback_parts.append(f"📝 **Keywords**: Some relevant terms used ({keywords_found}/{len(question_data['expected_keywords'])}). Consider including more technical vocabulary.")
    else:
        feedback_parts.append(f"⚠️ **Keywords**: Few relevant terms detected ({keywords_found}/{len(question_data['expected_keywords'])}). Review the key concepts for this topic.")
    
    # Section-specific feedback
    if question_data["section"] == "SQL":
        if any(word in answer.upper() for word in ["SELECT", "FROM"]):
            feedback_parts.append("✅ **SQL Structure**: Good basic query structure.")
        if "JOIN" in answer.upper():
            feedback_parts.append("✅ **Joins**: Correctly identified need for table joins.")
        if not any(word in answer.upper() for word in ["GROUP BY", "ORDER BY"]):
            feedback_parts.append("📝 **Aggregation**: Consider using GROUP BY and ORDER BY clauses.")
            
    elif question_data["section"] == "Python":
        if "def" in answer:
            feedback_parts.append("✅ **Function**: Good function definition structure.")
        if any(word in answer for word in ["if", "else", "try", "except"]):
            feedback_parts.append("✅ **Logic**: Good use of conditional logic and error handling.")
        if "return" not in answer:
            feedback_parts.append("📝 **Return**: Don't forget to return the result from your function.")
            
    elif question_data["section"] == "Machine Learning":
        if len(answer.split()) >= 50:
            feedback_parts.append("✅ **Depth**: Comprehensive explanation provided.")
        if any(word in answer.lower() for word in ["example", "such as", "like"]):
            feedback_parts.append("✅ **Examples**: Good use of examples to illustrate concepts.")
    
    # Generate improvement suggestions
    suggestions = []
    if keyword_score < 50:
        suggestions.append(f"💡 Try incorporating these key terms: {', '.join(question_data['expected_keywords'][:3])}")
    
    if question_data["section"] == "SQL" and "JOIN" not in answer.upper():
        suggestions.append("💡 This problem likely requires joining multiple tables")
    
    if question_data["section"] == "Python" and "def" not in answer:
        suggestions.append("💡 Structure your solution as a proper function with def and return")
    
    if suggestions:
        feedback_parts.append("**Suggestions:**")
        feedback_parts.extend(suggestions)
    
    return "\n\n".join(feedback_parts)

def display_welcome():
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Data Science Interview Bot</h1>
        <p>Your AI-powered technical interview experience with voice guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Interviewer Introduction
    text_to_speech_simulation("Hello! Welcome to your data science interview. I'm your AI interviewer today, and I'll guide you through 6 technical questions covering SQL, Python, and Machine Learning. After each answer, I'll provide detailed feedback to help you improve. Are you ready to begin?")
    
    st.markdown("""
    ### 🎯 Interview Structure
    
    **📊 2 SQL Questions** - Database querying and joins  
    **🐍 2 Python Questions** - Programming logic and algorithms  
    **🤖 2 ML Questions** - Conceptual understanding  
    
    ### ✨ Features
    - **🎤 Voice Guidance** - AI interviewer speaks each question
    - **🤖 Real-time Feedback** - Instant AI analysis of your answers
    - **📈 Smart Scoring** - Advanced assessment algorithm
    - **📊 Detailed Analysis** - Comprehensive performance breakdown
    """)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀 Start Interview", type="primary", use_container_width=True):
            st.session_state.interview_started = True
            st.session_state.current_question = 0
            st.rerun()

def display_sql_tables(context):
    """Display SQL tables in a readable format"""
    if "customers" in context:
        st.markdown("**📋 customers table:**")
        st.dataframe(context["customers"], use_container_width=True)
    
    if "orders" in context:
        st.markdown("**📋 orders table:**")
        st.dataframe(context["orders"], use_container_width=True)
        
    if "employees" in context:
        st.markdown("**📋 employees table:**")
        st.dataframe(context["employees"], use_container_width=True)

def display_question():
    question = questions[st.session_state.current_question]
    
    # Progress bar
    progress = (st.session_state.current_question + 1) / len(questions)
    st.progress(progress, text=f"Question {st.session_state.current_question + 1} of {len(questions)} - {question['section']} Section")
    
    # Voice guidance for question
    if st.button("🎤 Listen to Question", type="secondary"):
        text_to_speech_simulation(question['voice_text'])
    
    # Question container with better visibility
    st.markdown(f"""
    <div class="question-container">
        <h3>📝 Question {st.session_state.current_question + 1}: {question['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Context/Tables
    if question['type'] == 'sql' and isinstance(question['context'], dict):
        st.markdown("**📊 Database Tables:**")
        display_sql_tables(question['context'])
    elif question['context']:
        st.markdown("**📖 Context:**")
        st.markdown(question['context'])
    
    # Answer input
    answer_key = f"answer_{st.session_state.current_question}"
    current_answer = st.session_state.user_answers.get(st.session_state.current_question, "")
    
    if question['type'] in ['sql', 'python']:
        answer = st.text_area(
            f"✍️ Your {question['type'].upper()} code:",
            value=current_answer,
            height=200,
            key=answer_key,
            placeholder=f"Write your {question['type'].upper()} code here..."
        )
    else:  # ML questions
        answer = st.text_area(
            "✍️ Your detailed answer:",
            value=current_answer,
            height=150,
            key=answer_key,
            placeholder="Explain your answer in detail with examples..."
        )
    
    # Save answer
    st.session_state.user_answers[st.session_state.current_question] = answer
    
    # Generate AI feedback if answer exists
    if answer.strip():
        if st.button("🤖 Get AI Feedback", type="secondary"):
            feedback = generate_ai_feedback(st.session_state.current_question, answer)
            st.session_state.ai_feedback[st.session_state.current_question] = feedback
    
    # Display AI feedback if available
    if st.session_state.current_question in st.session_state.ai_feedback:
        st.markdown(f"""
        <div class="ai-feedback">
            <h4>🤖 AI Interviewer Feedback:</h4>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(st.session_state.ai_feedback[st.session_state.current_question])
    
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

def calculate_advanced_scores():
    """Advanced scoring with AI feedback integration"""
    scores = {}
    
    for i, question in enumerate(questions):
        answer = st.session_state.user_answers.get(i, "")
        
        if not answer.strip():
            scores[i] = 0
            continue
            
        # Base score from answer length (max 40 points)
        word_count = len(answer.split())
        length_score = min(word_count * 2, 40)
        
        # Keyword matching (max 30 points)
        keywords_found = sum(1 for keyword in question["expected_keywords"] 
                           if keyword.lower() in answer.lower())
        keyword_score = (keywords_found / len(question["expected_keywords"])) * 30
        
        # Section-specific scoring (max 30 points)
        section_score = 0
        if question["section"] == "SQL":
            sql_commands = ["SELECT", "FROM", "JOIN", "WHERE", "GROUP BY", "ORDER BY", "HAVING"]
            sql_found = sum(1 for cmd in sql_commands if cmd in answer.upper())
            section_score = min(sql_found * 5, 30)
            
        elif question["section"] == "Python":
            python_features = ["def", "return", "if", "for", "while", "try", "except", "class"]
            python_found = sum(1 for feature in python_features if feature in answer)
            section_score = min(python_found * 4, 30)
            
        elif question["section"] == "Machine Learning":
            # For ML, reward comprehensive explanations
            if word_count >= 100:
                section_score = 30
            elif word_count >= 50:
                section_score = 20
            else:
                section_score = 10
        
        # Total score (max 100)
        total_score = min(length_score + keyword_score + section_score, 100)
        scores[i] = total_score
    
    return scores

def display_analysis():
    # AI Interviewer final message
    text_to_speech_simulation("Congratulations! You've completed the interview. Let me analyze your performance and provide comprehensive feedback on your technical skills.")
    
    st.markdown("""
    <div class="main-header">
        <h1>📊 Interview Analysis</h1>
        <p>Comprehensive AI-powered performance evaluation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate advanced scores
    scores = calculate_advanced_scores()
    
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
        <p style="font-size: 1em; margin: 0; opacity: 0.8;">AI-Assessed Technical Competency</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Performance interpretation
    if overall >= 80:
        performance_msg = "🎉 **Excellent Performance!** You demonstrate strong technical skills across all areas."
        text_to_speech_simulation("Excellent work! You've shown strong technical competency across SQL, Python, and Machine Learning concepts.")
    elif overall >= 65:
        performance_msg = "👍 **Good Performance!** Solid foundation with room for improvement in some areas."
        text_to_speech_simulation("Good job! You have a solid technical foundation. Focus on the areas highlighted in the feedback to further improve.")
    elif overall >= 50:
        performance_msg = "📚 **Developing Skills.** You're on the right track, keep practicing!"
        text_to_speech_simulation("You're making progress! Continue practicing and studying the concepts to strengthen your technical skills.")
    else:
        performance_msg = "💪 **Keep Learning!** Focus on fundamentals and practice regularly."
        text_to_speech_simulation("Keep up the learning! Focus on building strong fundamentals in each area through regular practice.")
    
    st.markdown(performance_msg)
    
    # Section scores
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="section-score">
            <h3>🗃️ SQL Knowledge</h3>
            <h2>{avg_sql:.0f}%</h2>
            <p>Query writing and database concepts</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_sql/100)
    
    with col2:
        st.markdown(f"""
        <div class="section-score">
            <h3>🐍 Python Skills</h3>
            <h2>{avg_python:.0f}%</h2>
            <p>Programming logic and algorithms</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_python/100)
    
    with col3:
        st.markdown(f"""
        <div class="section-score">
            <h3>🤖 Machine Learning</h3>
            <h2>{avg_ml:.0f}%</h2>
            <p>Conceptual understanding</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(avg_ml/100)
    
    # AI Comprehensive Feedback
    st.markdown("### 🤖 AI Interviewer's Comprehensive Assessment")
    
    comprehensive_feedback = []
    
    # SQL Assessment
    if avg_sql >= 75:
        comprehensive_feedback.append("**🗃️ SQL Mastery**: Excellent understanding of database concepts and query optimization.")
    elif avg_sql >= 50:
        comprehensive_feedback.append("**🗃️ SQL Development**: Good foundation, focus on complex joins and aggregations.")
    else:
        comprehensive_feedback.append("**🗃️ SQL Learning**: Practice basic queries, joins, and grouping operations.")
    
    # Python Assessment
    if avg_python >= 75:
        comprehensive_feedback.append("**🐍 Python Proficiency**: Strong programming logic and algorithmic thinking.")
    elif avg_python >= 50:
        comprehensive_feedback.append("**🐍 Python Growth**: Good problem-solving approach, work on edge cases and optimization.")
    else:
        comprehensive_feedback.append("**🐍 Python Foundation**: Focus on basic syntax, functions, and control structures.")
    
    # ML Assessment
    if avg_ml >= 75:
        comprehensive_feedback.append("**🤖 ML Expertise**: Solid grasp of machine learning concepts and applications.")
    elif avg_ml >= 50:
        comprehensive_feedback.append("**🤖 ML Understanding**: Good conceptual knowledge, deepen practical applications.")
    else:
        comprehensive_feedback.append("**🤖 ML Basics**: Study fundamental concepts, supervised vs unsupervised learning.")
    
    # Overall recommendations
    comprehensive_feedback.append("**🎯 Next Steps**: Continue practicing coding challenges and stay updated with latest ML techniques.")
    comprehensive_feedback.append("**📚 Resources**: Consider online courses, coding platforms, and hands-on projects.")
    
    for feedback in comprehensive_feedback:
        st.markdown(f"- {feedback}")
    
    # Question-by-question breakdown with AI feedback
    with st.expander("📋 Detailed Question Analysis"):
        for i, question in enumerate(questions):
            score = scores.get(i, 0)
            answer = st.session_state.user_answers.get(i, "No answer provided")
            ai_feedback = st.session_state.ai_feedback.get(i, "No AI feedback generated")
            
            st.markdown(f"### Q{i+1}: {question['section']} - Score: {score:.0f}%")
            st.markdown(f"**Question:** {question['question']}")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**Your Answer:**")
                st.code(answer[:300] + "..." if len(answer) > 300 else answer)
            
            with col2:
                st.markdown("**AI Feedback:**")
                st.markdown(ai_feedback)
            
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
