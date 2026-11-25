import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial penalty terms with different exponents
        poly_penalty = np.sum((x_scaled**2 + 0.1 * x_scaled**4 + 0.01 * x_scaled**6))
        
        # Sinusoidal wave components with varying frequencies
        sin_wave = np.sum(np.sin(2 * np.pi * x_scaled) + 0.5 * np.sin(5 * np.pi * x_scaled) + 
                         0.3 * np.sin(8 * np.pi * x_scaled))
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2) * np.cos(3 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # Radial sinusoidal component
        r = np.sqrt(np.sum(x_scaled**2))
        radial_sin = np.sin(10 * r) * np.exp(-0.5 * r**2)
        
        # Combine all components with different weights
        return 0.3 * poly_penalty + 0.4 * sin_wave + 0.2 * cross_interaction + 0.1 * radial_sin