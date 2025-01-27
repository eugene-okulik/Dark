def arithmetic_mean(num_a: float, num_b: float) -> float:
    return (num_a + num_b) / 2


def geometric_mean(num_a: float, num_b: float) -> float:
    return (num_a * num_b) ** 0.5


if __name__ == "__main__":
    print(arithmetic_mean(4, 16))  # 10.0
    print(geometric_mean(4, 16))  # 8.0
