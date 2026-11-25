import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced exponentially decaying sinusoidal components with increased fractal complexity
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 3)  # Increased frequency range
            scale = 1.0 / (1.0 + 0.2 * i)  # Stronger scaling
            component = np.sin(freq * x[i]) * np.exp(-0.15 * np.abs(x[i])) * scale
            result += 0.4 * component**2  # Increased weight
        
        # Stronger chaotic trigonometric coupling with altered phase relationships
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.0) * np.cos(np.pi * (x[i] - x[i+1]) / 3.0)
            coupling = np.sin(7 * (x[i] - x[i+1])) * phase_mod  # Increased frequency
            result += 0.4 * coupling**2  # Increased weight
        
        # Multi-scale fractal-like ridge structures with enhanced self-similarity
        for i in range(self.dim):
            ridge_freqs = [3, 6, 9, 15, 20]  # Expanded and shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.04 * (freq - 15)**2)
            result += 0.6 * ridge_sum**2  # Increased weight
        
        # Enhanced long-range interactions with stronger exponential decay
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.3 * np.abs(i - j))  # Stronger decay
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.2 * interaction_sum  # Increased weight
        
        # Enhanced adaptive conditioning with stronger curvature effects
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**3  # Increased nonlinearity
        conditioning = 1.0 + 0.4 * np.tanh(curvature)  # Stronger conditioning factor
        result *= conditioning
        
        # Enhanced asymmetric basin structure with stronger symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.4 * x[i])  # Increased power and coefficient
        result += 0.2 * asymmetry  # Increased weight
        
        # Final fractal normalization with enhanced noise sensitivity
        result /= self.dim
        result += 0.05 * np.sum(np.abs(x)**3) / self.dim  # Increased noise sensitivity
        
        return result