import os, uuid
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage

try:
    print("Azure Queue storage v12 - Python quickstart sample")
    # Quick start code goes here
except Exception as ex:
    print('Exception:')
    print(ex)

# Retrieve the connection string for use with the application.
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create a unique name for the queue
    queue_name = "quickstartqueues-" + str(uuid.uuid4())

    print("Creating queue: " + queue_name)

# Create and manipulate the queue
    queue_client = QueueClient.from_connection_string(connect_str, queue_name)

# Create the queue
    queue_client.create_queue()

    print("\nAdding messages to the queue...")

# Send several messages to the queue
    queue_client.send_message(u"First message")
    queue_client.send_message(u"Second message")
    saved_message = queue_client.send_message(u"Third message")
    print("\nPeek at the messages in the queue...")

# Peek at messages in the queue
    peeked_messages = queue_client.peek_messages(max_messages=5)

    for peeked_message in peeked_messages:
# Display the message
        print("Message: " + peeked_message.content)
	print("\nUpdating the third message in the queue...")

# Update a message using the message saved when calling send_message earlier
    queue_client.update_message(saved_message, pop_receipt=saved_message.pop_receipt, \
        content="Third message has been updated")
    print("\nReceiving messages from the queue...")

# Get messages from the queue
    messages = queue_client.receive_messages(messages_per_page=5)

    print("\nPress Enter key to 'process' messages and delete them from the queue...")
    input()

    for msg_batch in messages.by_page():
            for msg in msg_batch:
# "Process" the message
            print(msg.content)
                
# The message can be safely deleted
            queue_client.delete_message(msg)
    print("\nPress Enter key to delete the queue...")
    input()

# Clean up
    print("Deleting queue...")
    queue_client.delete_queue()

    print("Done")
