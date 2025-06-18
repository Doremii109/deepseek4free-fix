from dsk.api import DeepSeekAPI

api_key = "DEEPSEEK_API_KEY"
client = DeepSeekAPI(api_key)

# The function allows you to upload almost any file to DeepSeek
files_id = client.upload_file("very_interesting_history.txt")


# Creating a new session
chat_id = client.create_chat_session()


"""

In 'ref_file_ids', you must pass the id of the file that you uploaded earlier.
You can't upload more than 1 file at a time (I'm too lazy to do that)

"""
promt = 'What is this file about?'
for chunk in client.chat_completion(chat_id, promt, ref_file_ids=files_id, thinking_enabled=False, search_enabled=False):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)

# This function deletes the current session
client.delete_chat_session(chat_id)

