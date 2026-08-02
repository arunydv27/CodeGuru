# CodeGuru — Advanced AI Software Engineering Assistant

CodeGuru is a multi-agent AI assistant for software engineers, built with Python and Streamlit. It routes tasks across specialized agents to generate, debug, explain, optimize, and review code — backed by static analysis, security heuristics, and a persistent workspace.

## ✨ Features

- **Multi-agent task routing** — requests are automatically routed to the right specialized agent
- **Code generation, debugging, explanation, optimization & refactoring**
- **AI-powered code review & security review**
- **Automated test-case generation**
- **Complexity analysis** and **Python AST static analysis**
- **Security heuristics** to flag risky patterns
- **Sandboxed development code execution** with timeout protection
- **Project workspace** to organize and manage your work
- **Login / signup** with **SQLite persistence**
- **Dashboard and history** to track past sessions
- **Markdown export** of results

## 🛠️ Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **AI Model:** Google Gemini API
- **Database:** SQLite
- **Analysis:** Python AST (Abstract Syntax Tree)

## 📦 Project Structure

```
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
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A [Gemini API key](https://ai.google.dev/)

### Installation

Clone the repository:

```bash
git clone https://github.com/arunydv27/CodeGuru.git
cd CodeGuru
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

> On macOS/Linux, use `.venv/bin/python` instead of `.venv\Scripts\python.exe`.

### Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_KEY
GEMINI_MODEL=gemini-3.6-flash
```

### Run

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## ⚠️ Important Security Notice

The built-in Python code runner is a **development feature**, not a security sandbox. **Never expose unrestricted code execution to untrusted users in production.** For production deployments, isolate execution in a hardened container or VM with strict CPU, memory, filesystem, and network limits.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

No license specified yet. Consider adding one (e.g., MIT, Apache 2.0) so others know how they can use this project.
