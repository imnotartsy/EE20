# Iterative solution to the generic single-diode problem
# Provide the solution (VD) as the Thevenin voltage ranges
# from 1 volt to 100 volts for 4 decimal points of accuracy.

import numpy as np
import matplotlib.pyplot as plt


### Variables ###
plot = True
verbose = False

Vt  = .025 # V
Rth = 1000 # ohms
iS  = .00000000000001 # (10e-14) A

deci_accuracy = 4

Voltages = []

## Finding Voltages 1 to 100 ##
for Vth in range(1, 100):
    print("Vth:", Vth, end=" V ")

    VD = 0
    VD_old = 1

    ## Incremental solution to X decimal points
    while(round(VD, deci_accuracy) != round(VD_old, deci_accuracy)):
        VD_old = VD
        iD = (Vth - VD)/Rth
        if verbose:
            print("\t\tiD = {:.6f} A = (".format(iD), Vth, "-", VD, ")/", Rth,)

        log = np.log(iD/iS + 1)
        VD = Vt * log

        if verbose:
            print("\t\tVD = {:.6f} V =".format(VD), Vt, "* ln(", iD, "/", iS, "+ 1")
    Voltages.append(round(VD, 4))
    print("\tiD: {:.4f} \t VD: {:.4f}".format(iD, VD))


if plot:
    plt.plot(Voltages)
    plt.title('Vd vs Vth')
    plt.ylabel('Vd')
    plt.xlabel('Vth')
    plt.show()
    
