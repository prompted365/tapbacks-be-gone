import re

# Define regex patterns for common tap backs
tap_back_patterns = [
    r"^(Liked|Loved|Disliked|Laughed at|Emphasized|Questioned) \"(.+?)\"$",
    r"(Liked|Loved|Disliked|Laughed at|Emphasized|Questioned) \"(.+?)\"$"
]

def filter_tap_backs(message):
    # Remove tap backs using regex patterns
    for pattern in tap_back_patterns:
        message = re.sub(pattern, "", message).strip()
    return message

def filter_messages(messages):
    # Apply filtering to each message and exclude empty results
    return [msg for msg in (filter_tap_backs(msg) for msg in messages) if msg]

# Example usage
messages = [
    "This is a sample message",
    "Liked \"This is a sample message\"",
    "Can we meet tomorrow?",
    "Loved \"Can we meet tomorrow?\"",
    "This is another message Liked \"This is another message\""
]

filtered_messages = filter_messages(messages)
print(filtered_messages)
