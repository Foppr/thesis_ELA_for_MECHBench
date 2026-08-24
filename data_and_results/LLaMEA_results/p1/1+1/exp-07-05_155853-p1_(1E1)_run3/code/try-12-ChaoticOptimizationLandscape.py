import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with higher frequency oscillations and amplitude modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(12 * x[i]) * np.cos(9 * x[i]) + 
                       0.7 * np.sin(20 * x[i]) * np.cos(13 * x[i]) + 
                       0.3 * np.sin(25 * x[i]))
        
        # Modified polynomial potential with higher degree terms and variable coefficients
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.15 * x[i]**5 + 0.25 * x[i]**4 - 0.15 * x[i]**3 + 
                          0.05 * x[i]**2 - 0.1 * x[i])
        
        # Novel cross-dimensional interaction with trigonometric coupling and adaptive weights
        cross_interaction = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[i+1]))
            cross_interaction += weight * np.sin(3 * (x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2)
        
        # Global scaling with dynamic modulation based on solution proximity to boundaries
        boundary_effect = np.sum(np.abs(x - np.sign(x) * 5.0))
        scaling = 1.0 + 0.3 * np.sin(0.7 * np.sum(x**2)) + 0.2 * np.exp(-0.05 * boundary_effect)
        
        # Combine all components with modified weighting
        return scaling * (1.2 * chaotic + 0.8 * polynomial + 1.5 * cross_interaction)