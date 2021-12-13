def odd_or_not(number: int) -> bool:
    number = int(number)
    return number % 2 != 0

def run():
    print(odd_or_not(101))

if __name__ == '__main__':
    run()
