from setuptools import setup

APP = ['stargame.py']
DATA_FILES = ['background.png','player.png','star.png','Game_bgsound.mp3','Game_clap.mp3','Game_over.mp3','Game_playing.mp3','Game_start.mp3','Game_win.mp3','Pop_sound.mp3','retro.TTF'] 
OPTIONS = {'iconfile' : 'icon.png', 'packages': ['pygame', 'random']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

  