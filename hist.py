## Randomizing data, generating summary statistics, histogram

import numpy as np
import matplotlib.pyplot as plt

mu = 80
sigma = 10

x = np.random.normal(mu, sigma, 100)

print("Random Normal Array Mean Centered"), x[:10]

print("mean", np.mean(x))

plt.hist(x)
plt.show()

print("I am a champion on Science!")

## Adding standard deviation
print("Stand.dev", np.std(x))

I need to do more.
