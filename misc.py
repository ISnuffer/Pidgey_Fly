import keyboard

def anyKeyPressed():
    keys = ['a', 'space', 'enter']
    for key in keys:
        if keyboard.is_pressed(key):
            return True
    return False