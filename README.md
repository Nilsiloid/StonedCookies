# StonedCookie

### Contents:
- [Inspiration](#installation)
- [Introduction](#introduction)
- [How to Run](#how-to-run)
- [Challenges](#challenges)
- [Features](#features)
- [Commands](#commands)

### Inspiration

Often students' voice, suggestions, ideas and complaints regarding the "system" remain unheard. This could be due to many reasons, majorly being the lack of confidence and the fear of superiors/seniors. These are some issues that we and our peers faced. Us being college students, we thought if our voice /suggestions/complaints could be heard by our peers, seniors and other officials without getting our identity doxxed that would solve more than half of our problems! Hence we got the idea to implement $confess command. Now students issues/sugestions could be logged annonymously in an specific a channel in the server that would be visible all.

We also wanted to track our study timings and thus our study schedule. We decided to use this opportunity to create a Discord bot which will join our voice channel and use the $study command to set a timer. We then thought about adding additional features such as trivia and music to help us during such study sessions.

### Introduction

StonedCookie is the name of our Discord bot.
We used Python to code our bot. It has several functions, some of which are listed below:

* Confess - an anonymous complaint/suggestion feature for users to give feedback about happenings in the server/organisation around the server, etc.
* Study - The bot will set a timer for your study session.
* Music - Many people like to listen to music while studying. This function performs precisely that xD.
* Trivia - Sudden urge to answer a random question? Our unique trivia feature is there for this.

### How to Run

Once you fork the repo and download the code, you will need to use the following commands in the respective terminal of your system.

    pip install discord.py
    
    pip install ast
    
    pip install PyNaCl
    
    pip install youtube_dl
    
    pip install python-dotenv
    
    pip install requests


### Challenges

We ran into multiple challenges as this was our first time coding a discord bot. Syntax errors, debugging code due to errors. Combining our codes was also difficult as both our styles of writing codes is different.

### Features:

* Study is to set a timer for your study session. Helps track study schedule.

* Confess is an anonymous complaint/suggestion feature for users to give feedback about happenings in the server/organisation around the server, etc.

* Tic-Tac-Toe is a basic implementation for pass time between 2 friends.

### Commands

### All commands are run using the prefix : '$'

* Study-commands:

    $**join** - joins the voice channel the user is present in.
    
    $**study** - starts our study session and timer.
    
    $**stop_study** - ends our study session and displays the amount of time we studied once we are done.
    
    $**leave** - leaves the voice channel.
    
* Music-commands:

    $**play** - plays the song we want to listen to using the YouTube url.
    
    $**pause** - pauses the song currently playing.
    
    $**resume** - resumes the paused song.
    
    $**stop** - stops the song.
    
* Confess-commands:
    
    $**confess** - dm the confession to the bot which will send it to the respective channel.
    
    $**setconfess** - shows all the channels existing and initializes process of setting the channel where all confession would be logged.
    
    $**setid** - sets the channel using its id.
    
* TicTacToe-commands:
    
    $**tictactoe** - tag 2 people and start your own game of tic tac toe.
    
    $**place** - places your token(X or O) in the given position you pass after place.
    
* Trivia-commands:
    
    $**trivia** - shows the different categories of questions. Messaging the number will then cause the bot to reply with a question.
    
* UrMOM-commands:
    
    $**urmom** - generates a Your Mom joke.
    
* Misc-commands:
    
    $**kick** - kicks user mentioned from the server.
    
    $**help** - shows the commands and their functioning.
    
