"""Behavioral completion checks in disposable repositories."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import okf_reconcile as kr


def receipt(root, subjects, files=(), disposition='no-knowledge-change', concepts=()):
    path = root / 'runs/reconciliation/fixture.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    record = dict(subjects=subjects, disposition=disposition, concepts=list(concepts),
                  authority='Fixture author approval', reason='Fixture tests mechanics only',
                  files={n: kr.digest(root/n) for n in files})
    path.write_text(json.dumps(record))
    return str(path.relative_to(root))


def merged_main_case():
    """A branch that merges main must not inherit main's book edits as its own.
    2026-09-27: a branch pushed before main moved on merged main and could not
    push or land, because the check diffed from the stale upstream."""
    with tempfile.TemporaryDirectory() as tmp:
        remote, root = Path(tmp)/'remote.git', Path(tmp)/'work'
        def git(*args, cwd=None):
            return subprocess.check_output(['git', *args], cwd=cwd or root, stderr=subprocess.DEVNULL, text=True).strip()
        git('init', '-q', '--bare', str(remote), cwd=tmp)
        git('clone', '-q', str(remote), str(root), cwd=tmp)
        git('config', 'user.name', 'Fixture'); git('config', 'user.email', 'fixture@example.com')
        git('checkout', '-qb', 'main'); git('commit', '--allow-empty', '-qm', 'base'); git('push', '-q', 'origin', 'main')
        git('checkout', '-qb', 'session'); git('push', '-qu', 'origin', 'session')
        git('checkout', '-q', 'main')
        p = root/'books/example/chapters/ch01/refined.md'; p.parent.mkdir(parents=True); p.write_text('main edit')
        git('add', '.'); git('commit', '-qm', 'main edits the book'); git('push', '-q', 'origin', 'main')
        git('checkout', '-q', 'session'); git('merge', '-q', '--no-edit', 'main')
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            rc = kr.check(root)
        return [(rc == 0, 'OKF merging main does not inherit main\'s book edits',
                 'a stale upstream must not make main\'s changes this branch\'s', rc)]


def okf_reconcile_cases():
    rows = merged_main_case()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL, text=True).strip()
        git('init', '-q', '-b', 'main'); git('config', 'user.name', 'Fixture'); git('config', 'user.email', 'fixture@example.com')
        git('commit', '--allow-empty', '-qm', 'base'); base=git('rev-parse','HEAD')
        name='books/example/chapters/ch01/refined.md'; p=root/name; p.parent.mkdir(parents=True);p.write_text('new knowledge')
        def check():
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                return kr.check(root,base)
        rows.append((check()==2, 'OKF untracked book knowledge blocks completion','no receipt means no completion',''))
        rec=receipt(root,['chapter:ch01'],[name])
        rows.append((check()==0,'OKF recorded disposition permits completion','file bytes covered',''))
        git('add','.');git('commit','-qm','initial knowledge');base=git('rev-parse','HEAD')
        git('checkout','-qb','session')
        p.write_text('corrected knowledge');git('add','.');git('commit','-qm','correction')
        rows.append((check()==2,'OKF committed edits invalidate stale receipts','clean worktree cannot hide new facts',''))
        receipt(root,['chapter:ch01'],[name]);rows.append((check()==0,'OKF refreshed receipt covers correction','freshness matters',''))
        p.unlink();rows.append((check()==2,'OKF deletion needs a disposition','deletion changes knowledge too',''))
        receipt(root,['chapter:ch01'],[name]);rows.append((check()==0,'OKF recorded deletion is covered','explicit removal is allowed',''))
        for field,value in [('disposition','unknown'),('authority',' '),('reason',''),('concepts',[])]:
            record=dict(subjects=['x'],disposition='updated',concepts=['books/example/okf/x.md'],authority='author',reason='correction',files={})
            record[field]=value
            try:kr.validate(root,record);ok=False
            except ValueError:ok=True
            rows.append((ok,'OKF invalid '+field+' refuses','structural evidence required',''))
        (root/'scripts').mkdir();(root/'inbox').mkdir()
        for script in ['inbox.py','okf_reconcile.py','sync.py']:
            shutil.copy(kr.ROOT/'scripts'/script,root/'scripts'/script)
        p.write_text('knowledge not yet reconciled')
        git('add','.');git('commit','-qm','new knowledge without receipt')
        r = subprocess.run([sys.executable, 'scripts/sync.py', '--push'], cwd=root, capture_output=True, text=True)
        rows.append((r.returncode == 2 and 'unreconciled' in r.stderr, 'OKF sync refuses unreconciled committed work', 'actual push entry point blocks before network write', r.stdout+r.stderr))
        r = subprocess.run(['bash', str(kr.ROOT/'.claude/hooks/session-stop.sh')], cwd=root, capture_output=True, text=True)
        rows.append((r.returncode == 2 and 'unreconciled' in r.stderr, 'OKF Stop hook refuses unreconciled work', 'actual hook stops before automatic commits', r.stdout+r.stderr))
        target=root/'inbox/001-test.md' ;original='---\nid: 001\nstatus: open\n---\n\n# Test\n';target.write_text(original)
        def inbox(*args):
            return subprocess.run([sys.executable,'scripts/inbox.py',*args],cwd=root,capture_output=True,text=True)
        r=inbox('--close','1','--resolution','approved')
        rows.append((r.returncode==2 and target.read_text()==original,'OKF inbox cannot close without receipt','refuses before mutation',r.stdout+r.stderr))
        rec=receipt(root,['inbox:002']);r=inbox('--close','1','--okf-receipt',rec)
        rows.append((r.returncode==2 and target.read_text()==original,'OKF unrelated receipt cannot close inbox','subject must match',r.stdout))
        rec=receipt(root,['inbox:001']);r=inbox('--close','1','--okf-receipt',rec,'--resolution','approved','--applied-by','true')
        rows.append((r.returncode==0 and 'status: resolved' in target.read_text(),'OKF receipt plus passing proof closes inbox','automatic path retains disposition',r.stdout+r.stderr))
        target.write_text(original.replace('status: open','status: ruled\napplied_by: touch PROOF_RAN'))
        r=inbox('--json')
        rows.append(('status: ruled' in target.read_text() and not(root/'PROOF_RAN').exists(),'OKF automatic reconciliation requires receipt','proof cannot bypass missing knowledge record',r.stdout+r.stderr))
    return rows

if __name__ == '__main__':
    rows=okf_reconcile_cases()
    for ok,name,_,detail in rows:
        print(('[ ok ] ' if ok else '[FAIL] ')+name)
        if not ok:print(detail)
    raise SystemExit(not all(r[0] for r in rows))
