import streamlit as st
from pathlib import Path
from services.ai import run_agent
from database.db import init_db, create_user, authenticate, save_request, get_history, get_stats
from analysis.static import analyze_python
from analysis.security import security_scan
from execution.runner import run_python
from workspace.manager import create_project, save_file, list_files, read_file, delete_file

st.set_page_config(page_title="CodeGuru", page_icon="👨‍💻", layout="wide")
init_db()

if "user" not in st.session_state:
    st.session_state.user = None

st.markdown("""
<style>
.block-container{max-width:1400px;padding-top:1.2rem}
.cg-title{font-size:3rem;font-weight:800;margin:0}
.cg-sub{opacity:.72;margin:0 0 1.2rem}
.card{padding:1rem;border:1px solid rgba(128,128,128,.25);border-radius:14px}
</style>
""", unsafe_allow_html=True)

def login():
    st.markdown('<p class="cg-title">👨‍💻 CodeGuru</p>', unsafe_allow_html=True)
    st.markdown('<p class="cg-sub">AI-powered intelligent software engineering assistant.</p>', unsafe_allow_html=True)
    a,b=st.tabs(["🔐 Login","📝 Create Account"])
    with a:
        u=st.text_input("Username", key="lu")
        p=st.text_input("Password", type="password", key="lp")
        if st.button("Login", type="primary", use_container_width=True):
            if authenticate(u.strip(),p):
                st.session_state.user=u.strip(); st.rerun()
            else: st.error("Invalid username or password.")
    with b:
        u=st.text_input("Choose username", key="su")
        p=st.text_input("Choose password", type="password", key="sp")
        p2=st.text_input("Confirm password", type="password", key="sp2")
        if st.button("Create Account", type="primary", use_container_width=True):
            if not u.strip() or not p: st.warning("Enter username and password.")
            elif p!=p2: st.error("Passwords do not match.")
            elif create_user(u.strip(),p): st.success("Account created. Login now.")
            else: st.error("Username already exists.")
    st.stop()

if not st.session_state.user: login()
user=st.session_state.user

with st.sidebar:
    st.markdown("## 👨‍💻 CodeGuru")
    st.success(f"Logged in as **{user}**")
    page=st.radio("Navigation",[
        "🚀 AI Code Studio","🧩 Project Workspace","🛡️ Security Scanner",
        "📊 Dashboard","🕘 History","📘 About"
    ])
    st.divider()
    if st.button("Logout",use_container_width=True):
        st.session_state.user=None; st.rerun()

