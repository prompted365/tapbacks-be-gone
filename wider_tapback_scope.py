// Define regex patterns for common tap backs and reactions across platforms
const tapBackPatterns = [
    /^(Liked|Loved|Disliked|Laughed at|Emphasized|Questioned|Thumbs Up|Thumbs Down|Heart|Laughed|Exclamation|Question Mark|Haha|Wow|Sad|Angry|Care|Celebrate|Support|Insightful|Curious|Upvote|Downvote|Retweet|Quote Tweet) "(.+?)"$/,
    /(Liked|Loved|Disliked|Laughed at|Emphasized|Questioned|Thumbs Up|Thumbs Down|Heart|Laughed|Exclamation|Question Mark|Haha|Wow|Sad|Angry|Care|Celebrate|Support|Insightful|Curious|Upvote|Downvote|Retweet|Quote Tweet) "(.+?)"$/
];

function filterTapBacks(message) {
    // Remove tap backs using regex patterns
    for (const pattern of tapBackPatterns) {
        message = message.replace(pattern, "").trim();
    }
    return message;
}

function filterMessages(messages) {
    // Apply filtering to each message and exclude empty results
    return messages.map(filterTapBacks).filter(msg => msg);
}

// Example usage with input from BuildShip workflow
const inputMessages = [
    "This is a sample message",
    "Liked \"This is a sample message\"",
    "Can we meet tomorrow?",
    "Loved \"Can we meet tomorrow?\"",
    "This is another message Liked \"This is another message\"",
    "Thumbs Up \"This is another message\"",
    "Wow \"Amazing post!\"",
    "Haha \"That's funny!\"",
    "Upvote \"This is useful\"",
    "Downvote \"I disagree\""
];

const filteredMessages = filterMessages(inputMessages);
console.log(filteredMessages);

// Output the filtered messages as the node result
return { filteredMessages };
