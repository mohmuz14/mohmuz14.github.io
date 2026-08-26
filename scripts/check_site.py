#!/usr/bin/env python3
"""Static site checks. No third-party dependencies -- stdlib only."""
import glob, os, re, sys
from html.parser import HTMLParser

BS = chr(92)
FAIL = []
WARN = []
IMG_BUDGET_KB = 400          # per image
PAGE_BUDGET_MB = 3.0         # total first-load weight

def rel(p): return p.replace(BS, '/')

class Anchors(HTMLParser):
    def __init__(self): super().__init__(); self.refs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for k in ('src', 'href'):
            if d.get(k): self.refs.append((tag, d[k]))

def check_links():
    for page in [rel(p) for p in glob.glob('*.html') + glob.glob('projects/*.html')]:
        base = os.path.dirname(page)
        p = Anchors(); p.feed(open(page, encoding='utf-8', errors='ignore').read())
        for tag, ref in p.refs:
            if re.match(r'^(https?:|mailto:|tel:|data:|#|//)', ref): continue
            clean = ref.split('#')[0].split('?')[0]
            if not clean: continue
            root = clean.startswith('/')
            target = os.path.normpath(clean.lstrip('/') if root else os.path.join(base, clean))
            target = rel(target).replace('%20', ' ')
            if target and not os.path.exists(target):
                FAIL.append(f"broken {tag} reference in {page}: {ref}")

def check_placeholders():
    for page in [rel(p) for p in glob.glob('projects/*.html')]:
        n = open(page, encoding='utf-8', errors='ignore').read().count('TODO:')
        if n: FAIL.append(f"{page} still has {n} unfilled TODO placeholder(s)")

def check_images():
    total = 0
    for img in [rel(p) for p in glob.glob('assets/img/**/*.*', recursive=True)]:
        if not img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')): continue
        kb = os.path.getsize(img) / 1024; total += kb
        if kb > IMG_BUDGET_KB:
            WARN.append(f"{img} is {kb:.0f} KB (budget {IMG_BUDGET_KB} KB)")
    if total / 1024 > PAGE_BUDGET_MB:
        FAIL.append(f"images total {total/1024:.1f} MB, over the {PAGE_BUDGET_MB} MB budget")

def check_privacy():
    for page in [rel(p) for p in glob.glob('*.html') + glob.glob('projects/*.html')]:
        s = open(page, encoding='utf-8', errors='ignore').read()
        if re.search(r'tel:|[+]\d{2}\s?\d{10}', s):
            FAIL.append(f"{page} exposes a phone number")

def check_licence():
    if os.path.exists('LICENSE'):
        FAIL.append("LICENSE reintroduced -- portfolio content is all-rights-reserved (see COPYRIGHT.md)")
    if not os.path.exists('COPYRIGHT.md'):
        FAIL.append("COPYRIGHT.md is missing")

for fn in (check_links, check_placeholders, check_images, check_privacy, check_licence):
    fn()

for w in WARN: print(f"warning: {w}")
for f in FAIL: print(f"error: {f}")
print(f"\n{len(FAIL)} error(s), {len(WARN)} warning(s)")
sys.exit(1 if FAIL else 0)
