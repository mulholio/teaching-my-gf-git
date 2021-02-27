import sys
import random

def greet(name = None):
    greeting = get_rand_greeting()
    if name:
        print(f"{greeting}, {name}")
        return
    print(greeting)

def get_rand_greeting():
    return random.choice(["Hi", "Hello", "How you doing"])

if len(sys.argv) > 1:
    name = sys.argv[1]
    greet(name)
else:
    greet()
