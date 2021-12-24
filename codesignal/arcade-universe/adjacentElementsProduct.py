'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

'''


def solution(inputArray):
    produto = -10000000

    for numero in range(len(inputArray) - 1):
        resultado = inputArray[numero] * inputArray[numero + 1]
        if resultado > produto:
            produto = resultado

    return produto