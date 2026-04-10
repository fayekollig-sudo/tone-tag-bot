"""
tone_tags.py
------------
A dictionary of common tone tags used in online communication.

Each key is the tone tag as typed by users (e.g. "/j").
Each value is a dict with:
  - label : short human-readable description
  - url   : link to a dictionary / reference page for that tag

Sources used for URLs:
  - https://toneindicators.carrd.co  (community reference)
  - https://docs.google.com/... spreadsheets maintained by the disability/autism community
  - Individual wiki / dictionary entries where available

Feel free to add, remove, or update entries to match your community's norms.
"""

TONE_TAG_DICT: dict[str, dict[str, str]] = {
    # ── Sincerity / intent ────────────────────────────────────────────────────
    "/j": {
        "label": "Joking",
        "url": "Intended as a joke, with the goal of causing amusement",
    },
    "/hj": {
        "label": "Half joking",
        "url": "Partially intended as a joke, with the goal of causing amusement, and partially genuine or serious, with the goal of communicating information",
    },
    "/s": {
        "label": "Sarcastic / sarcasm",
        "url": "Intended to have a sarcastic tone, with sarcasm defined as the use of words that mean the opposite of what you really want to say, especially in order to insult someone, or to show irritation, or just to be funny",
    },
    "/srs": {
        "label": "Serious",
        "url": "Intended to be serious, with the goal of communicating or soliciting important or urgent information; intended not to be sarcastic, joking, or casual",
    },
    "/nsrs": {
        "label": "Not serious",
        "url": "Intended to be not serious or casual, with the goal of communicating or soliciting non-urgent information; intended not to be serious or urgent",
    },
    "/gen": {
        "label": "Genuine / genuinely",
        "url": "Intended to be genuine and authentic, with the goal of earnestly communicating or soliciting information; intended not to be sarcastic, ironic, joking, annoying, or provocative",
    },
    "/genq": {
        "label": "Genuine question",
        "url": "Intended to be genuine and authentic, with the goal of earnestly soliciting information; intended not to be sarcastic, ironic, joking, annoying, or provocative",
    },
    "/q": {
        "label": "Quote",
        "url": "Indicates that the message is a quote, not original content created by the sender",
    },
    # ── Emotional tone ────────────────────────────────────────────────────────
    "/lh": {
        "label": "Light-hearted",
        "url": "Intended to be light-hearted, unserious, carefree, or playful, often with the goal of diffusing tension; intended not to be serious, urgent, or angry",
    },
    "/ly": {
        "label": "Lovingly",
        "url": "Intended to be kind, affectionate, and read with love towards the recipient; intended not to be hurtful, joking or sarcastic",
    },
    "/t": {
        "label": "Teasing",
        "url": "Intended to be teasing or playful, with the goal of poking fun at someone or something; intended not to be genuine, serious, or taken literally",
    },
    "/sym": {
        "label": "Sympathetic",
        "url": "Intended to be sympathetic, or indicating understanding, feeling, and/or concern for the recipient’s situation",
    },
"/lu": { "label": "A Little Upset",
	"url": "Intended to express a low level of upset, anger, frustration; intended not to be very angry or very serious"
},
    # ── Request / interaction type ────────────────────────────────────────────
    "/rh": {
        "label": "Rhetorical question",
        "url": "Question in the message is intended to be rhetorical, with the goal of creating a dramatic effect or making a point rather than earnestly requesting an answer",
    },
    "/ij": {
        "label": "Inside joke",
        "url": "Indicating that the message contains an in-joke, or humor/reference based on a private, shared experience between the sender and someone else",
    },
    "/ref": {
        "label": "Reference (to media, meme, etc.)",
        "url": "Indicating that the message contains an allusion or reference to some piece of media outside of the current conversation",
    },
    "/cb": {
        "label": "Callback (referencing something said earlier)",
        "url": "Indicating that the message contains a reference to something said earlier in the conversation or between the sender/recipient",
    },
    "/hyp": {
        "label": "Hyperbole",
        "url": "Intended to be hyperbolic or exaggerated; intended not to be taken literally or at face value",
    },
    "/li": {
        "label": "Literal",
        "url": "Intended to be read literally and at face value, with the goal of communicating information exactly as it is; intended not to be hyperbole, exaggerated, sarcastic, or joking",
    },
    "/nli": {
        "label": "Not literal",
        "url": "Intended not to be read literally or at face value",
    },
    # ── Requests around replies ───────────────────────────────────────────────
    "/nf": {
        "label": "Not forced",
        "url": "Intended to be read without any pressure to respond ",
    },
    "/nm": {
        "label": "Not mad",
        "url": "Intended not to be angry",
    },
    "/neu": {
        "label": "Neutral",
        "url": "The author does not intend the message positively or negatively. This indicator is used to clarify the type of connotation the writer is trying to convey, when the message itself could have different connotations depending on the audience.",
    },
    "/neg": {
        "label": "Negative connotation",
        "url": "The author intends the message negatively. This indicator is used to clarify the connotation the writer is trying to convey, when the message itself could have different connotations depending on the audience.",
    },
    "/pos": {
        "label": "Positive connotation",
        "url": "The author intends the message positively. This indicator is used to clarify the type of connotation the writer is trying to convey, when the message itself could have different connotations depending on the audience.",
    },
    # ── Miscellaneous ─────────────────────────────────────────────────────────
    "/m": {
        "label": "Metaphor / metaphorically",
        "url": "Intended to be metaphorical, with a metaphor defined as a figure of speech in which a word or phrase is applied to an something to which it is not literally applicable with the goal of making a symbolic comparison; intended not to be taken literally or at face value",
    },
    "/ex": {
        "label": "Exaggeration",
        "url": "Intended to be hyperbolic or exaggerated; intended not to be taken literally or at face value",
    },
}
