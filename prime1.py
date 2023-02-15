def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes_in_list(lst):
    for num in lst:
        if prime(num):
            print(num, "is prime")
        else:
            print(num, "is not prime")

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
check_primes_in_list(numbers)
