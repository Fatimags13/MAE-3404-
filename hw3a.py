#region imports
from math import sqrt, pi, exp
#endregion


#region numerical methods

def Simpson(f, a, b, n, *args):
    """
    Simpson's 1/3 rule for numerical integration.
    :param f: function to integrate
    :param a: lower limit
    :param b: upper limit
    :param n: number of subintervals (must be even)
    :param args: additional parameters passed to f
    :return: approximate integral value
    """
    if n % 2 == 1:
        n += 1

    h = (b - a) / n
    s = f(a, *args) + f(b, *args)

    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            s += 2*f(x, *args)
        else:
            s += 4*f(x, *args)

    return s*h/3


def Secant(f, x0, x1, maxiter, xtol):
    """
    Secant method for root finding.
    :param f: function
    :param x0: first guess
    :param x1: second guess
    :param maxiter: maximum iterations
    :param xtol: tolerance
    :return: root approximation
    """
    for _ in range(maxiter):
        f0 = f(x0)
        f1 = f(x1)

        x2 = x1 - f1*(x1-x0)/(f1-f0)

        if abs(x2 - x1) < xtol:
            return x2

        x0 = x1
        x1 = x2

    return x1

#endregion


#region normal distribution

def GPDF(x, mu, sigma):
    """
    Gaussian probability density function.
    """
    return (1/(sigma*sqrt(2*pi))) * exp(-0.5*((x-mu)/sigma)**2)


def Probability(mu, sigma, c):
    """
    Computes P(x < c) for a normal distribution.
    """
    lower = mu - 5*sigma
    return Simpson(GPDF, lower, c, 1000, mu, sigma)


def FindC(mu, sigma, P):
    """
    Finds c such that P(x < c) = P using Secant method.
    """
    def fn(c):
        return Probability(mu, sigma, c) - P

    return Secant(fn, mu, mu+sigma, 100, 1e-6)

#endregion


#region main

def main():
    """
    HW3 Part (a)
    Computes normal probability or finds c value.
    """

    print("HW3 – Part (a)")
    print("---------------------------")

    mu = float(input("Enter mean (mu): "))
    sigma = float(input("Enter standard deviation (sigma): "))

    print("1: Compute P(x < c)")
    print("2: Find c for given probability")

    choice = int(input("Select option (1 or 2): "))

    if choice == 1:
        c = float(input("Enter c value: "))
        P = Probability(mu, sigma, c)
        print("P(x < {:.4f}) = {:.6f}".format(c, P))

    elif choice == 2:
        P = float(input("Enter probability: "))
        c = FindC(mu, sigma, P)
        print("c = {:.6f}".format(c))

    else:
        print("Invalid selection.")

#endregion


if __name__ == "__main__":
    main()
