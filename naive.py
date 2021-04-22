import numpy as np
import matplotlib.pyplot as plt

# Set up the transition matrix
T = np.zeros((101, 101))
for i in range(1, 101):
    T[i-1, i:i+6] = 1/6


# Final squares near 100
land_on_100 = 1
if land_on_100:
    pr = 1/6
    for i in range (95,100):
        T[i,i] = pr
        pr += 1/6
else:
    T[95:100,100] += np.linspace(1/6, 5/6, 5)

print(T[95:101,95:101])
    

# The player starts at position 0.
v = np.zeros(101)
v[0] = 1

n, P = 0, []
cumulative_prob = 0
# Update the state vector v until the cumulative probability of winning
# is "effectively" 1
while cumulative_prob < 0.99999:
    n += 1
    v = v.dot(T)
    P.append(v[100])
    cumulative_prob += P[-1]
mode = np.argmax(P)+1
print('modal number of moves:', mode)

# Plot the probability of winning as a function of the number of moves
fig, ax = plt.subplots()
ax.plot(np.linspace(1, n, n), P, 'g', lw=2, alpha=0.6)
ax.set_xlim(15)
ax.set_xlabel('Number of moves')
ax.set_ylabel('Probability of winning')

plt.show()
