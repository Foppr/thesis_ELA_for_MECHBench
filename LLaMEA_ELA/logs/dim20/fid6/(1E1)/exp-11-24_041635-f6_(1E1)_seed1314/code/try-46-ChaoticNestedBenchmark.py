import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with multiple chaotic frequencies
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * (np.sin(10.0 * r) + 0.5 * np.sin(20.0 * r)) * np.exp(-0.1 * r)
        
        # Multi-scale nested sinusoidal components with adaptive amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * np.sin(0.5 * i)
            amp = 1.0 / (i + 1) * np.cos(0.3 * i)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Adaptive cross-dimensional coupling with variable interaction strength
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.5 * np.sin(0.1 * (i + j))
                coupling_term += strength * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Polynomial and exponential components with chaotic modulation
        poly_term = np.sum(x**4) * np.cos(0.3 * r)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.2 * r)
        
        # Additional chaotic harmonic component
        harmonic_term = 0.05 * np.sum(np.sin(3.0 * x) * np.cos(1.5 * x))
        
        # Final chaotic combination with weighted components
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + harmonic_term
        
        return result