# intro to web browser module
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
else:
    address = '+'.join(pyperclip.paste())

webbrowser.open("https://google.com/search?q="  +address)
