import numpy as np

L1=1
L2=1.5 * L1
theta = 40 * np.pi / 180

#initial guesses

L3 = 1.5
alpha = 30 * np.pi / 180
epsilon = 1
n = 0

while epsilon > 0.0001:
    g1 = L1 * np.cos(theta) + L2 * np.cos(alpha) - L3
    dg1dalpha = -L2 * np.sin(alpha)
    dg1dL3 = -1;

    g2 = L1 * np.sin(theta) - L2 * np.sin(alpha)
    dg2dalpha = -L2 * np.cos(alpha);
    dg2dL3 = 0

    J = np.array([[dg1dalpha, dg1dL3], [dg2dalpha, dg2dL3]])
    
    #print('J', J.shape,J.dtype)  # (2,2) floats
    
    s = np.array([[alpha], [L3]]) - J/np.array([[g1], [g2]])
    s = s[:,0]  # fudge to turn (2,2) array into a (2,) array

    epsilon_alpha = abs(s[0] - alpha)

    epsilon_L3 = abs(s[1] - L3)

    epsilon = max(epsilon_alpha.all, epsilon_L3.all)

    print('epsilon', epsilon)

    alpha = s[0]

    L3 = s[1]

    n = n + 1

print(n, alpha, L3)
