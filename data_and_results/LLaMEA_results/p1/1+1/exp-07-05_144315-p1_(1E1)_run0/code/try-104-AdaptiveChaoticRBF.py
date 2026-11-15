import numpy as np

class AdaptiveChaoticRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaos generation
        self.chaos_factor = 2.0 * np.pi / np.random.uniform(0.5, 2.0)
        
    def f(self, x):
        # Ensure bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive width
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, min(15, self.dim * 2))
        for i, center in enumerate(centers):
            if i < self.dim:
                rbf += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.1 * i))**2) * np.sin(2.0 * np.pi * x[i])
        
        # Sinusoidal wave component with varying frequencies
        wave = np.sum(np.sin(self.chaos_factor * x) * np.cos(1.5 * self.chaos_factor * x))
        
        # Polynomial chaos component with mixed degrees
        poly = np.sum(x**2 + 0.3 * x**3 + 0.05 * x**4)
        
        # Adaptive scaling based on distance from origin
        dist = np.sqrt(np.sum(x**2))
        scale = 1.0 + 0.2 * np.sin(0.5 * dist) + 0.1 * np.cos(0.3 * dist)
        
        # Cross-dimensional interaction terms
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                cross += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multimodal component with varying peak heights
        multimodal = 0.0
        for i in range(1, 8):
            height = 1.0 / (1.0 + 0.1 * i)
            multimodal += height * np.exp(-0.2 * np.sum((x - i * 0.5)**2)) * np.sin(3.0 * np.pi * np.sum(x - i * 0.5))
        
        # Chaotic modulation with time-varying parameters
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i] + np.sin(5 * x[i])) * np.cos(7 * x[i] + np.cos(3 * x[i]))
        
        # Fractional power component for additional complexity
        frac = 0.0
        for i in range(self.dim):
            frac += np.abs(x[i])**1.7 * np.sin(4 * x[i])
        
        # Combine all components with carefully tuned weights
        result = 0.5 * rbf + 0.7 * wave + 0.4 * poly + scale + 0.3 * cross + 0.6 * multimodal + 0.2 * chaotic + 0.25 * frac
        
        return result