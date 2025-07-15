# API & Webhook Hook Index

List of endpoint plans, keys, triggers, and linked actions.

---

## Slack API
- **Endpoint:** `/slack/incoming`
- **Purpose:** Receive techpack or vendor commands
- **Trigger:** `@Abraham` or task assignment

## ClickUp API
- **Endpoint:** `/clickup/status-change`
- **Purpose:** React to task status changes like "Launch / Green"
- **Trigger:** Status webhook + task type

## Dropbox API
- **Endpoint:** `/dropbox/folder-create`
- **Purpose:** Automatically generate asset folders
- **Trigger:** Techpack added or task created

---

Next step: define webhook auth and response payload formats.
