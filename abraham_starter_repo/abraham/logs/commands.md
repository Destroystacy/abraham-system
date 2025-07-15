# Abraham Prompt & Command Library

This document tracks all useful prompts and Slack/ClickUp/ChatGPT commands used across Abraham's automation systems.

---

## 🧠 ChatGPT Prompts

- *"Draft a Slack message parser for ClickUp intake."*
- *"Summarize the last 3 tech pack entries into JSON format."*
- *"What automation can I build from this checklist?"*

---

## 💬 Slack Command Templates

- `@Abraham parse this tech pack → ClickUp`
- `@Abraham create vendor folder in Dropbox for GF00012`
- `@Abraham log cost sheet entry: SH010202 - Trench Coat - $480 - 6/28/25`

---

## 📋 ClickUp Triggers

| Triggered Phrase or Status | Action |
|----------------------------|--------|
| Task Status = `Launch / Green` | Trigger Slack vendor email + log cost |
| Task Title includes `techpack` | Begin ClickUp breakdown logic |
| Comment contains `@Abraham` | Parse and respond in Slack |

---

Add more as Abraham evolves.
