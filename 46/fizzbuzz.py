# div by 3 Fizz
# div by 5 Buzz
# div by 3 & 5 FizzBuzz
# else num
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num