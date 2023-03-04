import matplotlib.pyplot as plt

import random


random.seed(42)

anos = [a for a in range(1990, 2010)]
valores = [random.randint(100,1500) for v in range(len(anos))]

plt.bar(anos, valores)
plt.xticks(range(1990,2010,2))
plt.show()

