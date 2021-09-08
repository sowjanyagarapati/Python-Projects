import pyperclip

copied_text = "This is copied text"
pyperclip.copy(copied_text)

pasted_text = pyperclip.paste()

print(pasted_text)
