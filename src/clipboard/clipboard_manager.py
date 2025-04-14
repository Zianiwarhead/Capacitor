import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Text copied to clipboard.")

def paste_from_clipboard():
    text = pyperclip.paste()
    print("Text pasted from clipboard:", text)
    return text

# Example usage
if __name__ == "__main__":
    copy_to_clipboard("Hello, SmartCursor!")
    pasted_text = paste_from_clipboard()
