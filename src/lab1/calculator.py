def calculate(a: float, b: float, operation: str) -> float:
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    raise ValueError("Неизвестная операция")


def main() -> None:
    a = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))

    result = calculate(a, b, operation)
    print("Результат:", result)


if __name__ == "__main__":
    main()
