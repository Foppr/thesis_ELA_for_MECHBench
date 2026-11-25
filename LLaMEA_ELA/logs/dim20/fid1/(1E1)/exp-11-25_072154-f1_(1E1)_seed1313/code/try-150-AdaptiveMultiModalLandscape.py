import numpy as np

class AdaptiveMultiModalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with periodic basis functions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sum(np.exp(-0.5 * (x_scaled**2)) * np.cos(2 * np.pi * x_scaled) + 
                       0.5 * np.exp(-0.3 * (x_scaled**2)) * np.sin(3 * np.pi * x_scaled))
        
        # Multi-modal periodic structure with varying frequencies
        modal = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled) + 
                      0.7 * np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) + 
                      0.3 * np.sin(20 * np.pi * x_scaled) * np.cos(18 * np.pi * x_scaled))
        
        # Adaptive coupling terms that scale with dimensionality
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (i + 1) * np.sin(np.pi * (x_scaled[i] - x_scaled[i+1])) * np.cos(2 * np.pi * (x_scaled[i] + x_scaled[i+1]))
        
        # Dimensionality-dependent fractal-like structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin((i + 1) * np.pi * x_scaled[i]) * np.cos((i + 1) * np.pi * x_scaled[i] / 2)
        
        # Adaptive radial scaling based on dimensionality
        adaptive_radial = np.sum(np.exp(-0.2 * (r + 0.5)**2) * np.sin(5 * r) + 
                               0.3 * np.exp(-0.1 * (r + 0.3)**3) * np.cos(4 * r))
        
        # Cross-dimensional interaction with varying weights
        cross_interaction = 0.0
        for i in range(self.dim - 2):
            cross_interaction += (i + 1) * np.sin(np.pi * x_scaled[i]) * np.cos(np.pi * x_scaled[i+1]) * np.sin(np.pi * x_scaled[i+2])
        
        # Multi-scale oscillatory component
        multi_scale = np.sum(np.sin(7 * np.pi * x_scaled**0.5) * np.cos(6 * np.pi * x_scaled**0.5) + 
                           0.4 * np.sin(11 * np.pi * x_scaled**0.3) * np.cos(10 * np.pi * x_scaled**0.3))
        
        # Boundary-sensitive component
        boundary = np.sum(np.exp(-2 * (x_scaled - 1)**2) + np.exp(-2 * (x_scaled + 1)**2))
        
        # Combined function with adaptive weights
        return (0.3 * radial + 0.25 * modal + 0.2 * coupling + 0.15 * fractal + 
                0.1 * adaptive_radial + 0.08 * cross_interaction + 0.05 * multi_scale + 0.07 * boundary)