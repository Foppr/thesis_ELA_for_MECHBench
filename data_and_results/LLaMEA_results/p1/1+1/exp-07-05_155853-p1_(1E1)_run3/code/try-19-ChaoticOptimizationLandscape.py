import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using sine and cosine functions with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.5 * np.sin(15 * x[i])
        
        # Polynomial potential component with mixed degrees
        polynomial = 0
        for i in range(self.dim):
            polynomial += 0.1 * x[i]**4 + 0.3 * x[i]**3 - 0.2 * x[i]**2 + 0.1 * x[i]
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += np.exp(-0.1 * (x[i] - x[i+1])**2) * (x[i]**2 + x[i+1]**2)
        
        # Add a global scaling factor to control the landscape difficulty
        scaling = 1.0 + 0.5 * np.sin(0.5 * np.sum(x**2))
        
        # Combine all components
        return scaling * (chaotic + polynomial + cross_interaction)