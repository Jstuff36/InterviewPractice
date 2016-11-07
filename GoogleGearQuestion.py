from array import *

pegs = [4, 30, 50]
def answer(pegs):
    radius_coef = [[0 for i in range(len(pegs))] for j in range(len(pegs))]
    radius_coef[0][0] = 1
    radius_coef[0][-1] = -2
    for i in range(0, len(pegs)-1):
    	radius_coef[i+1][i] = 1
    	radius_coef[i+1][i+1] = 1

    pegs_coef = [[0]]
    for i in range(len(pegs)-1):
        pegs_coef.append([pegs[i+1] - pegs[i]])
    
    radius = pegs_coef / radius_coef
    return(radius)

print(answer(pegs))