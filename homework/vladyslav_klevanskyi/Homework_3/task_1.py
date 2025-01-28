from typing import Union


def calculator(num_a: int, num_b: int, operation: str) -> Union[int, str]:
    if operation == "+":
        return num_a + num_b
    elif operation == "-":
        return num_a - num_b
    elif operation == "*":
        return num_a * num_b
    else:
        return "Error: Invalid operation"


if __name__ == "__main__":
    print("addition", calculator(10, 5, "+"))  # 15
    print("subtraction", calculator(10, 5, "-"))  # 5
    print("product", calculator(10, 5, "*"))  # 50
    print("error", calculator(10, 5, "/"))  # "Error: Invalid operation"
