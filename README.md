CodeGuru — Advanced AI Software Engineering Assistant

CodeGuru is a multi-agent AI assistant for software engineers, built with Python and Streamlit. It routes tasks across specialized agents to generate, debug, explain, optimize, and review code — backed by static analysis, security heuristics, and a persistent workspace.

📌 Problem Statement

Developers spend a significant amount of time on repetitive tasks — writing boilerplate code, debugging, reviewing pull requests for security issues, and writing test cases. Existing single-purpose AI coding tools handle only one of these tasks at a time, forcing developers to switch between multiple tools. CodeGuru addresses this by unifying these tasks under one AI-powered, multi-agent platform.

🎯 Objectives
To design a multi-agent system capable of routing a developer's request to the most relevant AI agent
To integrate generative AI (Gemini API) for code generation, debugging, explanation, optimization, and refactoring
To implement static analysis using Python's AST module for complexity and security evaluation
To provide a secure, timeout-bound sandbox for executing untrusted code during development
To build a persistent, user-specific workspace with login/signup and history tracking
To evaluate the system's usefulness in reducing developer effort across the software development lifecycle
✨ Features
Multi-agent task routing — requests are automatically routed to the right specialized agent
Code generation, debugging, explanation, optimization & refactoring
AI-powered code review & security review
Automated test-case generation
Complexity analysis and Python AST static analysis
Security heuristics to flag risky patterns
Sandboxed development code execution with timeout protection
Project workspace to organize and manage your work
Login / signup with SQLite persistence
Dashboard and history to track past sessions
Markdown export of results
🛠️ Tech Stack
Language: Python
UI: Streamlit
AI Model: Google Gemini API
Database: SQLite
Analysis: Python AST (Abstract Syntax Tree)
📦 Project Structure
CodeGuru/
├── agents/       # Specialized AI agents (generation, debugging, review, etc.)
├── analysis/     # Static analysis, complexity, and security heuristics
├── assets/       # Static assets (images, icons, styles)
├── database/     # SQLite persistence layer
├── execution/    # Sandboxed code execution engine
├── pages/        # Streamlit pages (dashboard, history, etc.)
├── services/     # Core services and business logic
├── workspace/    # User project workspace management
├── app.py        # Application entry point
└── requirements.txt
🚀 Getting Started
Prerequisites
Python 3.9+
A Gemini API key
Installation

Clone the repository:

bash
git clone https://github.com/arunydv27/CodeGuru.git
cd CodeGuru

Create a virtual environment and install dependencies:

bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt

On macOS/Linux, use .venv/bin/python instead of .venv\Scripts\python.exe.

Configuration

Create a .env file in the project root:

env
GEMINI_API_KEY=YOUR_KEY
GEMINI_MODEL=gemini-3.6-flash
Run
bash
.venv\Scripts\python.exe -m streamlit run app.py

The app will open in your browser at http://localhost:8501.

 Important Security Notice:

The built-in Python code runner is a development feature, not a security sandbox. Never expose unrestricted code execution to untrusted users in production. For production deployments, isolate execution in a hardened container or VM with strict CPU, memory, filesystem, and network limits.

 Future Scope:
Multi-language support — extend static analysis and execution beyond Python (e.g., Java, C++, JavaScript)
IDE/editor plugin — integrate CodeGuru directly into VS Code or JetBrains IDEs instead of a standalone web app
CI/CD pipeline integration — auto-trigger code review and security checks on every pull request
Team collaboration features — shared workspaces, role-based access, and reviewer assignment
Model flexibility — support for additional LLM providers (OpenAI, Claude, local open-source models) alongside Gemini
Advanced sandboxing — move code execution into isolated Docker containers with strict resource limits for production-grade safety
Analytics dashboard — track code quality trends, common bug patterns, and productivity metrics over time
Voice/chat-based interaction — conversational interface for hands-free coding assistance
Offline/self-hosted mode — for organizations with strict data-privacy requirements

Conclusion:
CodeGuru demonstrates how multi-agent AI architectures can be applied to real-world software engineering workflows — combining generative AI with traditional static analysis techniques to assist developers across the coding lifecycle. While the current implementation is suited for development and academic use, the modular agent-based design leaves clear room for scaling into a production-grade developer tool, as outlined in the Future Scope section above.

 Contributing :

Contributions are welcome! Feel free to open an issue or submit a pull request.

📄 License

No license specified yet.

📄 License

No license specified yet.
