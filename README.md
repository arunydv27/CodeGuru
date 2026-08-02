# CodeGuru — Advanced AI Software Engineering Assistant

## Major Project Modules
- Multi-agent AI task routing
- Code generation, debugging, explanation, optimization and refactoring
- AI code review and security review
- AI test-case generation
- Complexity analysis
- Python AST static analysis
- Security heuristics
- Development code execution with timeout
- Project workspace
- Login/signup
- SQLite persistence
- Dashboard and history
- Markdown export

## Setup

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create `.env`:
```env
GEMINI_API_KEY=YOUR_KEY
GEMINI_MODEL=gemini-3.6-flash
```

Run:
```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

## Important
The local Python runner is a development feature, not a security sandbox. Never expose unrestricted execution of untrusted user code publicly. For production, isolate execution with a hardened container/VM and strict CPU, memory, filesystem and network limits.
