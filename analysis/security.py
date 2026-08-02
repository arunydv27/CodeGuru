import re

PATTERNS=[
(r"\beval\s*\(","Potentially dangerous eval() usage."),
(r"\bexec\s*\(","Potentially dangerous exec() usage."),
(r"subprocess\.[A-Za-z_]+\([^)]*shell\s*=\s*True","Review shell=True for command-injection risk."),
(r"password\s*=\s*['\"][^'\"]+['\"]","Possible hard-coded password/secret."),
(r"(api[_-]?key|secret|token)\s*=\s*['\"][^'\"]+['\"]","Possible hard-coded credential."),
(r"\bSELECT\b.*\+.*\bFROM\b","Possible SQL string concatenation; use parameterized queries."),
]

def security_scan(code):
    return [msg for pat,msg in PATTERNS if re.search(pat,code,re.I|re.S)]
