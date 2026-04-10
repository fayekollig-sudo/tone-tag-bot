import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from tone_tags import TONE_TAG_DICT

# Initialize the Slack Bolt app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Build a regex pattern that matches any known tone tag (case-insensitive)
# Tone tags typically look like /lh, /j, /gen, /srs, etc.
TONE_TAG_PATTERN = re.compile(
    r"(?<!\w)(" + "|".join(re.escape(tag) for tag in TONE_TAG_DICT.keys()) + r")(?!\w)",
    re.IGNORECASE,
)

# Keywords that trigger each DM command (case-insensitive)
DEFINITION_KEYWORDS = {"definition", "define", "what are tone tags", "what is a tone tag", "what are tone tags?"}
DICTIONARY_KEYWORDS = {"dictionary", "list", "all tags", "show all", "full list"}
HELP_KEYWORDS       = {"help", "hello", "hi", "hey", "start", "commands"}
HEAR_MORE_KEYWORDS  = {"more", "research", "why"}
ABOUT_KEYWORDS      = {"about", "bot", "making", "creation", "creator"}

TONE_TAG_DEFINITION = (
    "*What are tone tags?* \n"
    "Tone tags (also called tone indicators) are an easily embedded way of explicitly and unambiguously communicating tone in text-based communication. \n"
    "They complement text, not only to clarify tone and intention and reduce misinterpretations, but also as another form of nonverbal digital social cue (like emojis) that helps someone express themselves. \n"
    "They were popularized by <https://my.clevelandclinic.org/health/symptoms/23154-neurodivergent|neurodivergent> social media users and are used to make digital communication clearer and more accessible. \n\n"
    "They typically look like `*/j*`, `*/srs*`, or `*/lh*` and are placed at the end of a sentence.\n\n"
    "*Example:*\n"
    '> "That meeting could have been an email /j"\n\n'
    "Here `*/j*` signals the message is a joke, preventing potential misunderstanding if the recipient thinks the sender may be angry. \n\n"
    "To see the full list of supported tone tags, type *dictionary*.\n\n"
    "To learn more about tone indicators with links to academic research, type *research*."
)

HELP_MESSAGE = (
    "*Hi! I'm the Tone Tag Bot.* Here's what you can ask me:\n\n"
    "• *definition* — Learn what tone tags are and how they work\n"
    "• *dictionary* — See the full list of supported tone tags\n"
    "• *research* — Learn more about research about tone tags/indicators\n"
    "• *about* — Learn more about this particular bot and how it was made \n\n"
    "You can also use tone tags like `/j` or `/srs` in any channel I've been invited to, "
    "and I'll reply with their dictionary entry. To invite me to a channel, just type `/invite @ToneTags`."
)

HEAR_MORE_MESSAGE = (
    "*Why use tone indicators or tags?*\n"
    "Tone indicators are a type of technology that promotes accessibility. Like many assistive technologies, they were originally for a relatively narrow substrate of disabled people (in this case, <https://embrace-autism.com/decoding-autism-in-the-dsm-5/|Autistic> folks, who <https://embrace-autism.com/autistic-verbal-and-nonverbal-communication-differences/|experience differences in verbal and non-verbal communication>), but they are not helpful <https://ssir.org/articles/entry/the_curb_cut_effect|only for that group.>\n\n"
    "*How are tone indicators/tags an accessibility technology, and why in a professional setting?*\n"
    "Autistic individuals, particularly when communicating with non-Autistic people, manage 'hidden work of questioning, juggling, setting boundaries, and managing emotions,' and underlying intentions from all sides can be 'unclear and obscured by discrepancies between language and emotions' (<https://doi.org/10.1145/3613904.3642210|Zolyomi & Snyder 2024>). While computer-mediated-communication contexts are generally perceived as more comfortable for Autistic people than face-to-face interaction (<https://doi.org/10.1145/3613904.3642210|Zolyomi & Snyder, 2024>), miscommunication is already common in text-based online communication for general users (<https://doi.org/10.47814/ijssrr.v5i1.118|Christanti et al 2022>). Further, nonverbal cues are uniquely enacted in online communication in ways that may affect cross-neurotype communication (e.g., Autistic and neurotypical folks persistently interpret emojis differently (<https://doi.org/10.1007/s10803-022-05557-4|Hand et al 2023>)).\n\n"
    "In stories from Autistic folks, these differences present a significant challenge that puts a huge psychological burden on the Autistic person, especially in professional settings. Instructional designer <https://hbr.org/2022/10/stop-asking-neurodivergent-people-to-change-the-way-they-communicate|JD Goulet> refers to this as 'the expectation that ND [neurodivergent] people must jump through mentally and physically demanding hoops to communicate \u2018correctly\u2019 if they want to succeed in the workplace (or even be allowed a spot in the workplace at all).' It isn't a hard leap to make, especially given that according to the Autistic Americans Civil Liberties Union, 80% of Autistic adults are unemployed and in software engineering alone employers filter out 97% of Autistic candidates through non-job-related screening processes (<https://aaclu.org/|AACLU>). "
    "Tone indicators/tags have been shown to reduce 'the cognitive load needed to interpret tone' and make online communication 'feel more intuitive and connected' for neurodivergent individuals (<https://doi.org/10.1145/3757677|Xiao et al 2025>). They are a simple, intuitive assistive technology to complement text, not only to clarify tone and intention and reduce misinterpretations but also as another form of nonverbal digital social cue that facilitates emotional expression (<https://doi.org/10.47814/ijssrr.v5i1.118|Christanti et al 2022>), even when they are used only by one or some members of the conversation (<https://doi.org/10.1145/3757677|Xiao et al 2025>).\n\n"
    "To see the full list of supported tone tags, type *dictionary*.\n\n"
    "To see how to use this Tone Tags bot, type *help*."
)

