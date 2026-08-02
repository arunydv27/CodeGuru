import ast

def analyze_python(code):
    r={"lines":len(code.splitlines()),"functions":0,"classes":0,"imports":0,"complexity":1,"issues":[]}
    try:
        t=ast.parse(code)
        r["functions"]=sum(isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) for n in ast.walk(t))
        r["classes"]=sum(isinstance(n,ast.ClassDef) for n in ast.walk(t))
        r["imports"]=sum(isinstance(n,(ast.Import,ast.ImportFrom)) for n in ast.walk(t))
        r["complexity"]=1+sum(isinstance(n,(ast.If,ast.For,ast.While,ast.Try,ast.With,ast.BoolOp,ast.IfExp)) for n in ast.walk(t))
        if r["complexity"]>10:r["issues"].append("High cyclomatic complexity; consider splitting logic into smaller functions.")
        if r["lines"]>500:r["issues"].append("Large source file; consider modularizing it.")
    except SyntaxError as e:r["issues"].append(f"Syntax error at line {e.lineno}: {e.msg}")
    return r
