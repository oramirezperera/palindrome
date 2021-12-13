def is_prime(number: int) -> bool:
    """ Returns true if a number is prime false if not"""
    number = int(number)

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    
    else:
        return False

def run():
    print(is_prime(1))


if __name__ == '__main__':
    run()