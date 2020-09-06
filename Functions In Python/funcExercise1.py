def compute(rad, num):

    import random as rd
    
    rd.seed(10)
    
    numbers = range(1, rd.randint(1, rad))
    
    calc = []
    for i in range(len(numbers)):
    
        if numbers[i] %2 == num and numbers[i] > 10:
            s = numbers[i]
            calc.append(s)
            
        else:
            s = 0
            calc.append(s)
    print(sum(calc))
    
    return calc

print(compute(20, 1))