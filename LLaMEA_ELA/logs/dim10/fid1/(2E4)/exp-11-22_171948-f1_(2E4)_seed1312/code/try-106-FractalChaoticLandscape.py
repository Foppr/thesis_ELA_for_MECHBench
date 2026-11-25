import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying sinusoidal components with modified scaling
        for i in range(self.dim):
            freq = 2 ** (i % 3 + 2)  # Changed from 1 to 2, and %4 to %3
            scale = 1.0 / (1.0 + 0.1 * i)  # Reduced scaling factor
            component = np.sin(freq * x[i]) * np.exp(-0.05 * np.abs(x[i])) * scale  # Reduced decay rate
            result += 0.3 * component**2
        
        # Trigonometric coupling with modified phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 3) * np.cos(np.pi * (x[i] - x[i+1]) / 4)  # Changed denominators
            coupling = np.sin(6 * (x[i] - x[i+1])) * phase_mod  # Increased frequency
            result += 0.4 * coupling**2
        
        # Multi-scale fractal-like ridge structures with modified self-similarity
        for i in range(self.dim):
            ridge_freqs = [3, 7, 11, 17]  # Changed frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.01 * (freq - 10)**2)  # Reduced decay rate
            result += 0.6 * ridge_sum**2
        
        # Exponentially weighted long-range interactions with modified scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.2 * np.abs(i - j))  # Reduced weight decay
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.2 * interaction_sum
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.2 * np.tanh(curvature)  # Reduced conditioning factor
        result *= conditioning
        
        # Asymmetric basin structure with modified symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 4) * np.sin(0.2 * x[i])  # Reduced frequency
        result += 0.15 * asymmetry
        
        # Final fractal normalization and noise sensitivity
        result /= self.dim
        result += 0.02 * np.sum(np.abs(x)**3) / self.dim  # Reduced noise term
        
        return result