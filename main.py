import sys
import random

def get_rand_greeting():
    return random.choice(["Hi", "Hello", "How you doing"])

def greet(name):
    greeting = get_rand_greeting()
    if name:
        print(f"{greeting}, {name}")
    else:
        print(greeting)

if __name__ == "__main__":
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]
    greet(name)
    
