import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with fractional power and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r**1.7 * np.sin(15.0 * r) * np.exp(-0.2 * r)
        
        # Nested sinusoidal components with chaotic frequency modulation and variable amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.sin(0.5 * i)
            amp = 1.5 / ((i + 1)**1.3)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Enhanced cross-dimensional coupling with chaotic interaction and variable weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 * np.sin(0.3 * (i + j)) * np.cos(0.2 * (i - j))
                coupling_term += weight * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Fractional polynomial and exponential components for additional complexity
        poly_term = np.sum(x**2.5) * np.cos(0.7 * r)
        exp_term = np.sum(np.exp(-0.3 * x**1.8)) * np.sin(0.15 * r)
        
        # Additional chaotic harmonic component
        harmonic_term = 0.1 * np.sum(np.sin(20.0 * x) * np.cos(10.0 * x))
        
        # Final chaotic combination with modified scaling
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + harmonic_term
        
        return result