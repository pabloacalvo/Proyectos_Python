### Challenges ###

"""
Escribe un pograma que muestre por consolta los numeros de 1 a 100 (ambos incluidos con un salto de linea)
sustituyendi os siguientes:
-Multiplos de 3 por la palabra "fizz"
-Multiplos de 5 por la palabra "buzz"
-Multiplos de 3 y 5 de 5 a la vez por la palabra "fizzbuzz"
"""

def fizzbuzz ():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)
#fizzbuzz()

"""
Anagramas:
sorted- Ordena las letras de un string 
"""

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram('Amor', 'Roma'))

"""
Fibonacci
"""

def fibonacci():
    prev = 0
    next = 1
    for i in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib




fibonacci()