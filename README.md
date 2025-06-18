# DeepSeek4Free-fix
Source repository that I supplemented - [github.com/xtekky/deepseek4free](https://github.com/xtekky/deepseek4free) <br>
You can read more about the old features at this link ⤴

DeepSeek4Free but with additional features

## ✨ Features
- 🗑 **Delete Chat Session**: It is now possible to delete a chat session so as not to litter DeepSeek chats
- 📤 **Upload File**: It is now possible to upload a file to DeepSeek and then ask about it

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/deepseek4free.git
cd deepseek4free
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📚 Using new features

### Delete Chat Session
```python
from dsk.api import DeepSeekAPI

# Initialize with your auth token
api = DeepSeekAPI("YOUR_AUTH_TOKEN")

# Create a new chat session
chat_id = api.create_chat_session()

# Simple chat completion
prompt = "What is Python?"
for chunk in api.chat_completion(chat_id, prompt):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)

# Delete the current session
api.delete_chat_session(chat_id)
```

### Upload File
Upload File allows you to upload a file to DeepSeek, and then ask for something related to it. <br>
However, this feature does not support Web Search Integration (this is already a limitation of DeepSeek itself). <br>
You can also upload only 1 file at a time (I was too lazy to add the ability to upload more than 1 file).

```python
from dsk.api import DeepSeekAPI

client = DeepSeekAPI("DEEPSEEK_API_KEY")

# The function allows you to upload almost any file to DeepSeek
files_id = client.upload_file("very_interesting_history.txt")

chat_id = client.create_chat_session()

"""
In 'ref_file_ids', you must pass the id of the file that you uploaded earlier.
"""
promt = 'What is this file about?'
for chunk in client.chat_completion(chat_id, promt, ref_file_ids=files_id, thinking_enabled=False, search_enabled=False):
    if chunk['type'] == 'text':
        print(chunk['content'], end='', flush=True)

client.delete_chat_session(chat_id)
```
