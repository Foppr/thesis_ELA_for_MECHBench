import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * np.sin(10.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.5 * (i + 1)  # Slightly increased frequency
            amp = 1.2 / (i + 1)   # Slight amplitude increase
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Cross-dimensional coupling with stronger chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.7 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))  # Increased coupling strength and modified decay
        
        # Polynomial and exponential components for additional complexity
        poly_term = np.sum(x**4) * np.cos(0.6 * r)  # Changed to x^4 for higher nonlinearity
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.15 * r)  # Modified exponential and sinusoidal parameters
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term
        
        return result