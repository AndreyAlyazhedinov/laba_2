"""Вывод таблицы умножения."""


def multiplication_table(n=9):
    for i in range(1, n + 1):
        row = " ".join(f"{i * j:3d}" for j in range(1, n + 1))
        print(row)


if __name__ == "__main__":
    multiplication_table()
