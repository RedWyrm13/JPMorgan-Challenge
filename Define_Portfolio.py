import numpy as np

# Generates random values for sigma and mu
#Sigma is the covarianc ematrix
# Mu is the return value for each investment
def generate_portfolio(n, isRandom = False):
    """
    n: Int to represent the size of the problem (How many nodes are in the graph?)
    isRandom: Bool If false, it will generate the same graph every time for the appropriate n value. It is set to false by default to easily compare between trials
    """
    if not isRandom:
        np.random.seed(42) 
    sigma = np.zeros([n,n])
    for ii in range(n):
        for jj in range(ii+1,n):
            r = np.random.random()
            sigma[ii][jj] = r
            sigma[jj][ii] = r

    mu = [np.random.random() * 10 for i in range(n)]
    # Return order: Mu, Sigma
    return np.array(mu), np.array(sigma)

