"""Построение графика функции y = x^2."""
import matplotlib.pyplot as plt


def plot_square():
    x = list(range(-10, 11))
    y = [value ** 2 for value in x]

    plt.plot(x, y, marker="o")
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig("plot_y_x2.png")
    plt.show()


if __name__ == "__main__":
    plot_square()
