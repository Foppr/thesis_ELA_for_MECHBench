import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks
        radial = np.sum((x**2) * np.exp(-0.1 * x**2))
        
        # Sinusoidal oscillations with varying frequencies
        sin_osc = np.sum(np.sin(3 * x) * np.cos(7 * x) * np.exp(-0.05 * x**2))
        
        # Cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multimodal component with Gaussian peaks
        multimodal = 0.0
        for i in range(1, 6):
            center = np.full(self.dim, i * 0.5)
            multimodal += np.exp(-0.5 * np.sum((x - center)**2)) * np.sin(2 * np.pi * np.sum(x - center))
        
        # Add cubic and quartic terms for increased nonlinearity
        cubic = 0.05 * np.sum(x**3)
        quartic = 0.01 * np.sum(x**4)
        
        # Global scaling with distance from origin
        distance = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.2 * distance
        
        return radial + 0.8 * sin_osc + 0.3 * cross_term + 0.5 * multimodal + cubic + quartic + scaling