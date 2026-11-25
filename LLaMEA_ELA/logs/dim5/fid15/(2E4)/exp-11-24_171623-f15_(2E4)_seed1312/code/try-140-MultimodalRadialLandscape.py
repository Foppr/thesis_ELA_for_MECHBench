import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with varying widths
        rb_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            dist = np.sum((x_norm - centers[i])**2)
            rb_sum += np.exp(-dist * (1 + 0.5 * np.sin(i * 3.14159))) * (1 + 0.3 * np.cos(i * 2.0))
        
        # Sinusoidal oscillations with adaptive frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x_norm[i] * 1.5)
            sin_sum += np.sin(x_norm[i] * freq) * np.cos(x_norm[i] * 0.5 * freq)
        
        # Cross-dimensional coupling with polynomial interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x_norm[i]**2 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j] * 4.0)
                cross_sum += coupling
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5)
        
        # Valley structure with exponential decay
        valley_sum = 0.0
        for i in range(self.dim):
            valley_sum += (x_norm[i]**2) * np.exp(-0.5 * x_norm[i]**2) * (1 + 0.2 * np.sin(x_norm[i] * 7.0))
        
        # Combine all components with dynamic weights
        result = 0.3 * rb_sum + 0.25 * sin_sum + 0.2 * cross_sum + 0.25 * valley_sum
        
        return result * cond_factor * (1 + 0.1 * np.sum(np.abs(x_norm)))