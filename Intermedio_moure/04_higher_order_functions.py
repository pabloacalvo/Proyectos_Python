### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5
def sum_two_values_and_add_value(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add_value(5,2,sum_one))
print(sum_two_values_and_add_value(5,2,sum_five))


### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
add_closure = sum_ten()
print(add_closure(5))