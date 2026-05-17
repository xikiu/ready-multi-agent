# NeYO: Gemini CLI Extensions

Workspace for Gemini CLI extensions.

## Architecture

- `ready-multi-agent/`: Core extension folder.
- `ready-multi-agent/scripts/neyo.py`: NeYO CLI Terminal for monitoring.
- `ready-multi-agent/skills/`: Custom agent skills (including `neyo-terminal`).
- `ready-multi-agent/gemini-extension.json`: Extension manifest.

## Standards

- **Skills**: Define in `SKILL.md`. Use clear descriptions.
- **Scripts**: Place in `scripts/` within skill folder or `ready-multi-agent/scripts/` for CLI tools.
- **Mode**: Always use `caveman` ultra mode for dev.
- **Naming**: `kebab-case` for extension and skill names.

## Development

1. Define skill in `SKILL.md`.
2. Add to `gemini-extension.json`.
3. Test using local extension load paths.
4. Use `neyo.py start --tasks ...` to orchestrate multi-agent builds.
5. **Interactive Mode**: Use `neyo.py chat` or `neyo.py start` to orchestrate tasks. You can use the `--yolo` flag if you want to bypass confirmations manually.

## Session Configuration

- **Disabled Extensions**: `ready-multi-agent` (disabled by default in this workspace).
