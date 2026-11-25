import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.15 * r * np.sin(15.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with chaotic frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.sin(0.5 * i)
            amp = 1.5 / ((i + 1) ** 1.2)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Enhanced cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.7 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2)) * np.cos(0.2 * (i - j))
        
        # Polynomial and exponential components with adaptive weights
        poly_term = np.sum(x**4) * np.cos(0.6 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Additional chaotic modulation with dimensional adaptation
        dim_weight = np.sum(np.sin(np.arange(1, self.dim + 1) * 0.7))
        adaptive_term = 0.3 * np.sin(r * dim_weight) * np.cos(0.4 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + adaptive_term
        
        return result