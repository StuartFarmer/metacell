# Metacell

## A toolkit for making funges (2D programming languages), cellular automata / computers, and programs for them.

<img align="left" width="100" height="100" src="https://github.com/StuartFarmer/metacell/raw/master/media/rotDNA.gif">

Clone the repo and run the following to preview a demo application in Vanilla Metacell
```
python3 main.py
```

---

<p align="center">
  <img src="https://github.com/StuartFarmer/metacell/raw/master/media/celluar.gif"/>
</p>

## Why?

I've been into esoteric programming languages since I was little (which actually coincidentally ended up becoming a programming challenge for some people 1 2 3). A very popular esoteric language is Befunge which uses a 2D board and a cursor that wizzes around reading instructions is comes across and executing commands. Example interpreter here.

```
>              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@
```

I really liked this idea and wanted to make something similar. However, because recreating Befunge wasn't super interesting, I decided I wanted it to operate more like a pipeline. Because I play a lot of Factorio, I thought it would be pretty funny to make the funge feel like you were laying out machinery and pushing it down conveyor belts, etc.

<p align="center">
  <img src="https://github.com/StuartFarmer/metacell/raw/master/media/factorio.png"/>
</p>

However, as I started coding, I found that it was pretty similar to cellular automata (such as Conway's Game of Life and Langston's Loops) and so I started to think of it in this way. Artificial life is super interesting to me as well, especially systems that can self-modify themselves and begin to solve problems / speciate without human intervention.

<p align="center">
  <img src="https://github.com/StuartFarmer/metacell/raw/master/media/life.gif"/>
</p>

Ergo, I started to combine the two ideas and survey a lot of the cellular automata out there using Golly. Similarly, I was writing up an instruction set that was somewhat similar to Befunge, but focused more on moving data around rather than a single cursor. I wrote up a spec of commands that looked something like this:

```
> : push cell east
< : push cell west
^ : push cell north
V : push cell south
0 : represent a byte of zero
~ : copy the cell and emit it east
...
```

I then started to realize that I could go on and on and make hundreds of permutations of copying, rotating, and modifying cells which would just turn into a complex mess. I probably want to write something that allows people to describe their own command sets so that the ideal group of commands comes out of the community that ends up using it based on needs rather than my ideal dictatorial set.

*So I made it **Meta***.

Everyone knows that meta means better /s

## Goals

The goal of this project is to develop a library that allows you to either design your own funge language, or use one out of the box to solve interesting problems. I want the ability to describe artifical neurons in my Vanilla Metacell language, so I will be releasing something that can accomplish this type of data processing.

For using one out of the box, a UI is probably going to be developed. I am looking at classic Curses and Qt.

For describing new cell behaviors, the status quo is to extend the library with Python. This may change if I get bored.

## Status

I'm developing this on weekends to keep busy and challenge myself in a different way than my day job. It allows me to explore and hack and get the itch out of me so I can manage my business when I get back to work. Right now, I am developing the Vanilla implementation which will be made public when it is ready.
