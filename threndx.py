import numpy as np

def fourier_series(x, n, T):
    """Recursively compute n-term Fourier series approximation of f(x)"""
    if n == 0:
        return 0  # Base case
    return (1/n) * np.sin(2 * np.pi * n * x / T) + fourier_series(x, n-1, T)  # Recursive call

x = np.linspace(0, 2*np.pi, 1000)
y = [fourier_series(val, 10, 2*np.pi) for val in x]  # Compute with 10 terms
