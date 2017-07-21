#!/usr/bin/env python3

from datetime import date
import math
import numpy as np
import sys

today = date(2015, 11, 20)
expiry = date(2017, 1, 20)

#Global inputs
s = 138.65
k = 133
t = (expiry - today).days / 365
r = 0.0106161830925
sig = 0.22545538993
div = .027000

def tree(steps, flavor):
    Dt = t / steps
    r_Dt = r * Dt
    exp_r_Dt = math.exp(r_Dt)
    exp_neg_r_Dt = math.exp(-r_Dt)
    exp_div_Dt = math.exp(div * Dt)
    exp_neg_div_Dt = math.exp(-div * Dt)
    sig_sqrt_Dt = sig * math.sqrt(Dt)
    exp_sig_sqrt_Dt = math.exp(sig_sqrt_Dt)

    u = exp_sig_sqrt_Dt
    d = 1/u
    q = (exp_r_Dt * exp_neg_div_Dt - d) / (u -d)
    p = 1 - q

    sv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    sv[0,0] = s
    z1 = 0 
    for i in range(1,steps + 1, 1):
        z1 = z1 + 1
        for n in range(z1 + 1):
            sv[n,i] = sv[0,0] * (u ** (i - n)) * (d ** n)

    iv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    z2 = 0
    for i in range(1,steps + 1, 1):
        find = False
        for n in range(z2 + 2):
            if flavor == "C":
                iv[n,i] = max(sv[n,i] - k, 0)
            elif flavor == "P":
                iv[n,i] = max(-1 * (sv[n,i] - k), 0)
            else:
                print("fravor has to be 'C' for call and 'P' for put")
                find = True
                break
        if find:
            break
        z2 = z2 + 1

#    print(iv)
    
    pv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    pv[:, steps] = iv[:, steps]
    z3 = steps + 1
    for i in range(steps -1, -1, -1):
        z3 = z3 - 1
        for n in range(z3):
            pv[n,i] = (q * pv[n, i + 1] + p * pv[n + 1, i + 1]) * exp_neg_r_Dt
    return(pv[0,0])

if __name__ == "__main__":
    steps = int(sys.argv[1])
    flavor = (sys.argv[2])    
    print(tree(steps,flavor))  







