import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL=os.getenv("GEMINI_MODEL","gemini-3.6-flash")

AGENTS={
"Generate Code":"Generate production-quality code with clear structure and a short explanation.",
"Debug Code":"Identify root causes, explain errors, then provide corrected code.",
"Explain Code":"Explain the code step-by-step, including important concepts and complexity.",
"Optimize Code":"Find performance/readability issues and provide an improved implementation.",
"Code Review":"Review correctness, readability, maintainability, performance and architecture. Give severity levels.",
"Security Review":"Look for vulnerabilities, unsafe APIs, secrets, injection risks and insecure patterns. Provide remediation.",
"Generate Test Cases":"Create unit tests plus normal, edge, negative and boundary cases.",
"Complexity Analysis":"Determine time and space complexity and justify the result.",
"Generate Documentation":"Generate useful developer documentation, usage, setup and API/function details.",
"Refactor Code":"Refactor for clean architecture, modularity, readability and maintainability."
}

def run_agent(language,mode,prompt,code):
    key=os.getenv("GEMINI_API_KEY")
    if not key: return None,"GEMINI_API_KEY is missing in .env."
    role=AGENTS.get(mode,AGENTS["Generate Code"])
    system=f"""You are CodeGuru, a senior software engineer and specialized {mode} agent.
Language: {language}
Mission: {role}
Always be technically precise. Use Markdown. Never claim code was executed unless execution results are supplied.
For security findings, explain severity and safe remediation.
"""
    user=f"""User task:
{prompt or "(not specified)"}

Code/context:
```{language.lower()}
{code or "(none)"}
```"""
    try:
        client=genai.Client(api_key=key)
        r=client.models.generate_content(model=MODEL,contents=system+"\n\n"+user)
        return r.text,None
    except Exception as e:
        return None,f"Gemini API Error: {e}"
