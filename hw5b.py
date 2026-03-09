# region imports
import hw5a as pta
import random as rnd
from matplotlib import pyplot as plt
import numpy as np
# endregion


# region functions
def ffPoint(Re, rr):

    if Re >= 4000:
        return abs(pta.ff(Re, rr, CBEQN=True))

    if Re <= 2000:
        return abs(pta.ff(Re, rr))

    CBff = abs(pta.ff(Re, rr, CBEQN=True))
    Lamff = abs(pta.ff(Re, rr, CBEQN=False))

    mean = Lamff + (CBff - Lamff)*(Re-2000)/2000
    sig = 0.2*mean

    f = rnd.normalvariate(mean, sig)

    return abs(f)


def getInputs():

    print("\n--- Enter Pipe Parameters ---")

    d_in = float(input("Pipe diameter (inches): "))
    eps_mic = float(input("Pipe roughness (micro-inches): "))
    Q_gpm = float(input("Flow rate (gallons/min): "))

    return d_in, eps_mic, Q_gpm


def computeHeadLoss(d_in, eps_microin, Q_gpm):

    nu = 1.08E-5
    g = 32.174

    D = d_in/12.0
    eps = eps_microin*1E-6/12.0
    Q = Q_gpm*0.13368/60.0

    A = np.pi*D**2/4.0
    V = Q/A

    Re = V*D/nu
    rr = eps/D

    f = ffPoint(Re, rr)

    hf_per_L = f*V**2/(D*2*g)

    return Re, rr, f, hf_per_L, V


def main():

    points = []

    while True:

        d_in, eps_mic, Q_gpm = getInputs()

        Re, rr, f, hf_per_L, V = computeHeadLoss(d_in, eps_mic, Q_gpm)

        print("\n--- Results ---")
        print(f"Velocity:              {V:.4f} ft/s")
        print(f"Reynolds Number:       {Re:.2f}")
        print(f"Relative Roughness:    {rr:.6f}")
        print(f"Friction Factor (f):   {f:.6f}")
        print(f"Head Loss per foot:    {hf_per_L:.6f} ft/ft")

        points.append((Re,f))

        pta.plotMoody()

        for Re_pt, f_pt in points:

            if 2000 < Re_pt < 4000:
                plt.plot(Re_pt, f_pt, '^', markersize=10, color='red')
            else:
                plt.plot(Re_pt, f_pt, 'o', markersize=10, color='red')

        plt.show()

        again = input("\nEnter another set of parameters? (y/n): ").strip().lower()

        if again != 'y':
            break

    print("Done.")
# endregion


# region function calls
if __name__ == "__main__":
    main()
# endregion
