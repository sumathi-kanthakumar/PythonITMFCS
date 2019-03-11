def printEvenNumbers(x):
    '''
    List all the even number less than the input number
    '''
    return [num for num in range(x) if num%2==0]
output = printEvenNumbers(21)
