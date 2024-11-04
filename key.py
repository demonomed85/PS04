from pynput import keyboard

def on_press(key):
    try:
        # Если клавиша имеет символ, выводим ее и соответствующий код
        print(f'Клавиша: {key.char} | Код: {ord(key.char)}')
    except AttributeError:
        # Для специальных клавиш (например, Enter, Shift и т.д.)
        print(f'Клавиша: {key} | Код: {key.value}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Останавливаем слушатель
        return False

# Начинаем слушать нажатия клавиш
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()