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
            freq = 2 ** (i % 3 + 2)  # Slightly different frequency pattern
            scale = 1.0 / (1.0 + 0.15 * i)  # Adjusted scaling
            component = np.sin(freq * x[i]) * np.exp(-0.1 * np.abs(x[i])) * scale
            result += 0.25 * component**2  # Reduced weight
        
        # Trigonometric coupling with fractal phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.5) * np.cos(np.pi * (x[i] - x[i+1]) / 3.5)  # Modified phases
            coupling = np.sin(4.5 * (x[i] - x[i+1])) * phase_mod  # Slightly different frequency
            result += 0.35 * coupling**2  # Reduced weight
        
        # Multi-scale fractal-like ridge structures with self-similarity
        for i in range(self.dim):
            ridge_freqs = [4, 8, 12, 16]  # Changed frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.015 * (freq - 10)**2)  # Adjusted decay
            result += 0.55 * ridge_sum**2  # Slightly reduced weight
        
        # Exponentially weighted long-range interactions with scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.25 * np.abs(i - j))  # Different weighting
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.18 * interaction_sum  # Reduced weight
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.25 * np.tanh(curvature)  # Slightly reduced conditioning
        result *= conditioning
        
        # Asymmetric basin structure with polynomial symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 4) * np.sin(0.25 * x[i])  # Different coefficient
        result += 0.13 * asymmetry  # Slightly reduced asymmetry
        
        # Final fractal normalization and noise sensitivity
        result /= self.dim
        result += 0.025 * np.sum(np.abs(x)**3) / self.dim  # Reduced noise component
        
        return result