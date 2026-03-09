# region imports
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
# endregion


# region functions
def ff(Re, rr, CBEQN=False):
    """
    This function calculates the friction factor for a pipe based on the notion
    of laminar, turbulent and transitional flow.

    If CBEQN is True, use the Colebrook equation with fsolve to find f.
    If CBEQN is False, use the laminar equation f=64/Re.
    """

    if CBEQN:
        cb = lambda f: -2.0*np.log10(rr/3.7 + 2.51/(Re*np.sqrt(abs(f)))) - 1/np.sqrt(abs(f))
        result = fsolve(cb, 0.02, maxfev=2000)
        return result[0]

    else:
        return 64/Re


def plotMoody(plotPoint=False, pt=(0, 0)):

    ReValsCB = np.logspace(np.log10(4000.0), np.log10(1.0E8), 100)
    ReValsL = np.logspace(np.log10(600.0), np.log10(2000.0), 20)
    ReValsTrans = np.logspace(np.log10(2000.0), np.log10(4000.0), 20)

    rrVals = np.array([0,1E-6,5E-6,1E-5,5E-5,1E-4,2E-4,4E-4,6E-4,8E-4,
                       1E-3,2E-3,4E-3,6E-3,8E-3,1.5E-2,2E-2,3E-2,4E-2,5E-2])

    ffLam = np.array([ff(Re,0) for Re in ReValsL])
    ffTrans = np.array([ff(Re,0) for Re in ReValsTrans])

    ffCB = np.array([[ff(Re,relRough,CBEQN=True) for Re in ReValsCB]
                     for relRough in rrVals])

    plt.figure(figsize=(14,8))

    plt.loglog(ReValsL,ffLam,'b-',linewidth=2,label='Laminar')
    plt.loglog(ReValsTrans,ffTrans,'b--',linewidth=2,label='Transition')

    for nRelR in range(len(ffCB)):

        plt.loglog(ReValsCB,ffCB[nRelR],color='k')

        plt.annotate(
            xy=(ReValsCB[-1],ffCB[nRelR][-1]),
            text='{:.2e}'.format(rrVals[nRelR]),
            fontsize=7,
            va='center'
        )

    plt.xlim(600,1E8)
    plt.ylim(0.008,0.10)

    plt.xlabel(r"Reynolds number $Re$",fontsize=16)
    plt.ylabel(r"Friction factor $f$",fontsize=16)
    plt.title("Moody Diagram",fontsize=18)

    plt.text(2.5E8,0.02,r"Relative roughness $\frac{\epsilon}{d}$",
             rotation=90,fontsize=12,clip_on=False)

    ax = plt.gca()

    ax.tick_params(axis='both',which='both',direction='in',top=True,right=True,labelsize=12)
    ax.tick_params(axis='both',grid_linewidth=1,grid_linestyle='solid',grid_alpha=0.5)

    ax.tick_params(axis='y',which='minor')
    ax.yaxis.set_minor_formatter(FormatStrFormatter("%.3f"))

    plt.grid(which='both')

    if plotPoint:
        Re_pt,f_pt = pt

        if 2000 < Re_pt < 4000:
            marker = '^'
        else:
            marker = 'o'

        plt.plot(Re_pt,f_pt,marker,markersize=12,
                 markeredgecolor='red',markerfacecolor='none')

    plt.tight_layout()
    plt.show()


def main():
    plotMoody()
# endregion


# region function calls
if __name__ == "__main__":
    main()
# endregion
