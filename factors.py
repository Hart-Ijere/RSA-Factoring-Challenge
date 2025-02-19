#!/usr/bin/python3
import sys

def factorize(number):
    factors = []
    for item in range(2, int(number**0.5) + 1):
        if number % item == 0:
            factors.append((item, number // item))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            numbers = file.read().splitlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    for num in numbers:
        num = int(num)
        factor_pairs = factorize(num)
        for pair in factor_pairs:
            print(f"{num}={pair[0]}*{pair[1]}")

