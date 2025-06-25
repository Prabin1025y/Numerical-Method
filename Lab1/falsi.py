import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using python syntax: ")
def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

a = float(input("Enter the first initial approximation: "))
b = float(input("Enter the second initial approximation: "))
approx = []

if f(a)*f(b) > 0:
    print(f"No solution lies in internval ({a},{b})")
else:
    error_tolerate = float(input("Enter the tolerable error: "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    iteration = 1

    A = []
    

    while iteration <= max_iterations:
        c = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))

        A.append([iteration, a, b, c, f(a), f(b), f(c)])
        approx.append(c)

        if f(a)*f(c)<0:
            b = c
        else:
            a = c
        
        error = abs(f(c))
        if error < error_tolerate:
            df = pd.DataFrame(A, columns=["iterations",'a','b','c','f(a)','f(b)','f(c)'])
            print(df.to_string(index=False))
            print(f'Approx root is {c} in {iteration} iterations.')
            break
        iteration += 1

    if(iteration > max_iterations):
        print(f"Solution does not converge in {max_iterations} iterations!")

midpoint = np.array(approx)
x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), color='red', label=eqn)

plt.axhline(0,0,color='black')
plt.axvline(0,0,color='black')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Falsi method")
plt.legend()
plt.scatter(midpoint, f(midpoint))
for i, value in enumerate(midpoint):
    plt.text(value, f(value), f'{i}')
plt.show()