import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with multiple sine/cosine combinations and additional frequency terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(15 * x[i]) * np.cos(10 * x[i]) + 
                       0.6 * np.sin(20 * x[i]) * np.cos(13 * x[i]) + 
                       0.4 * np.sin(28 * x[i]) + 
                       0.2 * np.cos(30 * x[i]))
        
        # Higher-order polynomial potential with mixed coefficients and added nonlinearity
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.2 * x[i]**6 + 0.3 * x[i]**5 - 0.2 * x[i]**4 + 
                          0.1 * x[i]**3 - 0.15 * x[i]**2 + 0.05 * x[i])
        
        # Adaptive cross-dimensional interaction with exponential and trigonometric decay
        cross_interaction = 0
        for i in range(self.dim - 1):
            distance = (x[i] - x[i+1])**2
            cross_interaction += (np.exp(-0.03 * distance) * (x[i]**4 + x[i+1]**4 + 
                                                           0.6 * x[i] * x[i+1] * np.sin(5 * (x[i] + x[i+1]))))
        
        # Dynamic scaling factor based on global landscape characteristics with more complex modulation
        global_scale = 1.2 + 0.8 * np.sin(0.4 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**3)) * np.exp(-0.1 * np.sum(np.abs(x)))
        
        # Add a small noise term to increase ruggedness and prevent convergence to trivial solutions
        noise = 0.02 * np.sum(np.sin(60 * x) * np.cos(40 * x))
        
        # Combine all components
        return global_scale * (chaotic + polynomial + cross_interaction) + noise