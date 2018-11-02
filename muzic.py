import myMusic as mm
import os, time

trulyRandom = True # Adds a small delay if true
VLCpath = """C:\\Program Files (x86)\\VideoLAN\\VLC\\"""
Musicpath = """C:\\Users\\Rishi\\Music\\Playlist\\"""

mm.init(trulyRandom, VLCpath, Musicpath)
for i in range(0, 100):
    rs = mm.getRandSong()
    tag = mm.getTags(rs)
    mm.printTags(tag)
    mm.playSong(rs, tag.duration)
    mm.cls()
