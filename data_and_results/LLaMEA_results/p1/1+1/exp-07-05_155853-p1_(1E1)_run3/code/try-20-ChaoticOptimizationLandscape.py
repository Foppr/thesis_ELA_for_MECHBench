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
            chaotic += 0.8 * np.sin(12 * x[i]) * np.cos(8 * x[i]) + 0.3 * np.sin(18 * x[i])
        
        # Polynomial potential component with mixed degrees (slightly modified)
        polynomial = 0
        for i in range(self.dim):
            polynomial += 0.15 * x[i]**5 + 0.25 * x[i]**3 - 0.15 * x[i]**2 + 0.05 * x[i]
        
        # Cross-dimensional interaction terms with different exponential decay
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += np.exp(-0.2 * (x[i] - x[i+1])**2) * (x[i]**3 + x[i+1]**3)
        
        # Add a global scaling factor to control the landscape difficulty
        scaling = 1.0 + 0.3 * np.sin(0.3 * np.sum(x**2))
        
        # Combine all components
        return scaling * (chaotic + polynomial + cross_interaction)