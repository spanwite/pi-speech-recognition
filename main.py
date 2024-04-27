from speech_to_text import listen_commands
from features.light_control import light_control
from rapidfuzz import fuzz

features = [*light_control]

def handle_speech(text: str):
    if not text: 
        return
    
    print(f'Распознано: "{text}"')

    res_percent = 0
    res_action = None

    for action, aliases in features:
        percent = fuzz.ratio(text, aliases)
        if percent > res_percent:
            res_percent = percent
            res_action = action

    if res_percent > 70:
        if not res_action is None:
            res_action()
            
if __name__ == '__main__':
    listen_commands(handle_speech)
