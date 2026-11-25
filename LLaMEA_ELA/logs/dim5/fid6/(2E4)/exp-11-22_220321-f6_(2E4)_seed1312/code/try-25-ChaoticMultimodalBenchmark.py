import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Logarithmic barrier terms to create steep gradients near boundaries
        for i in range(self.dim):
            result += 10.0 * (np.log(1.0 + np.abs(x[i])) + np.sin(x[i]) ** 2)
            
        # Asymmetric polynomial distortions with varying exponents
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(i)
            result += (x[i] ** exp_factor) * (i + 1) * 0.1
            
        # Trigonometric coupling between dimensions with phase shifts
        for i in range(self.dim):
            j = (i + 1) % self.dim
            phase_shift = np.pi * (i / self.dim)
            result += 2.0 * np.sin(x[i] * x[j] + phase_shift) * np.cos(x[i] - x[j])
            
        # Cross-dimensional interaction with chaotic sine modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(np.pi * x[i] * x[j]) * (i + j)
                result += 0.3 * interaction
                
        # Add a chaotic perturbation term using the logistic map-like behavior
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(10.0 * x[i] + np.cos(x[(i+1) % self.dim])) ** 2
            
        return result + 0.5 * chaos_term