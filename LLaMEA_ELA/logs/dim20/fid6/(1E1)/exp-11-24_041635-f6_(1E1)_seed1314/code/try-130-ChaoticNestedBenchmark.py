import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with modified chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.15 * r * np.sin(12.0 * r) * np.exp(-0.2 * r)
        
        # Modified nested sinusoidal components with increased frequency diversity
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1) + 0.5 * np.sin(i)
            amp = 1.5 / (i + 1) ** 1.2
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Enhanced cross-dimensional coupling with exponential decay
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.8 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(0.1 * (i - j))
        
        # Additional polynomial and exponential components with altered parameters
        poly_term = np.sum(x**4) * np.cos(0.3 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Add a chaotic perturbation term for increased complexity
        perturbation = 0.05 * np.sin(20.0 * r) * np.cos(15.0 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + perturbation
        
        return result