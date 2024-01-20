import math

def print_squares():
    """
    Prints the square of all integers from 1 to 10 inclusive.
    """
    for i in range(1, 11):
        print(i ** 2)

def average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    if not isinstance(numbers, list):
        return None

    total = 0
    count = 0

    for num in numbers:
        if not (isinstance(num, (int, float))):
            return None
        total += num
        count += 1

    return total / count if count > 0 else 0

if __name__ == '__main__':
    print(average([3, 4, 5, 6]))
    print(average([-2.3, 45, 0.111, 11/6]))
    print(average([]))  # Returns 0
    print(average([1.0, 1.0, -math.inf]))
    print(average([1, 3.14, "h"]))
    print(average("hello?"))
    print(average([1, 2, 3, 4].extend([5])))  # what happens here?

def is_prime(num):

    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) +1):
        if num % i == 0:
            return False
    return True

def prime_100():
    """
    list of the first 100 prime numbers.
    """
    primes = []
    num = 2

    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes

def count_letters(s):
    """
    Counts the number of occurrences of each letter in a string.
    """
    s = s.lower()
    letter_count = {}

    for char in s:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count

if __name__ == '__main__':
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))

def filter_strings(string_list):
    """
    Filters strings based on vowel presence and length.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    filtered_strings = [s for s in string_list if len(s) >= 5 and any(char.lower() in vowels for char in s)]
    return filtered_strings

if __name__ == '__main__':
    testcase = ["joyyyyyy", "bananaaaaaaaaa", "catttt", "elephant"]
    print(filter_strings(testcase))

def is_palindrome(num):
    """
    Checks if a number is a palindrome.
    """
    num_str = str(num)
    return num_str == num_str[::-1]

if __name__ == '__main__':
    print(is_palindrome(1234567.7654321))
    print(is_palindrome(-0.123))