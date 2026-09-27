# Opus 5.5 default: ten desks

2026-09-27 16:46 America/Chicago.

Authority: “First order of business, let's switch to Opus 5.5, that should result in cost savings as our default model.”

Set `.claude/settings.json` model to `claude-opus-5-5`. Replaced one model declaration in each of ten canonical `.claude/agents` files, then regenerated root plugin mirrors with `scripts/sync_plugin_layout.py`. No desk instructions or effort settings changed. Historical model references remain historical. The change affects this project's Claude configuration; it does not switch the running Codex model or a separately installed cached plugin.

Verification:

```
sync_plugin_layout: in sync
manual: in sync (10 cold desks, 20 commands).
233/233 fixtures pass
Project default and all 20 canonical/mirrored desk declarations verified.
```

`git diff --check` passed. No live Claude model call or account-access test was run. Higher-priority runtime overrides can still select another model.

Anthropic documents `claude-opus-5-5` and standard input/output prices of $4/$20 per million tokens, versus Opus 5's $5/$25. Those unit rates are 20% lower; realized workflow or subscription savings have not been measured. Sources: [migration guide](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide), [Claude Code model configuration](https://code.claude.com/docs/en/model-config).

Knowledge disposition: no-knowledge-change; model configuration only.
