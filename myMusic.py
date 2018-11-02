import os, time
from tinytag import TinyTag
import random, quantumrandom

trulyRandom = False
path = ""
Musicpath = ""
def randint(min, max):
    if trulyRandom:
        return int(quantumrandom.randint(min, max))
    else:
        return int(random.randint(min, max))

def init(TR, PTH, MPTH):
    global trulyRandom
    global path
    global Musicpath
    trulyRandom = TR
    path = PTH
    Musicpath = MPTH
    os.chdir(path)

def getRandSong():
    global Musicpath
    song = Musicpath + os.listdir(Musicpath)[randint(0, len(Musicpath))]
    return song

def getTags(song):
    tag = TinyTag.get(song)
    return(tag)

def playSong(song, durationTag, playFor=randint(20, 120)):
    print("Playing for: ", playFor)
    uL = randint(playFor, int(durationTag))
    variable = " --start-time " + str(uL-playFor) + " --stop-time " + str(uL)
    constant = " --play-and-exit --qt-start-minimized"
    opts = variable + constant
    os.system("vlc " + song + opts)

def printTags(tag):
    print('Now Playing: %s.' % tag.title)
    print('By: %s' % tag.artist)
    print('From the Album: %s' % tag.album)


def cls():
    os.system("cls")
