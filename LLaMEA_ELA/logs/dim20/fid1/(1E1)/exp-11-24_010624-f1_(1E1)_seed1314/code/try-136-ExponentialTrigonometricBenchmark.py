import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for trigonometric components
        self.frequencies = np.array([1.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        # Precompute decay rates
        self.decay_rates = np.array([0.1 + 0.2 * np.cos(i * 0.6) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with sinusoidal modulation
        for i in range(self.dim):
            exp_term = np.exp(-self.decay_rates[i] * np.abs(x[i]))
            sin_mod = np.sin(self.frequencies[i] * x[i])
            result += exp_term * sin_mod**2
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.cos(self.frequencies[i] * x[i]) * np.sin(self.frequencies[j] * x[j])
                distance = np.abs(x[i] - x[j])
                result += 0.5 * coupling * np.exp(-0.1 * distance**2)
                
        # Add saddle-point regions with polynomial terms
        for i in range(self.dim):
            poly_term = x[i]**4 - 2 * x[i]**2 + 0.5 * x[i]
            result += 0.1 * poly_term
            
        # Add cross-dimensional interaction with modified harmonic potentials
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                interaction = np.sin(3 * diff) * np.cos(2 * diff)
                result += 0.05 * interaction * (x[i]**2 + x[j]**2)
                
        # Add global scaling with multiple periodic components
        sum_squares = np.sum(x**2)
        global_scale = 1.0 + 0.3 * np.sin(0.5 * sum_squares) * np.cos(0.3 * sum_squares)
        result *= global_scale
        
        # Add noise to increase irregularity
        noise = 0.02 * np.sum(np.sin(x * 7) * np.cos(x * 11))
        result += noise
        
        # Add a term that creates multiple local minima with varying basins
        for i in range(self.dim):
            result += 0.03 * (x[i]**6 - 3 * x[i]**4 + 2 * x[i]**2)
            
        return result