import numpy as np

class HybridRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_component = np.exp(-0.1 * r) * np.cos(0.5 * r)
        
        # Exponential decay along each dimension
        exp_component = 0.0
        for i in range(self.dim):
            exp_component += np.exp(-0.2 * np.abs(x[i])) * np.sin(0.3 * x[i])
            
        # Non-linear correlation between dimensions
        corr_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Pairwise interaction with non-linear coupling
                corr_term = (x[i]**2) * np.sin(x[j]) + (x[j]**2) * np.cos(x[i])
                corr_component += corr_term
                
        # Saddle point structure with periodic modulation
        saddle_component = 0.0
        for i in range(self.dim):
            # Create saddle-like behavior with sinusoidal modulation
            saddle_term = x[i] * np.sin(0.4 * x[i]) * np.cos(0.6 * x[i])
            saddle_component += saddle_term
            
        # Add noise for additional complexity
        noise = 0.01 * np.random.normal(0, 1)
        
        # Combine components with adaptive weights
        weight1 = 0.25 + 0.1 * np.sin(self.dim * 0.2)
        weight2 = 0.35 + 0.15 * np.cos(self.dim * 0.15)
        weight3 = 0.2 + 0.1 * np.sin(self.dim * 0.1)
        weight4 = 0.2 + 0.05 * np.cos(self.dim * 0.25)
        
        return (weight1 * radial_component + 
                weight2 * exp_component + 
                weight3 * corr_component + 
                weight4 * saddle_component + 
                self.dim * 0.2 + noise)