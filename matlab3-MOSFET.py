# Tool for visualizing the family of i-v curves for a MOSFET. The user
# enters the two MOSFET parameters (K, Vto) and then the progarm generates
# a plot of drain current ID vs. VDS for a range of VGS voltages.

import numpy as np
import matplotlib.pyplot as plt


### Variabvles ###
# program variables to dictact how the program runs
plot = True
takeInputs = True
verbose = False

VgsRange = 10
VdsRange = 10

# dictionary to hold all of the MOSFET Curves, labeled with their Vgs
V = {}



### Handling inputs
if takeInputs:
    print("Please enter a K value, the transconductance parameter, (mA/V^2): ",
                                                                        end="")
    try:
        K = float(input())
    except:
        print("\tERROR: K was an invalid number, please start again.")
        exit()

    print("Please enter your threshold voltage (V): ", end="")
    try:
        Vto = float(input())
    except:
        print("\tERROR: Vto was an invalid number, please start again.")
        exit()
else:
    print("Setting K to .05 mA/V^2 and Vto to 1 V")
    K = .5
    Vto = 1



### Compute curves

## find various curves with Vgs
for Vgs in range(0, VgsRange + 1):
    curve = []

    ## find curve for varied Vds
    for Vds in range(0, VdsRange + 1):
        
        ## triode region
        if Vgs >= Vto and Vds < Vgs - Vto:
            iD = K*(2*(Vgs - Vto)*Vds - pow(Vds, 2))
            
        ## saturation region
        else: # Vgs >= Vto and Vds >= Vgs - Vto:
            iD = K * pow((Vgs- Vto),2)

        # add iD to current Vgs curve
        curve.append(iD)

    # add Vgs curve to dictionary of curves
    V[str(Vgs)+"V"] = curve


### Plot graph
print("Showing plot . . .")
if plot:
    for curve in V:
        # plot each curve
        plt.plot(V[curve])

        # add Vgs labels
        plt.annotate(xy=[VdsRange, V[curve][-1]], text=curve) #fontsize=8

        if verbose: print(curve, V[curve])
    plt.title('MOSFET i-V Characteristic')
    plt.ylabel('id (mA)')
    plt.xlabel('Vds (V)')
    plt.show()