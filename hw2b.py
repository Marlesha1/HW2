# Marlesha Ellis
# Homework 2
# Part B
#I used the internet for majority of my code.  Chatgpt as well

from math import cos

# I am creating the secant
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):



    # This will start at 1 not 0
    I=0

    # I am going to use a whiloop
    while abs(x0-x1)>=xtol and I<=maxiter:
        # sec method is being made
        x2=x1-(fcn(x1)*(x1-x0))/(fcn(x1)-fcn(x0))
        x0=x1
        x1=x2
        # I am adding the values of iteration here
        I+=1
        return x2


def main():

    # print the first function
    F1=lambda x:x-3*cos(x)
    print("Solution of x-3cos(x)=0, with x0=1, x1=2, maxiter=5, and xtol=1e-4: {:0.2f}".format(Secant(F1,1,2,5,1e-4)))

    # Print the second function
    F2=lambda x:cos(2*x)*x**3
    print("Solution of cos(2x)*x^3=0, with x0=1, x1=2, maxiter=15, and xtol=1e-8: {:0.2f}".format(Secant(F2,1,2,15,1e-8)))

    # Print the third function
    F3=lambda x:cos(2*x)*x**3
    print("Solution of cos(2x)*x^3=0, with x0=1, x1=2, maxiter=3, and xtol=1e-8: {:0.2f}".format(Secant(F3,1,2,3,1e-8)))

main()