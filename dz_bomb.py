import time

while True:
    t = 0

    t = int(input())
    for q in range(t):
        time.sleep(1)
        t -= 1
        print(t)

    print('Boom!!')
    break