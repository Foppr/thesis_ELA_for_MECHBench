import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with fractal-like chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.cos(7.0 * r) * np.exp(-0.15 * r)
        
        # Nested sinusoidal components with dynamic frequencies and chaotic amplitudes
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.sin(0.5 * i)
            amp = 1.5 / ((i + 1) * np.cos(0.3 * i) + 1.0)
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Enhanced cross-dimensional coupling with fractal interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Polynomial and exponential components with chaotic scaling
        poly_term = np.sum(x**4) * np.sin(0.3 * r)
        exp_term = np.sum(np.exp(-0.3 * x**2)) * np.cos(0.15 * r)
        
        # Additional chaotic perturbation term
        perturbation = 0.0
        for i in range(self.dim):
            perturbation += np.sin(20.0 * x[i]) * np.cos(10.0 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Final chaotic combination with dynamic weighting
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + perturbation
        
        return result