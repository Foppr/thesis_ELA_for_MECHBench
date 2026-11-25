import numpy as np

class StructuredMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with periodic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (1 + 0.5 * np.sin(3 * r) + 0.3 * np.cos(5 * r)) * np.exp(-0.5 * r**2)
        
        # Sine-cosine periodic patterns with varying frequencies
        periodic = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                         0.7 * np.sin(4 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) + 
                         0.4 * np.sin(8 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled))
        
        # Cross-dimensional interference terms
        interference = 0.5 * np.sum(np.sin(np.pi * (x_scaled[:-1] + x_scaled[1:])) * 
                                  np.cos(np.pi * (x_scaled[:-1] - x_scaled[1:])))
        
        # Multi-scale harmonic components
        harmonics = 0.3 * np.sum(np.sin(10 * np.pi * x_scaled**2) + 
                               0.2 * np.sin(15 * np.pi * x_scaled**1.5) + 
                               0.1 * np.sin(20 * np.pi * x_scaled**1.2))
        
        # Quadratic penalty for distance from origin
        quadratic = 0.4 * r**2
        
        # Add a global minimum at the origin with additional structure
        global_min = 0.1 * np.exp(-r**2) * np.sin(2 * np.pi * r)**2
        
        # Combine all components
        return radial + periodic + interference + harmonics + quadratic + global_min