# Tone Tag Bot — Slack Application

A Slack bot that detects **tone tags** (e.g. `/j`, `/srs`, `/lh`) in channel messages and
replies with a link to the dictionary entry for each one found. Users can also DM the bot
directly to look up definitions and browse the full tag dictionary.

---

## Files

| File | Purpose |
|---|---|
| `app.py` | Main bot logic — handles channel messages, @mentions, and DMs |
| `tone_tags.py` | Dictionary of all recognised tone tags, labels, and URLs |
| `requirements.txt` | Python dependencies |

---

## Setup

### 1. Create a Slack App

1. Go to <https://api.slack.com/apps> and click **Create New App → From scratch**.
2. Give it a name (e.g. *Tone Tag Bot*) and pick your workspace.

### 2. Configure Bot Token Scopes

Under **OAuth & Permissions → Scopes → Bot Token Scopes**, add:

| Scope | Reason |
|---|---|
| `chat:write` | Post replies in channels and DMs |
| `channels:history` | Read public channel messages |
| `groups:history` | Read private channel messages |
| `im:history` | Read direct messages |
| `im:read` | Detect when a DM conversation opens |
| `im:write` | Send direct messages |
| `mpim:history` | Read group DMs |

### 3. Enable Socket Mode

1. Go to **Socket Mode** and toggle it on.
2. Create an **App-Level Token** with the `connections:write` scope.
   Save it — this becomes `SLACK_APP_TOKEN`.

### 4. Subscribe to Events

Under **Event Subscriptions → Subscribe to bot events**, add:

- `message.channels`
- `message.groups`
- `message.im`
- `message.mpim`
- `app_mention`

### 5. Allow Direct Messages

Under **App Home**, scroll to **Show Tabs** and make sure:
- **Messages Tab** is toggled **on**
- Check **Allow users to send Slash commands and messages from the messages tab**

This is what allows users to DM the bot directly.

### 6. Install the App to Your Workspace

Go to **OAuth & Permissions** and click **Install to Workspace**.
Copy the **Bot User OAuth Token** — this becomes `SLACK_BOT_TOKEN`.

### 7. Invite the Bot to Channels

In Slack, type `/invite @YourBotName` in any channel you want it to monitor.
DMs work automatically once the app is installed — no invite needed.

---

## Running the Bot

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables (or put them in a .env file)
export SLACK_BOT_TOKEN="xoxb-..."
export SLACK_APP_TOKEN="xapp-..."

# Start the bot
python app.py
```

The bot uses **Socket Mode** so no public HTTP endpoint is required.

---

## DM Commands

Users can open a direct message with the bot and type any of the following:

| What to type | What the bot does |
|---|---|
| `definition` / `define` | Explains what tone tags are and how they work |
| `dictionary` / `list` / `all tags` | Shows the full list of supported tone tags with links |
| `hi` / `hello` / `help` | Shows the help message and available commands |
| A tone tag e.g. `/j` | Looks up that specific tag directly |
| Anything else | Tells the user what they can ask |

---

## Channel Behaviour

In any channel the bot has been invited to, it silently watches for tone tags. When one
is detected it replies in-thread with the label and a clickable dictionary link. No
response is sent if no tags are found.

---

## Adding or Editing Tone Tags

Open `tone_tags.py` and add entries to `TONE_TAG_DICT`:

```python
"/xyz": {
    "label": "Human-readable description",
    "url": "https://link-to-dictionary-entry.com",
},
```

Also add the new tag to the appropriate category list inside `build_full_dictionary()`
in `app.py` so it appears in the DM dictionary output. Restart the bot after any changes.

---

## How It Works

1. `app.py` compiles a regex from every key in `TONE_TAG_DICT` at startup.
2. Incoming messages are routed by `channel_type`:
   - `im` → DM handler: classifies the user's intent and responds accordingly.
   - Everything else → channel handler: scans for tone tags and replies in-thread.
3. Bot messages are filtered out to prevent reply loops.
