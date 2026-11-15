import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple frequency bands and phase shifts
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(12 * x[i]) * np.cos(8 * x[i]) + 
                       0.7 * np.sin(18 * x[i]) * np.cos(11 * x[i]) + 
                       0.3 * np.sin(25 * x[i]))
        
        # Higher-order polynomial potential with mixed coefficients
        polynomial = 0
        for i in range(self.dim):
            polynomial += 0.05 * x[i]**5 + 0.2 * x[i]**4 - 0.15 * x[i]**3 + 0.1 * x[i]**2 - 0.05 * x[i]
        
        # Adaptive cross-dimensional interaction with trigonometric coupling
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += (np.sin(3 * (x[i] - x[i+1])) * np.cos(2 * (x[i] + x[i+1])) + 
                                0.5 * np.exp(-0.05 * (x[i] - x[i+1])**2) * (x[i]**2 + x[i+1]**2))
        
        # Dynamic scaling factor with multi-scale modulation
        scaling = 1.5 + 0.5 * np.sin(0.3 * np.sum(x**2)) * np.cos(0.7 * np.sum(x**2))
        
        # Combine all components with additional noise-like perturbation
        noise = 0.01 * np.sum(np.sin(50 * x))
        
        return scaling * (chaotic + polynomial + cross_interaction) + noise