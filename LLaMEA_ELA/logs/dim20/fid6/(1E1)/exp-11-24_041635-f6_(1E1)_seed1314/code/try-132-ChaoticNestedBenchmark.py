import numpy as np

class ChaoticNestedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with stronger chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.2 * r * np.sin(15.0 * r) * np.exp(-0.2 * r)
        
        # Modified nested sinusoidal components with increased frequency and amplitude variations
        nested_sum = 0.0
        for i in range(self.dim):
            freq = 3.0 * (i + 1)
            amp = 1.5 / (i + 1)**1.5
            nested_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Enhanced cross-dimensional coupling with stronger interaction terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.8 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * x[i] * x[j])
        
        # Additional polynomial and exponential components with higher order terms
        poly_term = np.sum(x**4) * np.cos(0.7 * r)
        exp_term = np.sum(np.exp(-0.5 * x**2)) * np.sin(0.15 * r)
        
        # Additional chaotic component with fractional powers for increased complexity
        frac_term = 0.3 * np.sum(np.abs(x)**1.7) * np.sin(0.2 * r)
        
        # Final chaotic combination
        result = radial_term + nested_sum + coupling_term + poly_term + exp_term + frac_term
        
        return result