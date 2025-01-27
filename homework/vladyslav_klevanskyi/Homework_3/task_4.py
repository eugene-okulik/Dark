def hypotenuse_and_area(leg_a: float, leg_b: float) -> tuple:
    hypotenuse = (leg_a ** 2 + leg_b ** 2) ** 0.5
    area = leg_a * leg_b / 2
    return hypotenuse, area


if __name__ == "__main__":
    print(hypotenuse_and_area(5, 3))  # (5.83, 7.5)
