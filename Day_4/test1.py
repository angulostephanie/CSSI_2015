# practice file


def FizzBuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return ""
def FizzBuzz2(n):
    s = ""
    if n%3 == 0:
        s = s + "Fizz"
    if n%5 == 0:
        s = s + "Buzz"
    return s

print FizzBuzz(15)
print FizzBuzz(3)
print FizzBuzz(5)
print FizzBuzz(4)
