from openai import OpenAI
import os
import time

# Set up the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

# Create an assistant
assistant = client.beta.assistants.create(
    name="My Assistant",
    instructions="You are an assistant that filters out tap back messages before processing.",
    model="gpt-4-1106-preview",
)

# Function to create a thread and run with filtered messages
def create_thread_and_run(user_input):
    # Filter the input messages
    filtered_input = filter_messages(user_input)
    
    # Create a thread
    thread = client.beta.threads.create()
    
    # Add filtered messages to the thread
    for message in filtered_input:
        client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=message
        )
    
    # Create a run
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    
    return thread, run

# Function to wait for the run to complete
def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

# Example usage
messages = [
    "This is a sample message",
    "Liked \"This is a sample message\"",
    "Can we meet tomorrow?",
    "Loved \"Can we meet tomorrow?\"",
    "This is another message Liked \"This is another message\""
]

thread, run = create_thread_and_run(messages)
run = wait_on_run(run, thread)

# Retrieve and display the messages
response_messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
for message in response_messages.data:
    print(f"{message['role']}: {message['content'][0]['text']['value']}")
