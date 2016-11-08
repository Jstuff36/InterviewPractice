from fractions import Fraction

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
    Guass_Matrix = []
    for i in range(len(pegs_coef)):
        Guass_Matrix.append(radius_coef[i] + pegs_coef[i])
    solution = Guass_Elimination(Guass_Matrix)
    if all(x > 0 for x in solution):
        return([round(solution[0]), 1])
        #return(Fraction(solution[0]).numerator, Fraction(solution[0]).denominator)
    else:
       return([-1, -1])

def Guass_Elimination(Matrix_coef):
    #eliminate columns
    for col in range(len(Matrix_coef[0])):
        for row in range(col+1, len(Matrix_coef)):
            r = [(rowValue * (-(Matrix_coef[row][col] / Matrix_coef[col][col]))) for rowValue in Matrix_coef[col]]
            Matrix_coef[row] = [sum(pair) for pair in zip(Matrix_coef[row], r)]
    #now backsolve by substitution
    ans = []
    Matrix_coef.reverse() #makes it easier to backsolve
    for sol in range(len(Matrix_coef)):
            if sol == 0:
                ans.append(Matrix_coef[sol][-1] / Matrix_coef[sol][-2])
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*Matrix_coef[sol][-2-x])
                #the equation is now reduced to ax + b = c form
                #solve with (c - b) / a
                ans.append((Matrix_coef[sol][-1]-inner)/Matrix_coef[sol][-sol-2])
    ans.reverse()
    return ans
print(Fraction(4.5).denominator)
print(answer(pegs))
