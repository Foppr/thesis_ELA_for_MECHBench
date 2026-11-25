import numpy as np

class DeceptiveSmoothLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with periodic basis functions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sum(np.exp(-5 * (x_scaled - np.sin(r))**2) + 
                       0.5 * np.exp(-3 * (x_scaled - np.cos(r))**2))
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin(2 * np.pi * (x_scaled[i] + x_scaled[j])) * \
                               np.cos(3 * np.pi * (x_scaled[i] - x_scaled[j]))
        
        # Adaptive noise modulation based on position
        noise = 0.1 * np.random.rand() * (1 + 0.5 * np.sin(10 * r))
        
        # Multi-scale periodic structure with varying frequencies
        periodic = np.sum(np.sin(10 * x_scaled) * np.cos(7 * x_scaled) + 
                         0.3 * np.sin(20 * x_scaled) * np.cos(15 * x_scaled) + 
                         0.1 * np.sin(30 * x_scaled) * np.cos(25 * x_scaled))
        
        # Adaptive plateau region with controlled gradient
        plateau = 0.5 * np.sum(np.abs(x_scaled) < 0.2) * (1 - np.exp(-r**2))
        
        # Combine components with optimized weights
        return 0.4 * radial + 0.3 * interference + 0.2 * periodic + 0.08 * plateau + noise