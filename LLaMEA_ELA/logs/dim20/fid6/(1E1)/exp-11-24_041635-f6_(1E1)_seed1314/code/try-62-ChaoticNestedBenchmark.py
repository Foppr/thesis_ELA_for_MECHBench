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
        
        # Enhanced nested sinusoidal components with varying frequencies and amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            amp = 1.0 / (i + 1)**1.5
            nested_sum += amp * np.sin(freq * x[i]) * np.tanh(freq * x[i] * 0.5)
        
        # Cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.5 * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
        
        # Polynomial and exponential components for additional complexity
        poly_term = np.sum(x**4) * np.cos(0.5 * r)
        exp_term = np.sum(np.exp(-0.4 * x**2)) * np.sin(0.1 * r)
        
        # Additional hyperbolic tangent component for increased nonlinearity
        tanh_term = np.sum(np.tanh(x)) * np.exp(-0.1 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + tanh_term
        
        return result