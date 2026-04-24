# -*- coding: utf-8 -*-
# Parte A — Pilas

# TODO 1: Validación de paréntesis con pila
def balanceado(exp):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    abiertos = set(pares.values())

    for ch in exp:
        if ch in abiertos:
            pila.append(ch)
        elif ch in pares:
            if not pila or pila.pop() != pares[ch]:
                return False
    return not pila

# TODO 2: Conversión de decimal a binario usando pila
def decimal_a_binario(n):
    if n == 0:
        return "0"
    pila = []
    num = abs(n)
    while num > 0:
        pila.append(num % 2)
        num //= 2

    signo = "-" if n < 0 else ""
    binario = "".join(str(pila.pop()) for _ in range(len(pila)))
    return signo + binario

if __name__ == "__main__":
    print("== Pilas ==")
    print("Paréntesis balanceados:")
    print(balanceado("(a+b)*[c-d]"))   # True
    print(balanceado("(a+b*[c-d]"))    # False
    print(balanceado("{[()]}"))        # True
    print(balanceado("([)]"))          # False

    print("\nDecimal a binario:")
    print(decimal_a_binario(13))   # 1101
    print(decimal_a_binario(0))    # 0
    print(decimal_a_binario(255))  # 11111111
