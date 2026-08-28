# Claude Code hooks

## auto-push.sh

PostToolUse hook (matcher `Write|Edit`, configured in `.claude/settings.local.json`).
After every file edit Claude makes inside this repo it runs:

```
git add <file>
git commit -m "Update <relative/path>"
git push
```

Runs only for files under the repo root. Concurrent edits are serialized with a
lock file (`.git/claude-autopush.lock`). If `git push` fails the commit is still
made locally and a message is shown.

To disable: open `/hooks` in Claude Code, or remove the `hooks` block from
`.claude/settings.local.json`.
