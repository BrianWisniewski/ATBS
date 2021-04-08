def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
        elif num % 2 == 1:
            num = num * 3 + 1
            print(num)
while True:
    print("Enter your number here:")
    try:
        num = int(input())
        collatz(num)
    except ValueError:
        print('Please enter a valid number.')

