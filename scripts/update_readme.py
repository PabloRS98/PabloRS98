"""Refresh the dynamic sections of README.md (recent repos + recent activity)."""
import json
import os
import re
import urllib.request
from pathlib import Path

USER = os.environ.get("GITHUB_USER", "PabloRS98")
TOKEN = os.environ.get("GITHUB_TOKEN")
README = Path(__file__).resolve().parent.parent / "README.md"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def recent_repos(limit=5):
    repos = api(f"/users/{USER}/repos?sort=pushed&per_page=30&type=owner")
    repos = [r for r in repos if not r["fork"] and r["name"].lower() != USER.lower()]
    rows = []
    for r in repos[:limit]:
        desc = (r["description"] or "—").replace("|", "\\|")
        lang = r["language"] or "—"
        rows.append(f"| [{r['name']}]({r['html_url']}) | {desc} | `{lang}` | {r['pushed_at'][:10]} |")
    header = "| Repository | Description | Language | Last push |\n|---|---|---|---|"
    return header + "\n" + "\n".join(rows)


def recent_activity(limit=5):
    events = api(f"/users/{USER}/events/public?per_page=50")
    lines, seen = [], set()
    for e in events:
        if e["type"] != "PushEvent":
            continue
        repo = e["repo"]["name"]
        commits = e["payload"].get("commits") or []
        if not commits:
            continue
        msg = commits[-1]["message"].splitlines()[0][:80]
        key = (repo, msg)
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- `{e['created_at'][:10]}` · [{repo}](https://github.com/{repo}) — {msg}")
        if len(lines) >= limit:
            break
    return "\n".join(lines) or "_No recent public activity._"


def replace(text, name, body):
    pattern = re.compile(rf"(<!--START_SECTION:{name}-->)(.*?)(<!--END_SECTION:{name}-->)", re.S)
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    text = README.read_text(encoding="utf-8")
    text = replace(text, "repos", recent_repos())
    text = replace(text, "activity", recent_activity())
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
