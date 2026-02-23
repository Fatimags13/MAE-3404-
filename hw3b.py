#region imports
from math import sqrt, pi, gamma
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

#endregion


#region t-distribution functions

def t_integrand(u, m):
    """
    Integrand for Student t-distribution.
    """
    return (1 + u**2/m)**(-(m+1)/2)


def t_probability(z, m):
    """
    Computes P(T < z) for Student t-distribution.
    """
    Km = gamma((m+1)/2) / (sqrt(m*pi) * gamma(m/2))

    lower = -50     # approximate -infinity
    integral = Simpson(t_integrand, lower, z, 2000, m)

    return Km * integral

#endregion


#region main

def main():
    """
    HW3 Part (b)
    Computes t-distribution probability.
    """

    print("HW3 – Part (b)")
    print("---------------------------")

    m = int(input("Enter degrees of freedom (m): "))
    z = float(input("Enter z value: "))

    P = t_probability(z, m)

    print("P(T < {:.4f}) = {:.6f}".format(z, P))

#endregion


if __name__ == "__main__":
    main()
