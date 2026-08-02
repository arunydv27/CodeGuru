from pathlib import Path
import re

ROOT=Path("workspaces")

def safe(x): return re.sub(r"[^A-Za-z0-9_.-]","_",x)

def project_path(user,project): return ROOT/safe(user)/safe(project)

def create_project(user,project):
    p=project_path(user,project); p.mkdir(parents=True,exist_ok=True); return p

def list_files(user,project):
    p=project_path(user,project)
    return [str(x.relative_to(p)) for x in p.rglob("*") if x.is_file()] if p.exists() else []

def save_file(user,project,name,content):
    p=project_path(user,project)/safe(name)
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8")

def read_file(user,project,name):
    p=project_path(user,project)/name
    return p.read_text(encoding="utf-8") if p.exists() and p.is_file() else ""

def delete_file(user,project,name):
    p=project_path(user,project)/name
    if p.exists() and p.is_file(): p.unlink()
