import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying sinusoidal components with fractal scaling
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)
            scale = 1.0 / (1.0 + 0.2 * i)
            component = np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i])) * scale
            result += 0.3 * component**2
        
        # Trigonometric coupling with fractal phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2) * np.cos(np.pi * (x[i] - x[i+1]) / 3)
            coupling = np.sin(5 * (x[i] - x[i+1])) * phase_mod
            result += 0.4 * coupling**2
        
        # Multi-scale fractal-like ridge structures with self-similarity
        for i in range(self.dim):
            ridge_freqs = [5, 10, 15, 20]
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.02 * (freq - 10)**2)
            result += 0.6 * ridge_sum**2
        
        # Exponentially weighted long-range interactions with scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.3 * np.abs(i - j))
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.2 * interaction_sum
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.3 * np.tanh(curvature)
        result *= conditioning
        
        # Asymmetric basin structure with polynomial symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 4) * np.sin(0.3 * x[i])
        result += 0.15 * asymmetry
        
        # Final fractal normalization and noise sensitivity
        result /= self.dim
        result += 0.03 * np.sum(np.abs(x)**3) / self.dim
        
        return result