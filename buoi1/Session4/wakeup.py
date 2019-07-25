import pyglet
from datetime import datetime
while True:
    now = datetime.now().time()
    print(now)
    if now == datetime(2019, 7, 23, 1, 24, 30, 000000):
        music = pyglet.resource.media('sample.wav')
        music.play()
        pyglet.app.run()
        break