import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Spherical component with adaptive conditioning
        spherical = np.sum(x_scaled**2)
        
        # Sinusoidal modulations with varying frequencies
        sinusoidal = np.sum(np.sin(10 * x_scaled) * np.cos(5 * x_scaled))
        
        # Gaussian mixture with multiple centers
        gaussian_mixture = 0
        centers = np.linspace(-0.8, 0.8, 5)
        for center in centers:
            gaussian_mixture += np.exp(-5 * np.sum((x_scaled - center)**2))
        
        # Cross-dimensional interactions with radial dependence
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x_scaled[i] * x_scaled[j] * 
                                   np.sin(8 * np.pi * (x_scaled[i] + x_scaled[j])) * 
                                   np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2)))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1 + 0.1 * self.dim
        
        # Combine all components
        return condition_factor * (0.5 * spherical + 0.3 * sinusoidal + 
                                 0.1 * gaussian_mixture + 0.1 * cross_interaction)