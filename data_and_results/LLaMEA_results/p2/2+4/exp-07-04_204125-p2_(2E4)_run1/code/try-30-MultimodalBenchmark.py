import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Exponential terms with chaotic coupling
        for i in range(self.dim):
            # Base exponential term
            result += np.exp(0.2 * x[i]**2) - 1.0
            
            # Sinusoidal modulation with varying frequency
            result += 0.3 * np.sin(2.5 * np.pi * x[i]) * np.cos(1.5 * np.pi * x[i])
            
            # Chaotic coupling between adjacent variables
            if i < self.dim - 1:
                result += 0.2 * np.exp(-0.2 * (x[i]**2 + x[i+1]**2)) * np.sin(3.0 * (x[i] - x[i+1]))
            
            # Saddle-point inducing terms
            result += 0.2 * x[i]**3 * np.cos(0.5 * x[i])
            
            # Higher-order polynomial with alternating signs
            result += 0.05 * (-1)**i * x[i]**6
        
        # Add inter-variable coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.05 * (i - j)**2) * np.sin(0.5 * (x[i] + x[j]))
                result += 0.1 * coupling
        
        # Add noise-like perturbations for non-convexity
        result += 0.02 * np.sum(np.abs(x)**1.5)
        
        return result