def euleMethod(f, w0, x0, x1, n):
    if(n==0): return w0
    h = (x1 - x0) / n
    w = w0
    x = x0
    for i in range(n):
        w = w + h * f(x, w)
        x = x + h
    return w

if __name__ == "__main__":
    def f(x, y):
        return x**2 + 0.5 * y**2
    print(euleMethod(f, 2, 1, 2, 0))