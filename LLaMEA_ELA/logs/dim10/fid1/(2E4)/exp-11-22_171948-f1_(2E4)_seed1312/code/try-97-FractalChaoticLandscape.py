import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced exponentially decaying sinusoidal components with improved fractal scaling
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 1)
            scale = 1.0 / (1.0 + 0.1 * i)
            component = np.sin(freq * x[i]) * np.exp(-0.08 * np.abs(x[i])) * scale
            result += 0.35 * component**2
        
        # Refined trigonometric coupling with adaptive phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2) * np.cos(np.pi * (x[i] - x[i+1]) / 4)
            coupling = np.sin(6 * (x[i] - x[i+1])) * phase_mod
            result += 0.35 * coupling**2
        
        # Enhanced multi-scale fractal-like ridge structures with improved self-similarity
        for i in range(self.dim):
            ridge_freqs = [4, 8, 12, 16, 20]
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.015 * (freq - 12)**2)
            result += 0.55 * ridge_sum**2
        
        # Improved long-range interactions with adaptive weighting
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.25 * np.abs(i - j))
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.25 * interaction_sum
        
        # Enhanced adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.25 * np.tanh(curvature)
        result *= conditioning
        
        # Improved asymmetric basin structure with stronger symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.25 * x[i])
        result += 0.18 * asymmetry
        
        # Final fractal normalization and refined noise sensitivity
        result /= self.dim
        result += 0.025 * np.sum(np.abs(x)**3) / self.dim
        
        return result