if page=="🚀 AI Code Studio":
    st.markdown('<p class="cg-title">AI Code Studio</p>',unsafe_allow_html=True)
    st.markdown('<p class="cg-sub">Multi-agent coding workflow: generate → review → test → optimize → document.</p>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)
    language=c1.selectbox("Language",["Python","Java","C++","JavaScript","C","C#","Go","PHP"])
    mode=c2.selectbox("AI Agent / Task",[
        "Generate Code","Debug Code","Explain Code","Optimize Code",
        "Code Review","Security Review","Generate Test Cases",
        "Complexity Analysis","Generate Documentation","Refactor Code"
    ])
    c3.metric("AI Agents","10")

    prompt=st.text_area("💬 Task",height=120,placeholder="Example: Build a secure student management API.")
    code=st.text_area("🧑‍💻 Code / Context",height=320,placeholder="Paste code or project context here...")

    x,y,z=st.columns(3)
    ask=x.button("🚀 Ask CodeGuru",type="primary",use_container_width=True)
    metrics=y.button("🔬 Static Analysis",use_container_width=True)
    execute=z.button("▶️ Run Python",use_container_width=True)

    if metrics:
        if language!="Python": st.warning("Static analyzer currently supports Python.")
        else:
            r=analyze_python(code)
            st.subheader("Static Analysis")
            a,b,c,d=st.columns(4)
            a.metric("Lines",r["lines"]); b.metric("Functions",r["functions"])
            c.metric("Classes",r["classes"]); d.metric("Imports",r["imports"])
            st.metric("Cyclomatic Complexity",r["complexity"])
            for issue in r["issues"]:
                st.warning(issue)
            if not r["issues"]: st.success("No basic static-analysis issues found.")

    if execute:
        if language!="Python": st.warning("Local runner supports Python only.")
        elif not code.strip(): st.warning("Enter Python code.")
        else:
            out,err,rc=run_python(code)
            st.subheader("Execution Result")
            if out: st.code(out)
            if err: st.error(err)
            st.caption(f"Exit code: {rc}")

    if ask:
        with st.spinner("CodeGuru is orchestrating specialized AI agents..."):
            answer,error=run_agent(language,mode,prompt,code)
        if error: st.error(error)
        else:
            st.subheader("🤖 CodeGuru Result")
            st.markdown(answer)
            save_request(user,mode,language,prompt,code,answer)
            st.download_button("⬇️ Download Markdown",answer,"codeguru_result.md","text/markdown")

elif page=="🧩 Project Workspace":
    st.title("🧩 Project Workspace")
    st.caption("Create a small project workspace and ask CodeGuru about its files.")

    pcol, fcol = st.columns([1,2])
    with pcol:
        project=st.text_input("Project name",value="MyProject")
        if st.button("Create / Open Project",use_container_width=True):
            create_project(user,project)
            st.success("Project ready.")
        files_list=list_files(user,project)
        st.write("**Files**")
        selected=st.selectbox("Select file",files_list or ["No files"])
        if selected!="No files":
            if st.button("Delete selected file"):
                delete_file(user,project,selected); st.rerun()
    with fcol:
        fname=st.text_input("File name",value="main.py")
        content=st.text_area("File content",height=360)
        if st.button("Save File",type="primary"):
            create_project(user,project)
            save_file(user,project,fname,content)
            st.success("Saved.")
        if selected!="No files":
            st.subheader(f"Preview: {selected}")
            st.code(read_file(user,project,selected) or "",language=Path(selected).suffix.lstrip("."))

elif page=="🛡️ Security Scanner":
    st.title("🛡️ Security Scanner")
    st.caption("Fast local heuristics for common risky Python patterns; use AI review for deeper analysis.")
    code=st.text_area("Paste Python code",height=420)
    if st.button("Scan",type="primary"):
        findings=security_scan(code)
        if not findings: st.success("No high-signal patterns detected.")
        for f in findings:
            st.warning(f)

elif page=="📊 Dashboard":
    st.title("📊 CodeGuru Dashboard")
    s=get_stats(user)
    a,b,c,d,e=st.columns(5)
    a.metric("AI Requests",s["total"]); b.metric("Generate",s["generate"])
    c.metric("Debug",s["debug"]); d.metric("Reviews",s["review"]); e.metric("Tests",s["tests"])
    st.divider()
    st.subheader("Architecture")
    st.code("""User → Streamlit UI → Task Router → Specialized AI Agent
                         ↓
                Gemini 3.6 Flash
                         ↓
       Static Analysis / Security / Testing / Workspace
                         ↓
                    SQLite""")

elif page=="🕘 History":
    st.title("🕘 Coding History")
    rows=get_history(user)
    if not rows: st.info("No requests yet.")
    for i,(mode,lang,prompt,response,created) in enumerate(rows,1):
        with st.expander(f"{i}. {mode} • {lang} • {created}"):
            st.write("**Prompt:**",prompt or "—")
            st.markdown(response)

else:
    st.title("📘 About CodeGuru")
    st.write("""
**CodeGuru** is an AI-powered intelligent software engineering assistant built as a B.Tech Major Project.
It combines generative AI, specialized task agents, static code analysis, security heuristics,
testing assistance, project workspaces, authentication, analytics and coding history.
""")
    st.info("Default AI model: Gemini 3.6 Flash")
    st.write("Stack: Python • Streamlit • Google Gemini API • SQLite • Python AST")
    st.warning("The local code runner is for development. Public deployments should isolate untrusted code in a real sandbox/container.")
