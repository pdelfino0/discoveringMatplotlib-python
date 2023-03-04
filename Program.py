import matplotlib.pyplot as plt

listx = [x for x in range(1, 10)]
listy = [x**2 for x in range(1, 10)]
listy2 = [x**3 for x in range(1, 10)]

plt.plot(listx, listy, 'r-', label="$x^2$")
plt.plot(listx, listy2, 'bo', label="$x^2$")

plt.title("$x^2$ e $x^3$")
plt.legend()

plt.show
