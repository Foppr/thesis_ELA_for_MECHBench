import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced exponentially decaying sinusoidal components with modified scaling
        for i in range(self.dim):
            freq = 2 ** (i % 5 + 1)
            scale = 1.0 / (1.0 + 0.15 * i)
            component = np.sin(freq * x[i]) * np.exp(-0.12 * np.abs(x[i])) * scale
            result += 0.35 * component**2
        
        # Modified trigonometric coupling with enhanced phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2) * np.cos(np.pi * (x[i] - x[i+1]) / 4)
            coupling = np.sin(6 * (x[i] - x[i+1])) * phase_mod
            result += 0.45 * coupling**2
        
        # Refined fractal-like ridge structures with adaptive frequency weights
        for i in range(self.dim):
            ridge_freqs = [4, 8, 12, 16]
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.015 * (freq - 10)**2)
            result += 0.55 * ridge_sum**2
        
        # Adjusted long-range interactions with modified weighting scheme
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.25 * np.abs(i - j))
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.18 * interaction_sum
        
        # Improved adaptive conditioning with enhanced curvature detection
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2 + 0.1 * np.sin(2*x[i])
        conditioning = 1.0 + 0.25 * np.tanh(curvature)
        result *= conditioning
        
        # Enhanced asymmetric basin structure with polynomial symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.25 * x[i]) + 0.3 * x[i]**3
        result += 0.18 * asymmetry
        
        # Improved fractal normalization and noise sensitivity
        result /= self.dim
        result += 0.025 * np.sum(np.abs(x)**2.5) / self.dim
        
        return result