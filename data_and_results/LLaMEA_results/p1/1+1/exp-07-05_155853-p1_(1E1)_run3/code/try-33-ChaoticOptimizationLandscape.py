import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple sine/cosine combinations
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(12 * x[i]) * np.cos(9 * x[i]) + 
                       0.7 * np.sin(18 * x[i]) * np.cos(11 * x[i]) + 
                       0.3 * np.sin(25 * x[i]))
        
        # Higher-order polynomial potential with mixed coefficients
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.15 * x[i]**5 + 0.25 * x[i]**4 - 0.15 * x[i]**3 + 
                          0.05 * x[i]**2 - 0.1 * x[i])
        
        # Adaptive cross-dimensional interaction with Gaussian-like decay
        cross_interaction = 0
        for i in range(self.dim - 1):
            distance = (x[i] - x[i+1])**2
            cross_interaction += np.exp(-0.05 * distance) * (x[i]**3 + x[i+1]**3 + 
                                                           0.5 * x[i] * x[i+1])
        
        # Dynamic scaling factor based on global landscape characteristics
        global_scale = 1.5 + 0.5 * np.sin(0.3 * np.sum(x**2)) * np.cos(0.2 * np.sum(x**3))
        
        # Add a small noise term to increase ruggedness
        noise = 0.01 * np.sum(np.sin(50 * x))
        
        # Combine all components
        return global_scale * (chaotic + polynomial + cross_interaction) + noise