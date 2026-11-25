import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.15 * r * np.sin(12.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.5 * (i + 1)
            amp = 1.5 / (i + 1)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6)
        
        # Cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.6 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Polynomial and exponential components for additional complexity
        poly_term = np.sum(x**4) * np.cos(0.6 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term
        
        return result