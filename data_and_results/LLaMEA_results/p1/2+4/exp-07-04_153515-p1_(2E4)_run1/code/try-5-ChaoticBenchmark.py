import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic exponential terms with varying decay rates
        for i in range(self.dim):
            # Exponentially decaying sinusoidal terms
            f_val += np.exp(-0.1 * i) * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Add saddle point structure using polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interactions to avoid overcomplication
                f_val += 0.01 * (x[i]**3 - 3*x[i]) * (x[j]**2 - 2)
                
        # Add a global scaling factor that makes the function increasingly complex with dimension
        f_val *= (1.0 + 0.1 * self.dim)
        
        # Add noise-like perturbations to increase complexity
        noise = 0.0
        for i in range(self.dim):
            noise += 0.005 * np.sin(10 * x[i]) * np.cos(7 * x[i])
        f_val += noise
        
        return f_val