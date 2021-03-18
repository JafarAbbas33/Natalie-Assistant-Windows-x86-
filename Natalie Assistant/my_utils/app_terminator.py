assistant = None
root = None
update_text = None
import sys

def terminate(ter=True):
    assistant.conversation_stream.close()
    root.destroy()
    print("Destroyed")
    if ter:
        sys.exit()
