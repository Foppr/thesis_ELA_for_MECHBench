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
            freq = 2.0 * (i + 1)
            amp = 1.0 / (i + 1)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Cross-dimensional coupling with altered interaction weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.7 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Additional polynomial and exponential components with modified parameters
        poly_term = np.sum(x**3) * np.cos(0.6 * r) + 0.5 * np.sum(x**4)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term
        
        return result