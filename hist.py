## Randomizing data, generating summary statistics, histogram

import numpy as np

mu = 80
sigma = 10

x = np.random.normal(mu, sigma, 100)

print("Random Normal Array Mean Centered"), x[:10]

print("mean", np.mean(x))

