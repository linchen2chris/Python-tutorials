import sys
for i in sys.argv:
    print(i)

print(sys.path)

i = 5
print(i)

def sayHello(message, times = 1):
    print(message*times)

sayHello('hello')
sayHello('hello', 5)
