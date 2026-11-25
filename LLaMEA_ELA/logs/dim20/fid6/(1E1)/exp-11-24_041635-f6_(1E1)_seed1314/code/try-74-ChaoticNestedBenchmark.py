import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with double chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.cos(8.0 * r) * np.exp(-0.2 * r)
        
        # Dynamic nested sinusoidal components with time-varying frequencies
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * (1.0 + 0.3 * np.sin(0.5 * r))
            amp = 1.5 / (i + 1) ** 1.5
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced cross-dimensional coupling with exponential interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(2.0 * x[i] * x[j])
                coupling_term += 0.8 * coupling_factor * (1.0 + 0.2 * np.sin(3.0 * r))
        
        # Polynomial and hyperbolic components for increased complexity
        poly_term = np.sum(x**4) * np.cos(0.3 * r) * np.exp(-0.1 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.2 * r) * np.cos(0.1 * r)
        
        # Additional chaotic harmonic component
        harmonic_term = 0.3 * np.sum(np.sin(5.0 * x) * np.cos(2.5 * x))
        
        # Final chaotic combination with dynamic weighting
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + harmonic_term
        
        return result