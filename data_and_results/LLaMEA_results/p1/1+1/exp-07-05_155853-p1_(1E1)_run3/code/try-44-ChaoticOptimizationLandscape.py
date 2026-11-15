import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional Brownian motion inspired fractal noise component
        fbm = 0
        for i in range(self.dim):
            fbm += (0.5 * np.sin(20 * x[i]) * np.cos(15 * x[i]) + 
                   0.3 * np.sin(35 * x[i]) * np.cos(25 * x[i]) + 
                   0.2 * np.sin(50 * x[i]) * np.cos(40 * x[i]) +
                   0.1 * np.sin(70 * x[i]))
        
        # Multi-scale sinusoidal modulation with varying frequencies
        modulation = 0
        for i in range(self.dim):
            modulation += (0.8 * np.sin(2 * x[i]) * np.cos(3 * x[i]) + 
                          0.6 * np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                          0.4 * np.sin(10 * x[i]) * np.cos(13 * x[i]) + 
                          0.2 * np.sin(15 * x[i]) * np.cos(20 * x[i]))
        
        # Higher-order polynomial with non-convex terms and sharp minima
        polynomial = 0
        for i in range(self.dim):
            polynomial += (0.2 * x[i]**6 - 0.3 * x[i]**5 + 0.1 * x[i]**4 + 
                          0.05 * x[i]**3 - 0.15 * x[i]**2 + 0.08 * x[i])
        
        # Non-linear cross-dimensional coupling with exponential interaction
        cross_interaction = 0
        for i in range(self.dim - 1):
            distance = np.abs(x[i] - x[i+1])
            cross_interaction += np.exp(-0.1 * distance) * (x[i]**4 + x[i+1]**4 + 
                                                          0.3 * x[i]**2 * x[i+1]**2)
        
        # Multi-scale chaotic modulation with dynamic frequency adjustment
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(15 * x[i]) * np.cos(12 * x[i]) + 
                       0.6 * np.sin(25 * x[i]) * np.cos(20 * x[i]) + 
                       0.4 * np.sin(40 * x[i]) * np.cos(30 * x[i]) + 
                       0.2 * np.sin(60 * x[i]))
        
        # Dynamic scaling with multi-frequency sinusoidal modulation
        global_scale = 2.0 + 0.8 * np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**3)) + \
                      0.5 * np.sin(0.8 * np.sum(x**4))
        
        # Add fractal-like noise with multiple frequency bands
        noise = 0.02 * np.sum(np.sin(100 * x) + 0.5 * np.sin(200 * x) + 0.3 * np.sin(300 * x))
        
        # Combine all components with enhanced ruggedness
        return global_scale * (fbm + modulation + polynomial + cross_interaction + chaotic) + noise