import PySimpleGUI as sg      
import random
import hashlib
adj = [
    'needless',
    'overwrought',
    'changeable',
    'abnormal',
    'living',
    'thoughtful',
    'scattered',
    'devilish',
    'yellow',
    'loud',
    'foregoing',
    'gruesome',
    'weary',
    'tiny',
    'willing',
    'thoughtful',
    'educated',
    'glorious',
    'majestic',
    'godly'
]
noun = [
    'kitten',
    'father',
    'chicken',
    'machine',
    'dad',
    'bat',
    'sock',
    'tiger',
    'actor',
    'cat',
    'eggs',
]

x = random.choice(adj) + ', '  + random.choice(adj) + ', ' + random.choice(adj) + ' ' + random.choice(noun)
y =  x.encode('utf-8')
h = hashlib.md5(y).hexdigest()
sg.popup(x + " " +  h, title="KeyGen", font=35, background_color='black')
