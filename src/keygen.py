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
    'godly',
    'evasive',
    'impossible',
    'serious',
    'enormous',
    'fresh',
    'pointless',
    'juicy',
    'fabulous',
    'graceful',
    'excited',
    'premium',
    'terrific',
    'wacky',
    'wonderful',
    'cute',
    'petite',
    'overjoyed',
    'safe',
    'deafening',
    'abusive'
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
print(h, x)
