import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            amp = 1.0 / ((i + 1) ** 1.5)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Cross-dimensional coupling with enhanced chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.8 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Fractional polynomial and exponential components for additional complexity
        poly_term = np.sum(x**3.5) * np.cos(0.7 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Additional chaotic harmonic terms
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.3 * np.sin(20.0 * x[i]) * np.cos(10.0 * x[i])
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + harmonic_term
        
        return result