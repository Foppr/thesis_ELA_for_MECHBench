import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * np.sin(10.0 * r) * np.exp(-0.15 * r)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.5 * (i + 1)  # Slightly increased frequency
            amp = 1.0 / (i + 1)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Cross-dimensional coupling with modified weights and chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.7 * np.sin(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))  # Increased weight and modified decay
        
        # Additional polynomial and exponential components with cubic terms for complexity
        poly_term = np.sum(x**3) * np.cos(0.5 * r) + 0.1 * np.sum(x**4)  # Added quartic term
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.1 * r)
        
        # Final chaotic combination with modified scaling
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term
        
        return result