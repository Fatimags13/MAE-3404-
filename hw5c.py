# region imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# endregion


# region functions
def ode_system(t, X, *params):
    """
    ODE system for the hydraulic valve system
    X[0] = x
    X[1] = xdot
    X[2] = p1
    X[3] = p2
    """

    # unpack parameters
    A, Cd, ps, pa, V, beta, rho, Kvalve, m, y = params

    # state variables
    x = X[0]
    xdot = X[1]
    p1 = X[2]
    p2 = X[3]

    # differential equations
    xddot = (p1 - p2) * A / m

    p1dot = (y * Kvalve * (ps - p1) - rho * A * xdot) * beta / (V * rho)

    p2dot = -(y * Kvalve * (p2 - pa) - rho * A * xdot) * beta / (rho * V)

    return [xdot, xddot, p1dot, p2dot]


def main():

    # time span
    tspan = (0, 0.02)
    t_eval = np.linspace(0, 0.02, 200)

    # parameters
    params = (4.909E-4, 0.6, 1.4E7, 1.0E5, 1.473E-4, 2.0E9, 850.0, 2.0E-5, 30, 0.002)

    # initial conditions
    pa = params[3]
    IC = [0, 0, pa, pa]

    # solve ODE system
    sol = solve_ivp(
        ode_system,
        tspan,
        IC,
        t_eval=t_eval,
        args=params
    )

    # extract solution
    t = sol.t
    xdot = sol.y[1]
    p1 = sol.y[2]
    p2 = sol.y[3]

    # --------------------------------------------------
    # Plot 1: xdot vs time
    # --------------------------------------------------
    plt.figure()

    plt.plot(t, xdot)
    plt.title("Piston Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity xdot (m/s)")
    plt.grid(True)

    # --------------------------------------------------
    # Plot 2: p1 and p2 vs time
    # --------------------------------------------------
    plt.figure()

    plt.plot(t, p1, label="p1")
    plt.plot(t, p2, label="p2")

    plt.title("Chamber Pressures vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Pressure (Pa)")
    plt.legend()
    plt.grid(True)

    plt.show()


# endregion


# region function calls
if __name__ == "__main__":
    main()
# endregion
