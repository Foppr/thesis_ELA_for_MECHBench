import numpy as np

class RuggedAsymmetricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Asymmetric Gaussian peaks with varying heights and widths
        gaussian = 0.0
        for i in range(1, 6):
            center = np.full(self.dim, i * 0.8)
            # Asymmetric scaling based on sign of coordinate
            sigma = 1.0 + 0.5 * np.sign(x)  # Varying width based on sign
            gaussian += 2.0 * np.exp(-0.5 * np.sum(((x - center) / sigma)**2)) * np.sin(2 * np.pi * np.sum(x - center))
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) * (1 + 0.1 * x[i]**2)
            
        # Dynamic conditioning based on coordinate values
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1 + 0.5 * np.abs(x[i])) * x[i]**2
            
        # Cross-term interactions with trigonometric functions
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Ruggedness through high-frequency oscillations
        rugged = 0.0
        for i in range(self.dim):
            rugged += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Add a global quadratic term to control overall shape
        quadratic = 0.1 * np.sum(x**2)
        
        # Combine all components with different weights
        return gaussian + 0.5 * periodic + 0.3 * conditioning + 0.4 * cross + rugged + quadratic