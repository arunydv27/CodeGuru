import subprocess,tempfile
from pathlib import Path

def run_python(code):
    try:
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"main.py"; p.write_text(code,encoding="utf-8")
            r=subprocess.run(["python",str(p)],capture_output=True,text=True,timeout=5)
            return r.stdout,r.stderr,r.returncode
    except subprocess.TimeoutExpired:return "","Execution timed out (5 seconds).",-1
    except Exception as e:return "",str(e),-1
