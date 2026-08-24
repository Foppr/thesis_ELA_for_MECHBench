import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with varying coefficients
        for i in range(self.dim):
            # Use a chaotic map for dynamic scaling
            chaotic_factor = 1.0 + 0.3 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            result += chaotic_factor * (x[i]**2 + 0.1 * x[i]**4 + 0.01 * x[i]**6)
            
        # Add cross-dimensional coupling with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.sin(2.5 * x[i] + 1.5 * x[j]) * np.cos(1.8 * x[i] - 1.2 * x[j])
                result += 0.05 * coupling * (x[i]**2 + x[j]**2)
                
        # Add saddle point structure
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.2 * x[i]**3 - 0.1 * x[i]**5
            
        # Combine with chaotic scaling
        scaling = 1.0 + 0.2 * np.sum(np.sin(4.0 * x)) + 0.1 * np.sum(np.cos(3.0 * x))
        result = result * scaling + 0.5 * saddle_term
        
        # Add noise-like perturbations to increase complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        result += noise
        
        return result