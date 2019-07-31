import pyglet
from datetime import datetime

now = datetime.now()

stop = False
while stop == False:
    rn = str(datetime.now().time())

    if rn >= "19:20:00.000000":
        music = pyglet.resource.media('sample.wav')
        music.play()
        pyglet.app.run()
        stop = True