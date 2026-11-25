import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with chaotic modulation and multiple scales
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * np.sin(15.0 * r) * np.exp(-0.05 * r) + \
                      0.05 * r * np.cos(7.0 * r) * np.exp(-0.1 * r)
        
        # Multi-scale nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            amp = 1.5 / (i + 1)**1.5
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * \
                          np.sin(0.5 * freq * x[i]**2)
        
        # Adaptive cross-dimensional coupling with variable interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_strength = 0.5 + 0.5 * np.sin(0.1 * (i + j))
                coupling_term += interaction_strength * np.sin(x[i] * x[j]) * \
                                np.exp(-0.02 * (x[i]**2 + x[j]**2)) * \
                                np.cos(0.2 * x[i] * x[j])
        
        # Polynomial and exponential components with additional chaotic interactions
        poly_term = np.sum(x**4) * np.cos(0.3 * r) + 0.5 * np.sum(x**2)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.sin(0.15 * r) + \
                   np.sum(np.sin(x)**2) * np.cos(0.2 * r)
        
        # Additional chaotic modulation and noise component
        noise = 0.01 * np.sum(np.sin(20.0 * x) * np.cos(10.0 * x))
        
        # Final chaotic combination with enhanced nonlinearity
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + noise
        
        return result