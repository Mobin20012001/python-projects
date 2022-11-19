import time
from pynput import keyboard , mouse

m = mouse.Controller()
k = keyboard.Controller()

time.sleep(5)
m.position = (300,300)
time.sleep(1)
m.click(mouse.Button.right)
time.sleep(1)
k.tap(keyboard.Key.down)
time.sleep(1)
k.tap(keyboard.Key.down)
time.sleep(1)
k.tap(keyboard.Key.down)
time.sleep(1)
k.tap(keyboard.Key.enter)
time.sleep(1)
k.tap(keyboard.Key.enter)
time.sleep(3)
k.type("mobin")
time.sleep(1)
k.tap(keyboard.Key.enter)