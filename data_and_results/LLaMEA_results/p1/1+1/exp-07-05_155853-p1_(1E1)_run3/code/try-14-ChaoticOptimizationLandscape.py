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
            chaotic += (np.sin(12 * x[i]) * np.cos(8 * x[i]) + 
                       0.7 * np.sin(18 * x[i]) * np.cos(11 * x[i]) + 
                       0.3 * np.sin(25 * x[i]))
        
        # Enhanced polynomial potential with mixed degrees and nonlinear terms
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.12 * x[i]**4 + 0.35 * x[i]**3 - 0.25 * x[i]**2 + 
                          0.15 * x[i] + 0.05 * x[i]**5)
        
        # Enhanced cross-dimensional interaction with trigonometric and exponential terms
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += (np.exp(-0.15 * (x[i] - x[i+1])**2) * 
                                (x[i]**2 + x[i+1]**2 + 0.5 * np.sin(5 * x[i] * x[i+1])))
        
        # Additional cross-dimensional interaction with cubic terms
        cubic_interaction = 0
        for i in range(self.dim - 2):
            cubic_interaction += 0.3 * (x[i]**3 + x[i+1]**3 + x[i+2]**3) * np.exp(-0.05 * (x[i] + x[i+1] + x[i+2])**2)
        
        # Modified scaling factor with more complex sinusoidal modulation
        scaling = 1.5 + 0.5 * np.sin(0.3 * np.sum(x**2)) * np.cos(0.7 * np.sum(x))
        
        # Combine all components
        return scaling * (chaotic + polynomial + cross_interaction + cubic_interaction)