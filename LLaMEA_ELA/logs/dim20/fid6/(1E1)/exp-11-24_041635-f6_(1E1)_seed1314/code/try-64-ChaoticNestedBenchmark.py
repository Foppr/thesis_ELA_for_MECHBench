import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r * np.sin(10.0 * r) * np.exp(-0.15 * r) * np.tanh(0.1 * r)
        
        # Enhanced nested sinusoidal components with varying frequencies, amplitudes, and phases
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 * (i + 1) + 0.5 * np.sin(0.3 * i)
            amp = 1.0 / (i + 1) * np.cos(0.2 * i)
            phase = 0.1 * i * np.sin(0.5 * i)
            nested_sum += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.5 + phase)
        
        # Enhanced cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.5 * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2)) * np.cos(0.1 * (x[i] + x[j]))
        
        # Additional polynomial and hyperbolic components for increased complexity
        poly_term = np.sum(x**4) * np.cos(0.5 * r) * np.sin(0.2 * r)
        tanh_term = np.sum(np.tanh(x)) * np.exp(-0.3 * r)
        
        # Final chaotic combination with additional exponential decay and scaling
        result = radial_term + nested_sum + coupling_term + poly_term + tanh_term
        
        return result