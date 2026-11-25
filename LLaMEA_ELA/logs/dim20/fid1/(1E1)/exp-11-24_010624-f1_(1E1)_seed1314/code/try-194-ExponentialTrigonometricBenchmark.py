import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for trigonometric components
        self.frequencies = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Spherical component with exponential decay
        r_squared = np.sum(x**2)
        result += np.exp(-0.1 * r_squared) * (r_squared + 1e-8)
        
        # Add trigonometric terms with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(self.frequencies[i] * x[i])**2 + \
                      0.3 * np.cos(self.frequencies[i] * x[i])**2
        
        # Cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.05 * ((x[i] - x[j])**2 + (x[i] + x[j])**2))
                result += coupling * np.sin(x[i] * x[j]) * np.cos(0.5 * (i - j))
        
        # Add a modified Ackley-like component for increased multimodality
        sum_cos = np.sum(np.cos(2 * np.pi * x))
        result += -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / self.dim)) - \
                  np.exp(sum_cos / self.dim) + 20 + np.e
        
        # Add noise component
        noise = 0.01 * np.sum(np.sin(x * 5))
        result += noise
        
        # Add a periodic component with varying periods
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(3 * x[i]) * np.cos(4 * x[i])
        result += 0.02 * periodic
        
        # Add a new twist: incorporate a modified Griewank function component
        griewank_term = 0.0
        for i in range(self.dim):
            griewank_term += x[i]**2 / 4000 - np.cos(x[i] / np.sqrt(i+1)) + 1
        result += 0.015 * griewank_term
        
        return result