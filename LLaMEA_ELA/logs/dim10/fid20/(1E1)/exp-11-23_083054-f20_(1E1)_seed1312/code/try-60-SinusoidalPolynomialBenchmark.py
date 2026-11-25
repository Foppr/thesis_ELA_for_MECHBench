import numpy as np

class SinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal frequencies and polynomial coefficients
        self.frequencies = np.linspace(1, 10, dim)
        self.poly_coeffs = np.random.uniform(-1, 1, dim)
        self.conditioning = np.random.uniform(0.1, 10, dim)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Sinusoidal oscillation component
        f1 = 0.0
        for i in range(self.dim):
            f1 += np.sin(self.frequencies[i] * x_norm[i]) * np.cos(self.frequencies[i] * x_norm[i])
        
        # Polynomial chaos expansion component
        f2 = 0.0
        for i in range(self.dim):
            f2 += self.poly_coeffs[i] * (x_norm[i] ** (i + 1))
        
        # Adaptive conditioning component
        f3 = 0.0
        for i in range(self.dim):
            f3 += self.conditioning[i] * x_norm[i] ** 2
        
        # Cross-dimensional interaction with varying coupling strengths
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                f4 += coupling * x_norm[i] * x_norm[j]
        
        # Nonlinear transformation with dynamic scaling
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.tanh(x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Combine all components with dynamic weights
        weights = np.abs(np.sin(np.arange(self.dim) * 0.7)) + 0.5
        weights = weights / np.sum(weights)
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4 + weights[4] * f5