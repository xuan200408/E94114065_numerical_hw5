import math

def f(t, y):
    return 1 + (y / t) + (y / t) ** 2

def exact_solution(t):
    return t * math.tan(math.log(t))

t0 = 1.0
y0 = 0.0
h = 0.1
n_steps = int((2.0 - 1.0) / h)

results = []

t = t0
y = y0

for i in range(n_steps + 1):
    exact = exact_solution(t)
    error = abs(y - exact)
    results.append((round(t, 2), y, exact, error))

   
    y = y + h * f(t, y)
    t = t + h


print(f"{'t':>5} {'Euler y':>12} {'Exact y':>12} {'Error':>12}")
for t_val, y_euler, y_exact, err in results:
    print(f"{t_val:5.2f} {y_euler:12.6f} {y_exact:12.6f} {err:12.6f}")
