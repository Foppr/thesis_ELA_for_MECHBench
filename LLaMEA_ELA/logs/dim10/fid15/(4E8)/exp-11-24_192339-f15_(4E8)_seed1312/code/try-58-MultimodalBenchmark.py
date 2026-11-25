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
            # Sine-based modulation with Gaussian decay
            rbf += np.exp(-np.sum((x - 2 * np.sin(0.3 * x))**2) / (2 * self.dim))
        
        # Sinusoidal multimodal component with dynamic frequency
        sin_mod = 0
        for i in range(self.dim):
            freq = 1.5 + 2.5 * np.sin(x[i] * 0.8)
            sin_mod += np.sin(freq * x[i])**3 + 0.7 * np.cos(3 * x[i]) * np.sin(3 * x[i])
        
        # Cross-dimensional interaction with polynomial decay
        cross_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Polynomially decaying interaction based on distance
                dist = np.abs(x[i] - x[j])
                cross_interaction += (1 / (1 + dist**2)) * (x[i]**3 + x[j]**3)
        
        # Global shift to enhance complexity
        global_shift = 0.5 * np.sum(np.sin(0.4 * x))
        
        # Adaptive difficulty scaling
        scale_factor = 1.0 + 0.4 * np.sin(self.dim * 0.3)
        
        # Combine all components with dynamic weighting
        return scale_factor * (0.9 * rbf + 1.1 * sin_mod + 0.6 * cross_interaction) + global_shift