ABOUT_MESSAGE = (
    "*About Tone Tags Bot*\n\n"
    "This Slack Bot was created by Autistic CU Boulder Information Science PhD student <https://fayekollig.com/|Faye Kollig> as a project for <https://jonathanzong.com/|Dr. Jonathon Zong's> Design for Accessibility Course.\n\n"
    "While it does not require any bot or technology beyond text input to add tone indicators to any text-based communication, there is no sole authoritative index of indicators and also limited adoption, especially among non-Autistic folks who need to understand and/or use  tone indicators to develop necessary communicative common ground. A Discord bot created by <https://top.gg/bot/1049042644107546664|top.gg prettyflowerss> to solve this problem acts as a dictionary-type tool when a user right clicks a message and hits 'process tone tag.' However, there was not a plugin for the workplace web and mobile application, Slack (commonly used, and used by the CU Boulder Information Science Department, as a professional communication medium) to facilitate using and having a shared dictionary for tone indicators. This app responded to this need.\n\n"
    "To create this bot, Faye utilized a combination of <https://docs.slack.dev/|Slack Developer documentation>, Python code generation using the generative AI tool, <https://claude.ai/|Claude>, and the starter tone tag dictionaries at <https://www.tonetags.xyz/|tonetags.xyz> and <https://toneindicators.carrd.co/|toneindicators.carrd.co>.\n\n"
    "To view 
)


# ── Helper functions ──────────────────────────────────────────────────────────

def find_tone_tags(text: str) -> list[str]:
    """Return a deduplicated list of tone tags found in the message text."""
    matches = TONE_TAG_PATTERN.findall(text)
    seen = []
    for match in matches:
        normalised = match.lower()
        if normalised not in seen:
            seen.append(normalised)
    return seen


def build_tag_response(found_tags: list[str]) -> str:
    """Build a Slack-formatted response listing each tag and its dictionary link."""
    lines = ["*Tone tag(s) detected!*"]
    for tag in found_tags:
        entry = TONE_TAG_DICT[tag]
        lines.append(
            f"• *{tag}* — {entry['label']}: {entry['url']}"
        )
    return "\n".join(lines)


def build_full_dictionary() -> str:
    """Build a Slack-formatted list of every tone tag in the dictionary."""
    lines = ["*Full Tone Tag Dictionary*\n"]

    for tag, entry in TONE_TAG_DICT.items():
        lines.append(f"• *{tag}* — {entry['label']}: {entry['url']}")

    return "\n".join(lines)


def classify_dm(text: str) -> str:
    """
    Classify a DM message into one of five intents:
      'definition' | 'dictionary' | 'help' | 'research' | 'about' | 'unknown'
    """
    normalised = text.lower().strip().rstrip("?!")

    if normalised in DEFINITION_KEYWORDS or "definition" in normalised or "define" in normalised:
        return "definition"
    if normalised in DICTIONARY_KEYWORDS or "dictionary" in normalised or "list" in normalised or "all tags" in normalised:
        return "dictionary"
    if normalised in HELP_KEYWORDS:
        return "help"
    if normalised in HEAR_MORE_KEYWORDS:
        return "research"
    if normalised in ABOUT_KEYWORDS:
        return "about"
    return "unknown"


# ── Event listeners ──────────────────────────────────────────────────────────

@app.event("message")
def handle_message(event, say):
    """
    Route messages based on channel type:
      - im (DM): interactive command interface
      - everything else: tone tag detection
    """
    # Ignore bot messages to prevent loops
    if event.get("bot_id") or event.get("subtype") == "bot_message":
        return

    channel_type = event.get("channel_type", "")
    text = (event.get("text", "") or "").strip()

    # ── DM handler ────────────────────────────────────────────────────────────
    if channel_type == "im":
        intent = classify_dm(text)

        if intent == "definition":
            say(TONE_TAG_DEFINITION)

        elif intent == "dictionary":
            say(build_full_dictionary())

        elif intent == "help":
            say(HELP_MESSAGE)

        elif intent == "research":
            say(HEAR_MORE_MESSAGE)

        elif intent == "about":
            say(ABOUT_MESSAGE)

        else:
            # Check if they included an actual tone tag in their DM
            found_tags = find_tone_tags(text)
            if found_tags:
                say(build_tag_response(found_tags))
            else:
                say(f"Sorry, I didn't understand *\"{text}\"*.\n\n{HELP_MESSAGE}")
        return

    # ── Channel / group handler ───────────────────────────────────────────────
    found_tags = find_tone_tags(text)
    if not found_tags:
        return

    say(
        text=build_tag_response(found_tags),
        thread_ts=event.get("thread_ts") or event.get("ts"),
    )


@app.event("app_mention")
def handle_mention(event, say):
    """Respond to @mentions in channels."""
    text = event.get("text", "") or ""
    found_tags = find_tone_tags(text)

    if found_tags:
        say(
            text=build_tag_response(found_tags),
            thread_ts=event.get("thread_ts") or event.get("ts"),
        )
    else:
        say(
            text=HELP_MESSAGE,
            thread_ts=event.get("thread_ts") or event.get("ts"),
        )


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    print("⚡ Tone-tag bot is running via Socket Mode...")
    handler.start()