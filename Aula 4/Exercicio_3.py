from time import sleep

x = 10
print(x)
sleep(1)

while x > 1:
    x -= 1
    print(x)
    sleep(1)
    if x == 0:
        print("Fogo!")