from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_numb) -> str:
    """Проверяет соответсвие ОДЗ."""
    if your_numb <= 0:
        return print('Недопустимое значение')
    result = calculate_square_root(your_numb)
    print(
        f'Мы вычислили квадратный корень из введённого '
        f'вами числа. Это будет: '
        f'{result}')


calc(25.5)
