## Lambdas ###

sum_two_value = lambda firs_value, second_value: print(firs_value + second_value)
sum_two_value(2,5)

multiply_values =  lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2,4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
