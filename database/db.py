import sqlite3, hashlib
DB="codeguru.db"

def con(): return sqlite3.connect(DB)
def hp(p): return hashlib.sha256(p.encode()).hexdigest()

def init_db():
    c=con()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username TEXT UNIQUE,password TEXT)")
    c.execute("""CREATE TABLE IF NOT EXISTS requests(
    id INTEGER PRIMARY KEY,username TEXT,mode TEXT,language TEXT,prompt TEXT,code TEXT,response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    c.commit(); c.close()

def create_user(u,p):
    try:
        c=con(); c.execute("INSERT INTO users(username,password) VALUES(?,?)",(u,hp(p))); c.commit(); c.close(); return True
    except sqlite3.IntegrityError: return False

def authenticate(u,p):
    c=con(); r=c.execute("SELECT 1 FROM users WHERE username=? AND password=?",(u,hp(p))).fetchone(); c.close(); return r is not None

def save_request(u,m,l,p,cod,res):
    c=con(); c.execute("INSERT INTO requests(username,mode,language,prompt,code,response) VALUES(?,?,?,?,?,?)",(u,m,l,p,cod,res)); c.commit(); c.close()

def get_history(u):
    c=con(); r=c.execute("SELECT mode,language,prompt,response,created_at FROM requests WHERE username=? ORDER BY id DESC LIMIT 100",(u,)).fetchall(); c.close(); return r

def get_stats(u):
    c=con()
    total=c.execute("SELECT COUNT(*) FROM requests WHERE username=?",(u,)).fetchone()[0]
    def n(m): return c.execute("SELECT COUNT(*) FROM requests WHERE username=? AND mode=?",(u,m)).fetchone()[0]
    out={"total":total,"generate":n("Generate Code"),"debug":n("Debug Code"),"review":n("Code Review"),"tests":n("Generate Test Cases")}
    c.close(); return out
