import numpy


def convert_to_powers_of_two(num):
    """
    returns with the list of power of two that make up the number
    """
    powers_of_two = []
    i = 0
    while not (num == 0):
        while 2 ** i < num:
            i += 1
        if num == 1:
            powers_of_two.append(0)
            break
        else:
            powers_of_two.append(i-1)
        num -= 2 ** (i-1)
        i = 0
    return powers_of_two


def modulo_of_powers_of_two(base, largest_power_of_two, modulo):
    """
    retunrs a list of modulos which are the base raised to the power of two
    raised to the power of 0, 1, 2, ..., largest_power_of_two
    """
    remainders = []
    for i in range(largest_power_of_two + 1):
        remainders.append((base ** (2 ** i)) % modulo)
    return remainders


def fast_pow(base, exponent, modulo):
    exponent_as_powers_of_two = convert_to_powers_of_two(exponent)
    list_of_modulos = modulo_of_powers_of_two(base, exponent_as_powers_of_two[0], modulo)
    product_of_modulos = 1
    for i in range(len(list_of_modulos)):
        if i in exponent_as_powers_of_two:
            product_of_modulos *= list_of_modulos[i]
    return product_of_modulos % modulo


def main():
    pass

if __name__ == '__main__':
    main()