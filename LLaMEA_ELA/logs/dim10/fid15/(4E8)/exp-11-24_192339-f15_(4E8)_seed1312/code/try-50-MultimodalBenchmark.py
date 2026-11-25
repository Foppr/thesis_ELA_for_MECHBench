import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic modulation
        rbf = 0
        for i in range(self.dim):
            # Chaotic sinusoidal modulation with radial basis
            rbf += np.exp(-np.sum((x - 3 * np.sin(0.5 * x))**2) / (2 * self.dim))
        
        # Sinusoidal multimodal component with dynamic frequency
        sin_mod = 0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x[i] * 0.7)
            sin_mod += np.sin(freq * x[i])**2 + 0.5 * np.cos(4 * x[i]) * np.sin(2 * x[i])
        
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying interaction based on distance
                dist = np.abs(x[i] - x[j])
                cross_interaction += np.exp(-dist) * (x[i]**2 + x[j]**2)
        
        # Adaptive difficulty scaling
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.25)
        
        # Combine all components with dynamic weighting
        return scale_factor * (0.8 * rbf + 1.2 * sin_mod + 0.5 * cross_interaction)