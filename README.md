# shoot_the_star_game-python
A simple shooting game (shoot the star game) with Python pygame. 

# Shooting Game: Shoot the Star (Game Development)

# About

- My first game. A Simple shooting game with Python - Pygame modules.
- The Player (rocket) has to shoot the target (star) at least 20 times to win. The player will gain one point if they shoot the target.
- All control using keyboard keys (arrow left and right key to move the player and space key to shoot), play, pause, restart and quit game.
- Playing time 30 seconds. Game over when reach timer set.
- Game over if the player (rocket) collide with target (star).

# Package and Setup

Pygame packages. You can install it using the command in the terminal:

```python
pip3 install pygame 
```

# Requirement

- image filename in png (I have include in this project but you can also change your own)
- sound filename in mp3 (I have include in this project but you can also change your own)
- font - in this project i used retro font (.ttf) - file extension (I have include in this project but you can also change your own)
- import the package/module in your .py file

```python
import pygame 
import random
```

# Game instruction

- Press “Enter’ key to start the game
- Press ‘Q’ or Quit to exit the game
- Press ‘P’ to pause and resume playing
- Press ‘R’ to restart playing (after game over)
- Press ‘Left and Right’ arrow to move and ‘Space’ bar to shoot

# Project outcome

![View 1](https://github.com/Hilmisuhaimi/shoot_the_star_game-python/assets/81658376/fa7ef95d-3855-42ef-8fde-664d68559088)

![View 2](https://github.com/Hilmisuhaimi/shoot_the_star_game-python/assets/81658376/90fb51e3-1854-4729-a41a-b5efa8078f1f)

![View 3](https://github.com/Hilmisuhaimi/shoot_the_star_game-python/assets/81658376/3550e2ab-7008-43d3-bf3f-41b95ce8752d)

![View 4](https://github.com/Hilmisuhaimi/shoot_the_star_game-python/assets/81658376/73c87c0d-b9b9-4614-ad5b-7c996cd6bcf9)

# Installation - build a desktop app (MacOS)

- Make the game to desktop app using py2app
- First, install the py2app

```
pip3 install py2app
```

- Before that make sure to install setuptools

```
pip3 install setuptools 
```

- import the package in [setup.py](http://setup.py) (included)

```python
from setuptools import setup 
```

- Run the [setup.py](http://setup.py) in terminal to start building the app

```
python3 setup.py py2app -A
```

- Once done, you can find the app under /dist directory (same as the game directory) and launch the app. You can also move the app under application folder

# Acknowledgement and Credit

- Throughout this project, I have learn the basic pygame and python using various channel, resources and site. I would like to give a credit and thank you to all the developer and people who share they knowledge. Doing the project, I have apply the practice and coding skills on what I ave learned so far.

# Future improvement or feature

- In the future I will like to added more instances and feature in this game such as add levels, players of two and more.
