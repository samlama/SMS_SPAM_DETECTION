def simplify_digit(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def generate_password(number, name):
    try:
        number = float(number)
        scientific_notation = "{:.9e}".format(number)
        mantissa, exponent = scientific_notation.split('e')
        simplified_mantissa = simplify_digit(int(''.join(filter(str.isdigit, mantissa))))
        simplified_exponent = simplify_digit(int(exponent))

        s1 = ''.join([word[:3] if word != 'e' else 'e' for word in str(simplified_mantissa)])
        s2 = ''.join([name[i - 1] for i in range(1, len(name) + 1) if i % 2 == simplified_exponent % 2])

        return f"{s1}@{s2}"
    except ValueError:
        return "Invalid input"

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        number, name = input().split()
        password = generate_password(number, name)
        print(password)