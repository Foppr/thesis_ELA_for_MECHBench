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
            freq = 2 ** (i % 3 + 2)
            scale = 1.0 / (1.0 + 0.3 * i)
            component = np.sin(freq * x[i]) * np.exp(-0.15 * np.abs(x[i])) * scale
            result += 0.4 * component**2
        
        # Trigonometric coupling with modified phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 3) * np.cos(np.pi * (x[i] - x[i+1]) / 4)
            coupling = np.sin(6 * (x[i] - x[i+1])) * phase_mod
            result += 0.5 * coupling**2
        
        # Enhanced fractal-like ridge structures with increased frequency diversity
        for i in range(self.dim):
            ridge_freqs = [3, 7, 11, 17]
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.03 * (freq - 10)**2)
            result += 0.7 * ridge_sum**2
        
        # Modified long-range interactions with stronger dimensionality dependence
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.4 * np.abs(i - j))
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.3 * interaction_sum
        
        # Enhanced adaptive conditioning with modified curvature terms
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**3
        conditioning = 1.0 + 0.4 * np.tanh(curvature)
        result *= conditioning
        
        # Increased asymmetry with polynomial terms of higher degree
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.4 * x[i])
        result += 0.2 * asymmetry
        
        # Final normalization and modified noise sensitivity
        result /= self.dim
        result += 0.04 * np.sum(np.abs(x)**4) / self.dim
        
        return result