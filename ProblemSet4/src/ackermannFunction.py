import matplotlib.pyplot as plt


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


for m in range(4):
    values = [ackermann(m, n) for n in range(6)]
    plt.plot(range(6), values, label=f"m={m}")

plt.yscale("log")
plt.legend()
plt.xlabel("n")
plt.ylabel("A(m,n)")
plt.title("Ackermann visualization")
plt.savefig("ackermann.png")

if __name__ == "__main__":
    print("Ackermann function A(0, 5):", ackermann(0, 5))
    print("Ackermann function A(1, 2):", ackermann(1, 2))
    print("Ackermann function A(2, 2):", ackermann(2, 2))
    print("Ackermann function A(3, 3):", ackermann(3, 3))
