# https://www.pythonpool.com/python-binomial-coefficient/

def binomial(n, k):
    if 0 <= k <= n:
        a= 1
        b=1
        for t in range(1, min(k, n - k) + 1):
            a *= n
            b *= t
            n -= 1
        return a // b
    else:
        return 0
print(binomial(26,6))