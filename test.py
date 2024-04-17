from sympy import diff
from sympy.abc import x

# get the string input from the command line as a python expression for feeding into subsequent functions

a = eval(input("please enter a polynomial function with a variable x. use * for multiplication and ** for exponentiation: \n")) # 3*x**2 - 3

b = diff(a, x) # differentiate the function and save the differentiated function in a variable

print(b) # confirm this is the differentiation

guess_input = float(input("guess"))

def new_raph(guess, function, differentiated_function): # take guess, function, and differentiated function as parameters
    
    # print the numerator and denominator of the newton-raphson method formula

    numerator = float(function.subs(x, guess))
    denominator = float(differentiated_function.subs(x, guess))

    print(numerator)
    print(denominator)

    # return the full formula with the plugged in guess
    return guess - numerator/denominator

temp = new_raph(guess_input, a, b) # first iteration with plugged in first guess

print(f"root for iteration 1: {temp}")

iters_wanted = 9 # number of iterations after the first iteration 

loop_count = 1 # 1 is the second iteration

while loop_count < iters_wanted: # for every count up to the iters_wanted, execute the following

    print(loop_count)

    temp = new_raph(temp, a, b) # save the iteration's output to the temp variable outside the loop originally : temp = new_raph(guess_input, a, b)

    print(f"root for iteration {loop_count}: {temp}") # print the iteration's root

    loop_count += 1 # move to the next iteration

print(f"final root at is at x = {temp}") # print the final root c: