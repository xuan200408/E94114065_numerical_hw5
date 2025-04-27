import math

# 定義 f(t, y)
def f(t, y):
    return 1 + (y / t) + (y / t) ** 2

# 定義 f_t(t, y)
def f_t(t, y):
    fy = f(t, y)
    return (t * fy - y) / (t ** 2) + 2 * (y / t) * (t * fy - y) / (t ** 2)

def exact_solution(t):
    return t * math.tan(math.log(t))

t0 = 1.0
y0 = 0.0
h = 0.1
n_steps = int((2.0 - 1.0) / h)

### ------------------ Euler 方法 ------------------
print("\nEuler’s Method Results:")
t = t0
y = y0
print(f"{'t':>5} {'Euler y':>12} {'Exact y':>12} {'Error':>12}")
for i in range(n_steps + 1):
    exact = exact_solution(t)
    error = abs(y - exact)
    print(f"{t:5.2f} {y:12.6f} {exact:12.6f} {error:12.6f}")

    y = y + h * f(t, y)
    t = t + h

### ------------------ Taylor 方法 ------------------
print("\nTaylor’s Method (Order 2) Results:")
t = t0
y = y0
print(f"{'t':>5} {'Taylor y':>12} {'Exact y':>12} {'Error':>12}")
for i in range(n_steps + 1):
    exact = exact_solution(t)
    error = abs(y - exact)
    print(f"{t:5.2f} {y:12.6f} {exact:12.6f} {error:12.6f}")

    y = y + h * f(t, y) + (h**2 / 2) * f_t(t, y)
    t = t + h
