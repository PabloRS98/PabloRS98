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


def get_public_repos():
    repos = api(f"/users/{USER}/repos?sort=pushed&per_page=30&type=owner")
    return [r for r in repos if not r["fork"] and r["name"].lower() != USER.lower()]


def recent_repos(repos, limit=5):
    rows = []
    for r in repos[:limit]:
        desc = (r["description"] or "—").replace("|", "\\|")
        lang = r["language"] or "—"
        rows.append(f"| [{r['name']}]({r['html_url']}) | {desc} | `{lang}` | {r['pushed_at'][:10]} |")
    header = "| Repository | Description | Language | Last push |\n|---|---|---|---|"
    return header + "\n" + "\n".join(rows)


def recent_activity(repos, limit=5):
    entries = []
    for r in repos[:5]:
        full_name = r["full_name"]
        try:
            commits = api(f"/repos/{full_name}/commits?per_page=5")
        except Exception:
            continue
        for c in commits:
            author = (c.get("author") or {}).get("login") or ""
            if author.endswith("[bot]"):
                continue
            commit_data = c.get("commit") or {}
            msg = (commit_data.get("message") or "").splitlines()[0][:80]
            date = ((commit_data.get("author") or {}).get("date") or "")
            if not msg or not date:
                continue
            entries.append((date, full_name, msg, c.get("html_url") or f"https://github.com/{full_name}"))
    entries.sort(key=lambda item: item[0], reverse=True)
    lines = [
        f"- `{date[:10]}` · [{repo}](https://github.com/{repo}) — [{msg}]({url})"
        for date, repo, msg, url in entries[:limit]
    ]
    return "\n".join(lines) or "_No recent public activity._"


def replace(text, name, body):
    pattern = re.compile(rf"(<!--START_SECTION:{name}-->)(.*?)(<!--END_SECTION:{name}-->)", re.S)
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def main():
    repos = get_public_repos()
    text = README.read_text(encoding="utf-8")
    text = replace(text, "repos", recent_repos(repos))
    text = replace(text, "activity", recent_activity(repos))
    README.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
