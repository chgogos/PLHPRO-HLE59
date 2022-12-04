def countdown(num):
    if num <= 0:
        print("Stop")
    else:
        print(num)
        countdown(num - 1)


countdown(10)
