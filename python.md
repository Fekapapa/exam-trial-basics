# TRIAL EXAM: Programming Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.
- **Don't push your work** to GitHub until your mentor announces that the time is up


# Tasks
## 1-4. Complete the following tasks: (~180 mins)

- [Seconds](seconds/seconds.py)
- [Count A-s](countas/count-as.py)
- [Pirates](pirates/pirates.py)
- [Box](box/box.py)

### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://google.github.io/styleguide/pyguide.html) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 5. Question time! (~15 mins) [2p]

### How can you generate a random number? [2p]
#### Your answer: To generate a random number in python you have to import the random method from the python library with "import random" command. From the random method you have to use the random function to generate a number. This number on default will be a number between 0 and 1. Here is an example:

import random
random.random()

If you want to display this number, you have to print it:

print(random.random())

It is possible to give a range for the random to generate numbers in it. The example below will generate a number between 2 and 12:

random.randrange(2, 12)
