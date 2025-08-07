'''
LEVEL 1 CHALLENGE - HAPPY PRIDE MONTH
    Write a program that prints "Hello World" every 0.1 seconds, forever.
    Each printed line should be a different color than the previous line.
'''

# This is an "import", ignore this for now, you're too hot and rich to understand this.
import time
from rich import print

DefaultColor = "\033[0m"
Blue = "\033[94m"
Red = "\033[91m"
Purple = "\033[95m"
Green = "\033[92m"
Yellow = "\033[93m"

while True:
    print(Blue + "Hello World")
    time.sleep(.1)
    print(Red + "Hello World")
    time.sleep(.1)
    print(Purple + "Hello World")
    time.sleep(.1)
    print(Green + "Hello World")
    time.sleep(.1)
    print(Yellow + "Hello World")
    time.sleep(.1)
    print(DefaultColor + "Hello World")
    

    pass # TODO - Replace this with your code!
