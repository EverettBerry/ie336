################################################################################
# Everett Berry (working with Jim Moss)                                        #
# IE 336 HW 6 Problems 3 & 4                                                   #
################################################################################
import matplotlib.pyplot as plt
import numpy as np

case1 = np.mat([[0.1, 0.2, 0.3, 0.4],
                [0.4, 0.3, 0.2, 0.1],
                [0.5, 0.1, 0.1, 0.3],
                [0.25, 0.25, 0.25, 0.25]])

case2 = np.mat([[0.1, 0.2, 0.3, 0.4],
                [0, 1, 0, 0],
                [0.5, 0.1, 0.1, 0.3],
                [0.25, 0.25, 0.25, 0.25]])

# Doesn't coverge
case3 = np.mat([[0, 0.5, 0, 0.5],
                [0.5, 0, 0.5, 0],
                [0, 0.4, 0, 0.6],
                [0.3, 0, 0.7, 0]])

# Symmetric matrix
case4_BONUS = np.mat([[0, 0, 0.2, 0.8],
                     [0.7, 0, 0, 0.3],
                     [0.3, 0, 0, 0.7],
                     [0.8, 0.2, 0, 0]])

# Kind of identity matrix
case5_BONUS = np.mat([[0.9, 0, 0, 0.1],
                     [0, 0.9, 0, 0.1],
                     [0, 0, 0.9, 0.1],
                     [0.1, 0, 0, 0.9]])

case6_PROBLEM4 = np.mat([
    [0.729, 0.081, 0.081, 0.081, 0.009, 0.009, 0.009, 0.001],
    [0.81, 0, 0.09, 0.09, 0, 0, 0.01, 0],
    [0.81, 0.09, 0, 0.09, 0, 0.01, 0, 0],
    [0.81, 0.09, 0.09, 0, 0.01, 0, 0, 0],
    [0, 0.9, 0, 0, 0, 0.1, 0, 0],
    [0, 0.9, 0, 0, 0.1, 0, 0, 0],
    [0, 0, 0.9, 0, 0.1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]])

cases = [case1, case2, case3, case4_BONUS, case5_BONUS, case6_PROBLEM4]


def trans_prob_simul():
    for idx, case in enumerate(cases):
        trans = []

        # Generate transition probability matrices
        for step in range(50):
            trans.append(case ** step)

        # Plot the terms of each matrix
        for term in range(16):
            to_plot = []
            for mat in trans:
                to_plot.append(mat.flat[term])
            plt.plot(to_plot)

        # Create plots and save
        plt.ylabel('Transition probabilities')
        plt.xlabel('Steps')
        plt.savefig('Case' + str(idx + 1) + '.png')
        plt.clf()


trans_prob_simul()
