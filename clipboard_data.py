# clipboard_data.py

clipboard_content = ""

def set_clipboard(text):
    global clipboard_content
    clipboard_content = text

def get_clipboard():
    return clipboard_content
