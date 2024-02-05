# Marlesha Ellis
# Homework 2
# Part A
#I used the internet for majority of my code.  Chatgpt as well

from math import sqrt, exp, pi
# Importing my math functions needed to work the problem


def Probability(PDF, args, c, GT=True):
    '''this is defining the probability'''


    # Integration need to be used to integrate PDF between x=m-5*s and c, where b=c

    a = args[0]-args[1]*5
    b = c
    nPoints = 1000

    # I am defining the  area under the curve
    area=Simpson(PDF, args, a, b, nPoints)

    # Calculate the probability
    # If GT=True, then it will be the first return, but if it is not then it will not be first
    if GT:
        return 1-area
    else:
        return area




def GNPDF(x, args):

    m,s = args
    # Create the function (Fn) for the GNPDF and return the resultant
    Fn = (1/(s*sqrt(2*pi))) * exp(-0.5*((x-m)/s)**2)
    return Fn


def Simpson(fcn, args, a, c, nPoints=1000):
    '''this is defining the simspson rule.  the simpson rule is used to define definite integrals'''

    #  calculating  the value for h
    a = args[0] - args[1]*5
    b = c
    h = (b-a)/nPoints

    # List for the values for x
    x = list()
    # List for the values for f(x)
    fx = list()

    I = 0
    # Loop until all iterations are done
    while I <= nPoints:
        x.append(a+I*h)
        fx.append(fcn(x[I], args))
        I += 1

    # Create a list to store values
    result = 0
    I = 0

    while I <= nPoints:
        if I == 0 or I == nPoints:
            result += fx[I]
        elif I % 2 != 0:
            result += 4*fx[I]
        else:
            result += 2*fx[I]
        I += 1
    result = result*(h/3)
    return result



def main():
    """
    This function uses the probability function to find P(x<1|N(0,1)):
    """

    # Re-pack  and define value of c
    args = (0, 1)
    c = args[0]+args[1]
    # Give the solution for P(x<1.00|N(0,1)), rounded to 2 decimals
    P1 = Probability(GNPDF, args, c, GT=False)
    print("Probability of x<105 in a normal distribution between (100,12.5): {:0.2f}%".format(P1*100))


    args = (175, 3)
    c = args[0] + 2*args[1]
    P2 = Probability(GNPDF, args, c, GT=True)
    print("Probability of x>181.00 in a normal distribution between (175,3): {:0.2f}%".format(P2*100))



main()