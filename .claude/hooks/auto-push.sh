#!/usr/bin/env bash
# Auto-commit + push the file touched by a Write/Edit tool call.
# Wired up as a PostToolUse hook (matcher: Write|Edit) in .claude/settings.local.json
set -uo pipefail

REPO="/root/holbertonschool-higher_level_programming"
cd "$REPO" || exit 0

# Serialize concurrent hook runs (parallel edits) on the git index.
exec 9>"$REPO/.git/claude-autopush.lock"
flock 9

# Extract the edited file path from the hook's stdin JSON (no jq on this box).
f=$(python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("tool_input",{}).get("file_path",""))' 2>/dev/null)
[ -z "$f" ] && exit 0

# Only touch files that live inside this repo.
case "$f" in
  "$REPO"/*) ;;
  *) exit 0 ;;
esac
rel="${f#"$REPO"/}"

git add -- "$f" 2>/dev/null || exit 0

# Nothing actually changed for this file? done.
if git diff --cached --quiet -- "$f"; then
  exit 0
fi

git commit --quiet -m "Update $rel" -m "Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01ULJ29JUqPRr3TVAeKKYZS4" || exit 0

if ! err=$(git push --quiet 2>&1); then
  printf '{"systemMessage": "auto-push: commit made but git push failed: %s"}\n' \
    "$(printf '%s' "$err" | tr '\n' ' ' | sed 's/"/\\"/g' | cut -c1-200)"
fi
