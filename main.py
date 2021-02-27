def greet(name = None):
    greeting = 'hello'
    if name:
        print(f"{greeting}, {name}")
        return
    print(greeting)

if len(sys.argv) > 1:
    name = sys.argv[1]
    greet(name)
else:
    greet()
