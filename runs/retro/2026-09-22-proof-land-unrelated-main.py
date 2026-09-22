import os,subprocess,sys,tempfile,shutil
REPO="/home/user/agentic-ghostwriter"
d=tempfile.mkdtemp()
def g(*a,cwd): return subprocess.run(["git",*a],cwd=cwd,capture_output=True,text=True)
up=os.path.join(d,"up"); os.makedirs(up); g("init","--bare","-b","main",cwd=up)
wk=os.path.join(d,"wk"); os.makedirs(wk)
g("init","-b","main",cwd=wk); g("remote","add","origin",up,cwd=wk)
g("config","user.email","t@t",cwd=wk); g("config","user.name","t",cwd=wk)
os.makedirs(os.path.join(wk,"scripts"),exist_ok=True)
os.makedirs(os.path.join(wk,"scripts"),exist_ok=True); shutil.copy(os.path.join(REPO,"scripts","sync.py"), os.path.join(wk,"scripts","sync.py"))
open(os.path.join(wk,"a.txt"),"w").write("1")
g("add","-A",cwd=wk); g("commit","-m","real root",cwd=wk); g("push","-u","origin","main",cwd=wk)
g("checkout","-b","feat",cwd=wk)
open(os.path.join(wk,"b.txt"),"w").write("2")
g("add","-A",cwd=wk); g("commit","-m","work",cwd=wk); g("push","-u","origin","feat",cwd=wk)
# make LOCAL main an unrelated history - exactly tonight's state
g("checkout","--orphan","junk",cwd=wk); g("rm","-rf",".",cwd=wk)
os.makedirs(os.path.join(wk,"scripts"),exist_ok=True); shutil.copy(os.path.join(REPO,"scripts","sync.py"), os.path.join(wk,"scripts","sync.py"))
open(os.path.join(wk,"c.txt"),"w").write("3")
g("add","-A",cwd=wk); g("commit","-m","unrelated root",cwd=wk)
sha=g("rev-parse","HEAD",cwd=wk).stdout.strip()
g("checkout","feat",cwd=wk); g("branch","-f","main",sha,cwd=wk)
g("checkout","--","." ,cwd=wk)
assert g("merge-base","main","origin/main",cwd=wk).stdout.strip()=="", "setup failed"
st=g("status","--porcelain",cwd=wk).stdout.strip()
assert st=="", f"setup dirty: {st}"
r=subprocess.run([sys.executable,"scripts/sync.py","--land"],cwd=wk,capture_output=True,text=True)
print("--- land rc:",r.returncode); print("STDOUT:",r.stdout[-800:]); print("STDERR:",r.stderr[-500:])
blob=(r.stdout+r.stderr).lower()
# The guard must refuse BEFORE checkout, naming the remedy. Reaching git's own
# "refusing to merge unrelated histories" via the land-FAILED path is the DEFECT,
# not the fix - an earlier version of this predicate went green on exactly that.
ok = (r.returncode==1
      and "land failed" not in blob
      and "branch -f main origin/main" in blob)
print("current branch after run:", g("rev-parse","--abbrev-ref","HEAD",cwd=wk).stdout.strip())
print("GUARD PRESENT:", ok)
sys.exit(0 if ok else 1)
