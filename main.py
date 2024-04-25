from core.speech_to_text import listen_commands
from core.text_to_speech import say_text
from features.light_control import light_control

assistant_names = ('ассистент', 'помощник')
assistant_features = [*light_control]

def handle_speech(text: str):
    if not text: 
        return
    
    print(f'Распознано: "{text}"')

    if not any(name in text for name in assistant_names):
        return
    
    for action, commands in assistant_features:
        if any(command in text for command in commands):
            action()
            return

    say_text('Я вас не понял. Повторите команду')

if __name__ == '__main__':
    listen_commands(handle_speech)