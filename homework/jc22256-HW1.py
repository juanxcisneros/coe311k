#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import matplotlib.pyplot as plt
import numpy as np
def monte_carlo_pi(n):
    inside = 0
    i = 0

    while i < n:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1
        i += 1

    return 4 * inside / n
pi_true = math.pi
samples = range(10, 1001, 20)
errors = []

for n in samples:
    pi_est = monte_carlo_pi(n)
    errors.append(abs(pi_est - pi_true))


# In[7]:


plt.plot(list(samples), errors)
plt.xlabel("Number of samples")
plt.ylabel("Absolute error")
plt.title("Error")
plt.show()


# In[ ]:




