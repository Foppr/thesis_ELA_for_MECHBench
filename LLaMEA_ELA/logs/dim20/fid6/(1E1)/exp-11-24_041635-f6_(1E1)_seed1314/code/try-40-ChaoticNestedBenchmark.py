import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r * np.exp(-0.2 * r) * np.sin(15.0 * r)
        
        # Nested sinusoidal components with exponentially increasing frequencies
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 ** (i + 1)
            amp = 1.0 / (i + 1)**2
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Cross-dimensional coupling with exponential interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j] * 0.5)
        
        # Polynomial and hyperbolic components for additional complexity
        poly_term = np.sum(x**4) * np.tanh(0.3 * r)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.cos(0.2 * r)
        
        # Central repulsion force to create narrow valleys
        center_repulsion = 10.0 * np.exp(-0.5 * r**2) * np.sin(2.0 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + center_repulsion
        
        return result