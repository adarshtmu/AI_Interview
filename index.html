<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced AI Interview Coach</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            color: #f8fafc;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            padding: 2rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            margin-bottom: 2rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .header h1 {
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(45deg, #60a5fa, #34d399, #fbbf24);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.2); }
        }

        .subtitle {
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 1rem;
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(16px);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }

        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.4);
        }

        .progress-container {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 50px;
            padding: 4px;
            margin-bottom: 2rem;
        }

        .progress-bar {
            height: 12px;
            background: linear-gradient(90deg, #60a5fa, #34d399);
            border-radius: 50px;
            transition: width 0.5s ease;
            position: relative;
        }

        .progress-text {
            text-align: center;
            margin-top: 0.5rem;
            font-weight: 600;
            color: #e2e8f0;
        }

        .ai-voice-container {
            background: linear-gradient(135deg, #1e40af, #7c3aed);
            border-radius: 15px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }

        .ai-voice-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            animation: shimmer 2s infinite;
        }

        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        .ai-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(45deg, #60a5fa, #34d399);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-right: 1rem;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .ai-message {
            display: flex;
            align-items: center;
            color: white;
            font-weight: 500;
        }

        .voice-controls {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .voice-btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 25px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }

        .voice-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }

        .voice-btn.active {
            background: #10b981;
        }

        .question-section {
            background: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #60a5fa;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
        }

        .question-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #f1f5f9;
            margin-bottom: 1rem;
        }

        .question-context {
            background: rgba(0, 0, 0, 0.3);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            font-family: 'Monaco', monospace;
            color: #e2e8f0;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .answer-container {
            margin-bottom: 2rem;
        }

        .answer-textarea {
            width: 100%;
            min-height: 200px;
            background: rgba(0, 0, 0, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 1rem;
            color: #f8fafc;
            font-size: 1rem;
            font-family: inherit;
            resize: vertical;
            transition: all 0.3s ease;
        }

        .answer-textarea:focus {
            outline: none;
            border-color: #60a5fa;
            box-shadow: 0 0 20px rgba(96, 165, 250, 0.3);
        }

        .answer-textarea::placeholder {
            color: #94a3b8;
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: white;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(59, 130, 246, 0.6);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: #f8fafc;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.2);
            border-color: rgba(255, 255, 255, 0.5);
        }

        .btn-success {
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
        }

        .navigation {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 2rem;
        }

        .feedback-container {
            background: linear-gradient(135deg, #065f46, #047857);
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 2rem;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        .score-display {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .score-circle {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: conic-gradient(#10b981 0deg, #10b981 var(--score-deg), #374151 var(--score-deg), #374151 360deg);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: white;
            position: relative;
        }

        .score-circle::before {
            content: '';
            position: absolute;
            width: 40px;
            height: 40px;
            background: #065f46;
            border-radius: 50%;
        }

        .score-text {
            position: relative;
            z-index: 1;
        }

        .typing-effect {
            overflow: hidden;
            border-right: 2px solid #60a5fa;
            white-space: nowrap;
            animation: typing 3s steps(40, end), blink 0.5s step-end infinite alternate;
        }

        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes blink {
            50% { border-color: transparent; }
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(255, 255, 255, 0.08);
        }

        .feature-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            display: block;
        }

        .loading-spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            border-top-color: #60a5fa;
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .hidden {
            display: none;
        }

        .analysis-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .analysis-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            border: 2px solid transparent;
            background-clip: padding-box;
        }

        .analysis-card.sql {
            border-color: #f59e0b;
        }

        .analysis-card.python {
            border-color: #10b981;
        }

        .analysis-card.ml {
            border-color: #8b5cf6;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .navigation {
                flex-direction: column;
                gap: 1rem;
            }
            
            .ai-message {
                flex-direction: column;
                text-align: center;
            }
            
            .ai-avatar {
                margin-right: 0;
                margin-bottom: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Welcome Screen -->
        <div id="welcome-screen">
            <div class="header">
                <h1><i class="fas fa-robot"></i> Advanced AI Interview Coach</h1>
                <p class="subtitle">Master Data Science with AI-Powered Voice Assistant & Real-Time Feedback</p>
            </div>

            <div class="glass-card">
                <h2 style="text-align: center; margin-bottom: 2rem; color: #60a5fa;">
                    <i class="fas fa-graduation-cap"></i> Interview Structure
                </h2>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <i class="fas fa-database feature-icon" style="color: #f59e0b;"></i>
                        <h3 style="color: #f1f5f9;">SQL Mastery</h3>
                        <p style="color: #cbd5e1;">2 Advanced database queries and optimization challenges</p>
                    </div>
                    <div class="feature-card">
                        <i class="fab fa-python feature-icon" style="color: #10b981;"></i>
                        <h3 style="color: #f1f5f9;">Python Expertise</h3>
                        <p style="color: #cbd5e1;">2 Algorithm and data structure problems</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-brain feature-icon" style="color: #8b5cf6;"></i>
                        <h3 style="color: #f1f5f9;">ML Concepts</h3>
                        <p style="color: #cbd5e1;">2 Machine learning theory and applications</p>
                    </div>
                </div>

                <div class="feature-grid">
                    <div class="feature-card">
                        <i class="fas fa-microphone feature-icon" style="color: #06b6d4;"></i>
                        <h3 style="color: #f1f5f9;">Voice Assistant</h3>
                        <p style="color: #cbd5e1;">AI speaks questions automatically with voice controls</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-chart-line feature-icon" style="color: #f472b6;"></i>
                        <h3 style="color: #f1f5f9;">Real-time Analysis</h3>
                        <p style="color: #cbd5e1;">Instant AI feedback with detailed scoring</p>
                    </div>
                    <div class="feature-card">
                        <i class="fas fa-trophy feature-icon" style="color: #facc15;"></i>
                        <h3 style="color: #f1f5f9;">Performance Tracking</h3>
                        <p style="color: #cbd5e1;">Comprehensive analytics and improvement tips</p>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 2rem;">
                    <button class="btn btn-primary" onclick="startInterview()">
                        <i class="fas fa-rocket"></i> Launch Interview Experience
                    </button>
                </div>
            </div>
        </div>

        <!-- Interview Screen -->
        <div id="interview-screen" class="hidden">
            <div class="progress-container">
                <div class="progress-bar" id="progress-bar"></div>
                <div class="progress-text" id="progress-text"></div>
            </div>

            <div class="ai-voice-container">
                <div class="ai-message">
                    <div class="ai-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div>
                        <div style="font-size: 1.1rem; margin-bottom: 0.5rem;">
                            <i class="fas fa-microphone-alt"></i> AI Interview Assistant
                        </div>
                        <div id="ai-speech-text" class="typing-effect"></div>
                        <div class="voice-controls">
                            <button class="voice-btn" onclick="toggleVoice()" id="voice-toggle">
                                <i class="fas fa-volume-up"></i> Voice On
                            </button>
                            <button class="voice-btn" onclick="repeatQuestion()">
                                <i class="fas fa-redo"></i> Repeat
                            </button>
                            <button class="voice-btn" onclick="speakAnswer()" id="speak-answer">
                                <i class="fas fa-ear"></i> Speak Answer
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="glass-card">
                <div class="question-section">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <div id="section-badge" class="badge"></div>
                        <h2 class="question-title" id="question-title"></h2>
                    </div>
                    <div id="question-context" class="question-context"></div>
                </div>

                <div class="answer-container">
                    <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #e2e8f0;">
                        <i class="fas fa-pen"></i> Your Solution:
                    </label>
                    <textarea 
                        id="answer-input" 
                        class="answer-textarea" 
                        placeholder="Type your detailed answer here... The AI will analyze your response for technical accuracy, clarity, and completeness."
                    ></textarea>
                </div>

                <div style="text-align: center; margin: 1.5rem 0;">
                    <button class="btn btn-success" onclick="getFeedback()" id="feedback-btn">
                        <i class="fas fa-brain"></i> Get AI Analysis
                    </button>
                </div>

                <div id="feedback-container" class="hidden"></div>

                <div class="navigation">
                    <button class="btn btn-secondary" onclick="previousQuestion()" id="prev-btn">
                        <i class="fas fa-arrow-left"></i> Previous
                    </button>
                    <div style="display: flex; gap: 1rem;">
                        <button class="btn btn-primary" onclick="nextQuestion()" id="next-btn" class="hidden">
                            Next <i class="fas fa-arrow-right"></i>
                        </button>
                        <button class="btn btn-primary" onclick="finishInterview()" id="finish-btn" class="hidden">
                            <i class="fas fa-flag-checkered"></i> Complete Interview
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Results Screen -->
        <div id="results-screen" class="hidden">
            <div class="header">
                <h1><i class="fas fa-chart-bar"></i> Interview Analysis Report</h1>
                <p class="subtitle">Comprehensive AI-Generated Performance Assessment</p>
            </div>

            <div class="glass-card">
                <div style="text-align: center; margin-bottom: 2rem;">
                    <div style="display: inline-block; position: relative;">
                        <div class="score-circle" id="overall-score-circle">
                            <span class="score-text" id="overall-score-text">0%</span>
                        </div>
                    </div>
                    <h2 style="margin-top: 1rem; color: #60a5fa;">Overall Performance</h2>
                </div>

                <div class="analysis-grid" id="section-analysis"></div>

                <div style="text-align: center; margin-top: 2rem;">
                    <button class="btn btn-primary" onclick="restartInterview()">
                        <i class="fas fa-refresh"></i> Take Another Interview
                    </button>
                    <button class="btn btn-secondary" onclick="downloadReport()" style="margin-left: 1rem;">
                        <i class="fas fa-download"></i> Download Report
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Interview Data
        const questions = [
            {
                section: "SQL",
                type: "sql",
                question: "Write a SQL query to find the top 3 customers by total order amount from the given tables.",
                context: `<strong>customers table:</strong><br><pre>customer_id | name<br>1 | John Doe<br>2 | Jane Smith<br>...</pre><br><strong>orders table:</strong><br><pre>order_id | customer_id | amount<br>101 | 1 | 500.00<br>102 | 2 | 750.00<br>...</pre>`,
                voiceText: "For your first question: Write a SQL query to find the top 3 customers by total order amount. You'll need to join the customer and order tables, and use aggregation."
            },
            {
                section: "SQL",
                type: "sql", 
                question: "Write a query to find employees who earn more than the average salary in their department.",
                context: `<strong>employees table:</strong><br><pre>emp_id | name | department | salary<br>1 | Alice | Engineering | 90000<br>2 | Bob | Engineering | 85000<br>...</pre>`,
                voiceText: "Next SQL question: Write a query to find employees who earn more than the average salary in their respective departments. Consider using a subquery or a window function."
            },
            {
                section: "Python",
                type: "python",
                question: "Write a Python function to find the second largest number in a list. Handle edge cases.",
                context: `<pre><code>find_second_largest([1, 3, 4, 5, 2]) → 4<br>find_second_largest([1, 1, 1]) → None</code></pre>`,
                voiceText: "Let's move to Python. Write a function to find the second largest number in a list. Remember to handle edge cases like lists with duplicates or fewer than two unique elements."
            },
            {
                section: "Python", 
                type: "python",
                question: "Implement a function to reverse words in a sentence while keeping the word order intact.",
                context: `<pre><code>reverse_words("Hello World Python") → "olleH dlroW nohtyP"</code></pre>`,
                voiceText: "Another Python challenge: Implement a function that reverses each word in a sentence but keeps the order of the words the same."
            },
            {
                section: "Machine Learning",
                type: "ml",
                question: "Explain the difference between supervised and unsupervised learning with examples.",
                context: "<p>Discuss data (labeled vs. unlabeled), goals (prediction vs. discovery), and provide examples of common algorithms for each.</p>",
                voiceText: "Now for Machine Learning. Please explain the core differences between supervised and unsupervised learning. Include examples of algorithms and problems each type is suited for."
            },
            {
                section: "Machine Learning",
                type: "ml", 
                question: "What is overfitting in machine learning and how can you prevent it?",
                context: "<p>Describe what overfitting is, and discuss at least three common techniques to prevent it (e.g., regularization, cross-validation, dropout).</p>",
                voiceText: "Final question: What is overfitting in machine learning? Explain how you would detect it and describe several common techniques used to prevent it."
            }
        ];

        // State Management
        let currentQuestion = 0;
        let userAnswers = {};
        let voiceEnabled = true;
        let speechSynthesis = window.speechSynthesis;

        // Initialize
        function startInterview() {
            document.getElementById('welcome-screen').classList.add('hidden');
            document.getElementById('interview-screen').classList.remove('hidden');
            loadQuestion();
        }

        function loadQuestion() {
            const question = questions[currentQuestion];
            
            // Update progress
            const progress = ((currentQuestion + 1) / questions.length) * 100;
            document.getElementById('progress-bar').style.width = progress + '%';
            document.getElementById('progress-text').textContent = `Question ${currentQuestion + 1} of ${questions.length} - ${question.section} Section`;

            // Update question content
            document.getElementById('question-title').textContent = question.question;
            document.getElementById('question-context').innerHTML = question.context;
            
            // Update section badge
            const badge = document.getElementById('section-badge');
            badge.textContent = question.section;
            badge.className = `badge ${question.section.toLowerCase().replace(' ', '-')}`;
            
            // Load saved answer
            const savedAnswer = userAnswers[currentQuestion]?.answer || '';
            document.getElementById('answer-input').value = savedAnswer;

            // Update navigation
            document.getElementById('prev-btn').style.display = currentQuestion > 0 ? 'block' : 'none';
            
            // Handle feedback display
            const feedbackContainer = document.getElementById('feedback-container');
            if (userAnswers[currentQuestion]?.feedback) {
                displayFeedback(userAnswers[currentQuestion]);
                document.getElementById('next-btn').classList.remove('hidden');
                document.getElementById('finish-btn').classList.toggle('hidden', currentQuestion < questions.length - 1);
            } else {
                feedbackContainer.classList.add('hidden');
                document.getElementById('next-btn').classList.add('hidden');
                document.getElementById('finish-btn').classList.add('hidden');
            }

            // Speak question with typing effect
            typeAndSpeak(question.voiceText);
        }

        function typeAndSpeak(text) {
            const element = document.getElementById('ai-speech-text');
            element.textContent = '';
            element.style.width = '0';
            
            let i = 0;
            const typeInterval = setInterval(() => {
                if (i < text.length) {
                    element.textContent += text.charAt(i);
                    i++;
                } else {
                    clearInterval(typeInterval);
                    element.style.width = '100%';
                    if (voiceEnabled) {
                        speakText(text);
                    }
                }
            }, 50);
        }

        function speakText(text) {
            if (speechSynthesis.speaking) {
                speechSynthesis.cancel();
            }
            
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.9;
            utterance.pitch = 1;
            utterance.volume = 0.8;
            
            // Try to use a more natural voice
            const voices = speechSynthesis.getVoices();
            const preferredVoice = voices.find(voice => 
                voice.name.includes('Google') || 
                voice.name.includes('Microsoft') ||
                voice.lang === 'en-US'
            );
            if (preferredVoice) {
                utterance.voice = preferredVoice;
            }
            
            speechSynthesis.speak(utterance);
        }

        function toggleVoice() {
            voiceEnabled = !voiceEnabled;
            const btn = document.getElementById('voice-toggle');
            btn.innerHTML = voiceEnabled ? 
                '<i class="fas fa-volume-up"></i> Voice On' : 
                '<i class="fas fa-volume-mute"></i> Voice Off';
            btn.classList.toggle('active', voiceEnabled);
            
            if (!voiceEnabled) {
                speechSynthesis.cancel();
            }
        }

        function repeatQuestion() {
            const question = questions[currentQuestion];
            speakText(question.voiceText);
        }

        function speakAnswer() {
            const answer = document.getElementById('answer-input').value;
            if (answer.trim()) {
                speakText("Here is your current answer: " + answer);
            } else {
                speakText("You haven't written an answer yet.");
            }
        }

        async function getFeedback() {
            const answer = document.getElementById('answer-input').value.trim();
            if (!answer) {
                alert('Please provide an answer before getting feedback.');
                return;
            }

            // Save answer
            if (!userAnswers[currentQuestion]) {
                userAnswers[currentQuestion] = {};
            }
            userAnswers[currentQuestion].answer = answer;

            // Show loading
            const btn = document.getElementById('feedback-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="loading-spinner"></span> Analyzing...';
            btn.disabled = true;

            // Simulate AI feedback (replace with actual API call)
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            const feedback = generateMockFeedback(questions[currentQuestion], answer);
            userAnswers[currentQuestion] = { ...userAnswers[currentQuestion], ...feedback };
            
            displayFeedback(userAnswers[currentQuestion]);
            
            // Restore button
            btn.innerHTML = originalText;
            btn.disabled = false;
            
            // Show navigation
            document.getElementById('next-btn').classList.remove('hidden');
            if (currentQuestion === questions.length - 1) {
                document.getElementById('finish-btn').classList.remove('hidden');
            }

            // Speak feedback summary
            if (voiceEnabled) {
                const summary = `Your score is ${feedback.score} out of 100. ${feedback.score >= 80 ? 'Excellent work!' : feedback.score >= 60 ? 'Good job, with room for improvement.' : 'Keep practicing to improve your skills.'}`;
                setTimeout(() => speakText(summary), 1000);
            }
        }

        function displayFeedback(data) {
            const container = document.getElementById('feedback-container');
            const scorePercentage = (data.score / 100) * 360;
            
            container.innerHTML = `
                <div class="feedback-container">
                    <div class="score-display">
                        <div class="score-circle" style="--score-deg: ${scorePercentage}deg;">
                            <span class="score-text">${data.score}%</span>
                        </div>
                        <div>
                            <h3 style="color: #f1f5f9; margin-bottom: 0.5rem;">
                                <i class="fas fa-robot"></i> AI Analysis Complete
                            </h3>
                            <p style="color: #cbd5e1;">Detailed feedback generated</p>
                        </div>
                    </div>
                    <div style="color: #e2e8f0; line-height: 1.6;">
                        ${data.feedback}
                    </div>
                </div>
            `;
            container.classList.remove('hidden');
        }

        function generateMockFeedback(question, answer) {
            // This is a mock function - replace with actual API call to your AI service
            const score = Math.floor(Math.random() * 40) + 60; // Random score between 60-100
            
            const feedbacks = {
                sql: {
                    high: "**Excellent SQL Skills!** ✨\n\n**Strengths:**\n- Proper use of JOIN operations\n- Correct aggregation functions\n- Good understanding of GROUP BY and ORDER BY\n\n**Areas for Improvement:**\n- Consider adding error handling\n- Could optimize with indexes",
                    medium: "**Good SQL Foundation** 📊\n\n**Strengths:**\n- Basic query structure is correct\n- Shows understanding of table relationships\n\n**Areas for Improvement:**\n- Work on complex joins\n- Practice with window functions\n- Consider performance optimization",
                    low: "**Keep Learning SQL** 💪\n\n**Strengths:**\n- Shows effort and basic understanding\n\n**Areas for Improvement:**\n- Review JOIN syntax\n- Practice aggregation functions\n- Study database normalization"
                },
                python: {
                    high: "**Outstanding Python Code!** 🐍\n\n**Strengths:**\n- Clean, readable code\n- Proper error handling\n- Efficient algorithm choice\n- Good variable naming\n\n**Areas for Improvement:**\n- Add more comments\n- Consider edge cases",
                    medium: "**Solid Python Skills** 🔧\n\n**Strengths:**\n- Logic is mostly correct\n- Shows problem-solving ability\n\n**Areas for Improvement:**\n- Optimize time complexity\n- Add input validation\n- Use more Pythonic approaches",
                    low: "**Python Practice Needed** 📚\n\n**Strengths:**\n- Shows understanding of basic concepts\n\n**Areas for Improvement:**\n- Review Python syntax\n- Practice with data structures\n- Study algorithm fundamentals"
                },
                ml: {
                    high: "**Excellent ML Knowledge!** 🧠\n\n**Strengths:**\n- Deep understanding of concepts\n- Good real-world examples\n- Clear explanations\n\n**Areas for Improvement:**\n- Include more mathematical details\n- Discuss recent developments",
                    medium: "**Good ML Foundation** 📈\n\n**Strengths:**\n- Understands core concepts\n- Provides relevant examples\n\n**Areas for Improvement:**\n- Dive deeper into algorithms\n- Practice with real datasets\n- Study model evaluation metrics",
                    low: "**ML Learning Journey** 🚀\n\n**Strengths:**\n- Shows interest in the field\n\n**Areas for Improvement:**\n- Study fundamental concepts\n- Practice with hands-on projects\n- Review statistics and linear algebra"
                }
            };

            const section = question.section.toLowerCase().replace(' ', '');
            const level = score >= 80 ? 'high' : score >= 65 ? 'medium' : 'low';
            
            return {
                score: score,
                feedback: feedbacks[section][level]
            };
        }

        function previousQuestion() {
            if (currentQuestion > 0) {
                currentQuestion--;
                loadQuestion();
            }
        }

        function nextQuestion() {
            if (currentQuestion < questions.length - 1) {
                currentQuestion++;
                loadQuestion();
            }
        }

        function finishInterview() {
            document.getElementById('interview-screen').classList.add('hidden');
            document.getElementById('results-screen').classList.remove('hidden');
            displayResults();
        }

        function displayResults() {
            // Calculate overall score
            let totalScore = 0;
            let answeredQuestions = 0;
            
            Object.values(userAnswers).forEach(answer => {
                if (answer.score !== undefined) {
                    totalScore += answer.score;
                    answeredQuestions++;
                }
            });
            
            const overallScore = answeredQuestions > 0 ? Math.round(totalScore / answeredQuestions) : 0;
            
            // Update overall score display
            const scoreCircle = document.getElementById('overall-score-circle');
            const scoreText = document.getElementById('overall-score-text');
            const scorePercentage = (overallScore / 100) * 360;
            
            scoreCircle.style.setProperty('--score-deg', `${scorePercentage}deg`);
            scoreText.textContent = `${overallScore}%`;
            
            // Calculate section scores
            const sectionScores = {
                'SQL': [],
                'Python': [],
                'Machine Learning': []
            };
            
            questions.forEach((q, index) => {
                const answer = userAnswers[index];
                if (answer && answer.score !== undefined) {
                    sectionScores[q.section].push(answer.score);
                }
            });
            
            // Display section analysis
            const sectionAnalysis = document.getElementById('section-analysis');
            const sectionIcons = {
                'SQL': 'fas fa-database',
                'Python': 'fab fa-python', 
                'Machine Learning': 'fas fa-brain'
            };
            const sectionColors = {
                'SQL': '#f59e0b',
                'Python': '#10b981',
                'Machine Learning': '#8b5cf6'
            };
            
            sectionAnalysis.innerHTML = Object.entries(sectionScores).map(([section, scores]) => {
                const avgScore = scores.length > 0 ? Math.round(scores.reduce((a, b) => a + b, 0) / scores.length) : 0;
                const sectionClass = section.toLowerCase().replace(' ', '-');
                
                return `
                    <div class="analysis-card ${sectionClass}">
                        <i class="${sectionIcons[section]}" style="font-size: 2rem; color: ${sectionColors[section]}; margin-bottom: 1rem;"></i>
                        <h3 style="color: #f1f5f9; margin-bottom: 0.5rem;">${section}</h3>
                        <div style="font-size: 2rem; font-weight: bold; color: ${sectionColors[section]};">${avgScore}%</div>
                        <div style="background: rgba(0,0,0,0.3); height: 8px; border-radius: 4px; margin-top: 1rem;">
                            <div style="background: ${sectionColors[section]}; height: 100%; width: ${avgScore}%; border-radius: 4px; transition: width 1s ease;"></div>
                        </div>
                    </div>
                `;
            }).join('');
            
            // Speak results summary
            if (voiceEnabled) {
                const resultsSummary = `Interview completed! Your overall score is ${overallScore} percent. ${overallScore >= 80 ? 'Outstanding performance!' : overallScore >= 70 ? 'Great job overall!' : overallScore >= 60 ? 'Good effort with room for improvement.' : 'Keep practicing to enhance your skills.'}`;
                setTimeout(() => speakText(resultsSummary), 1500);
            }
        }

        function restartInterview() {
            // Reset state
            currentQuestion = 0;
            userAnswers = {};
            
            // Show welcome screen
            document.getElementById('results-screen').classList.add('hidden');
            document.getElementById('welcome-screen').classList.remove('hidden');
            
            // Stop any ongoing speech
            speechSynthesis.cancel();
        }

        function downloadReport() {
            // Generate a simple text report
            let report = "AI Interview Coach - Performance Report\n";
            report += "=====================================\n\n";
            
            let totalScore = 0;
            let answeredQuestions = 0;
            
            questions.forEach((q, index) => {
                const answer = userAnswers[index];
                if (answer) {
                    report += `Question ${index + 1} (${q.section}):\n`;
                    report += `${q.question}\n\n`;
                    report += `Your Answer:\n${answer.answer}\n\n`;
                    if (answer.score !== undefined) {
                        report += `Score: ${answer.score}/100\n`;
                        report += `Feedback: ${answer.feedback.replace(/\*\*/g, '').replace(/\n/g, ' ')}\n\n`;
                        totalScore += answer.score;
                        answeredQuestions++;
                    }
                    report += "---\n\n";
                }
            });
            
            const overallScore = answeredQuestions > 0 ? Math.round(totalScore / answeredQuestions) : 0;
            report += `Overall Score: ${overallScore}%\n`;
            report += `Generated on: ${new Date().toLocaleDateString()}\n`;
            
            // Create and download file
            const blob = new Blob([report], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `interview-report-${new Date().toISOString().split('T')[0]}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        // Auto-save answers
        document.addEventListener('DOMContentLoaded', function() {
            const answerInput = document.getElementById('answer-input');
            if (answerInput) {
                answerInput.addEventListener('input', function() {
                    if (!userAnswers[currentQuestion]) {
                        userAnswers[currentQuestion] = {};
                    }
                    userAnswers[currentQuestion].answer = this.value;
                });
            }
            
            // Load voices for speech synthesis
            if (speechSynthesis.onvoiceschanged !== undefined) {
                speechSynthesis.onvoiceschanged = function() {
                    // Voices loaded
                };
            }
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey) {
                switch(e.key) {
                    case 'Enter':
                        e.preventDefault();
                        if (!document.getElementById('interview-screen').classList.contains('hidden')) {
                            getFeedback();
                        }
                        break;
                    case 'ArrowLeft':
                        e.preventDefault();
                        previousQuestion();
                        break;
                    case 'ArrowRight':
                        e.preventDefault();
                        if (!document.getElementById('next-btn').classList.contains('hidden')) {
                            nextQuestion();
                        }
                        break;
                }
            }
        });

        // Add CSS class for badges
        const style = document.createElement('style');
        style.textContent = `
            .badge {
                padding: 0.5rem 1rem;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .badge.sql {
                background: linear-gradient(135deg, #f59e0b, #d97706);
                color: white;
            }
            .badge.python {
                background: linear-gradient(135deg, #10b981, #059669);
                color: white;
            }
            .badge.machine-learning {
                background: linear-gradient(135deg, #8b5cf6, #7c3aed);
                color: white;
            }
        `;
        document.head.appendChild(style);
    </script>
</body>
</html>
