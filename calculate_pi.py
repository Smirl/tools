def calculate_pi(decimal_places=5):
    # Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    pi = 0
    denominator = 1
    sign = 1
    tolerance = 0.5 * 10 ** -(decimal_places + 1)

    while True:
        term = sign / denominator
        pi += term
        if abs(term) < tolerance:
            break
        sign *= -1
        denominator += 2

    return round(pi * 4, decimal_places)


if __name__ == "__main__":
    result = calculate_pi(5)
    print(f"pi = {result:.5f}")
