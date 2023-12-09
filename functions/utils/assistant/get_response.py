

def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")
