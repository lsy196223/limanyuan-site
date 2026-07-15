import base64, json, os, sys
import urllib.request, urllib.error, urllib.parse

TOKEN = 'YOUR_GITHUB_TOKEN_HERE'  # 替换为你的 GitHub Personal Access Token
REPO = 'lsy196223/limanyuan-site'
BASE = r'C:/Users/HUAWEI/limanyuan-site'
API = f'https://api.github.com/repos/{REPO}/contents'

SKIP_DIRS = {'.git'}
UPLOADED = 0
FAILED = 0
SKIPPED = 0

def upload(path):
    global UPLOADED, FAILED, SKIPPED
    rel = os.path.relpath(path, BASE).replace('\\', '/')
    if rel.startswith('upload_github') or rel.startswith('.git'):
        return

    try:
        with open(path, 'rb') as f:
            raw = f.read()
        content = base64.b64encode(raw).decode()
    except Exception as e:
        print(f'  SKIP (read error): {rel} - {e}')
        SKIPPED += 1
        return

    # URL-encode Chinese characters in path
    encoded_path = '/'.join(urllib.parse.quote(part, safe='') for part in rel.split('/'))

    data = json.dumps({
        'message': f'Add {rel}',
        'content': content,
        'branch': 'main'
    }).encode('utf-8')

    req = urllib.request.Request(
        f'{API}/{encoded_path}',
        data=data,
        headers={
            'Authorization': f'token {TOKEN}',
            'Accept': 'application/vnd.github+json',
            'Content-Type': 'application/json'
        },
        method='PUT'
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            status = resp.status
        if status in (201, 200):
            print(f'  OK ({len(raw)}B): {rel}')
            UPLOADED += 1
        else:
            print(f'  FAIL {status}: {rel}')
            FAILED += 1
    except urllib.error.HTTPError as e:
        print(f'  FAIL {e.code}: {rel} - {e.reason}')
        FAILED += 1
    except Exception as e:
        print(f'  FAIL: {rel} - {e}')
        FAILED += 1

# Upload all files
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fname in sorted(files):
        upload(os.path.join(root, fname))

print(f'\nDone: {UPLOADED} uploaded, {FAILED} failed, {SKIPPED} skipped')
