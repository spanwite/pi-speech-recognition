from speech_to_text import listen_commands
from commands.commands import assistant_commands

TRIGGER_WORDS = ('ассистент', 'помощник', 'привет')

def handle_speech(text: str):
    if not text: 
        return

    print(f'Распознано: "{text}"')

    if not any(name in text for name in TRIGGER_WORDS):
        return
    
    for fn, aliases in assistant_commands:
        if any(alias in text for alias in aliases):
            fn()
            break

if __name__ == '__main__':
    listen_commands(handle_speech)