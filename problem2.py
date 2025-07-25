"""
The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def even_or_odd(num: int) -> str:
    #number = int(input('Digite o numero'))
    return "even" if num%2==0 else "odd"

"""if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')"""
 










# Test inputs for even_or_odd
print(even_or_odd(2))      # Even
print(even_or_odd(3))     # Odd
print(even_or_odd(4))      # Multiple of 4
print(even_or_odd(0))     # Edge case: zero
print(even_or_odd(-1))     # Negative odd
print(even_or_odd(-4))   # Negative multiple of 4