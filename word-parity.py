# brute force
# time complexity O(n)

def parity(x: int):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


if __name__ == '__main__':
    word = input('Binary value: ')
    result = parity(int(word))
    print(result)
