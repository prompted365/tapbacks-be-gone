import re

# Define regex patterns for common tap backs and reactions across platforms
tap_back_patterns = [
    r'^(Liked|Loved|Disliked|Laughed at|Emphasized|Questioned|Thumbs Up|Thumbs Down|Heart|Laughed|Exclamation|Question Mark|Haha|Wow|Sad|Angry|Care|Celebrate|Support|Insightful|Curious|Upvote|Downvote|Retweet|Quote Tweet) "(.+?)"$'
]

def filter_tap_backs(message):
    # Check and remove messages that are just tap backs
    for pattern in tap_back_patterns:
        if re.match(pattern, message):
            return ""
    return message

def filter_messages(messages):
    # Apply filtering to each message and exclude empty results
    return [filter_tap_backs(msg) for msg in messages if filter_tap_backs(msg)]

# Example usage with input messages
input_messages = [
    "This is a sample message",
    "Liked \"This is a sample message\"",
    "Can we meet tomorrow?",
    "Loved \"Can we meet tomorrow?\"",
    "This is another message",
    "Thumbs Up \"This is another message\"",
    "Amazing post!",
    "Wow \"Amazing post!\"",
    "That's funny!",
    "Haha \"That's funny!\"",
    "This is useful",
    "Upvote \"This is useful\"",
    "I disagree",
    "Downvote \"I disagree\""
]

filtered_messages = filter_messages(input_messages)
print(filtered_messages)
