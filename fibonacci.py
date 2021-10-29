number1 = 0
number2 = 1

def fibonacci(number1, number2):
    number3 = number1 + number2
    return number3
    
for x in range(9):            
    print(fibonacci(number1, number2))
    numberExtra = fibonacci(number1, number2)
    number1 = number2
    number2 = numberExtra