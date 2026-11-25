import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying sinusoidal components with modified fractal scaling
        for i in range(self.dim):
            freq = 2 ** (i % 3 + 2)  # Changed from %4 to %3 and shifted by 2
            scale = 1.0 / (1.0 + 0.15 * i)  # Slightly different scaling
            component = np.sin(freq * x[i]) * np.exp(-0.12 * np.abs(x[i])) * scale  # Increased decay rate
            result += 0.35 * component**2  # Slightly increased weight
        
        # Trigonometric coupling with modified phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.5) * np.cos(np.pi * (x[i] - x[i+1]) / 2.8)  # Modified phases
            coupling = np.sin(6 * (x[i] - x[i+1])) * phase_mod  # Changed frequency from 5 to 6
            result += 0.35 * coupling**2  # Slightly reduced weight
        
        # Multi-scale fractal-like ridge structures with modified self-similarity
        for i in range(self.dim):
            ridge_freqs = [4, 8, 12, 16]  # Shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.03 * (freq - 12)**2)  # Changed decay rate and center
            result += 0.55 * ridge_sum**2  # Slightly reduced weight
        
        # Exponentially weighted long-range interactions with modified scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.25 * np.abs(i - j))  # Changed decay rate
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.18 * interaction_sum  # Slightly reduced weight
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.35 * np.tanh(curvature)  # Increased conditioning factor
        result *= conditioning
        
        # Asymmetric basin structure with modified symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 4) * np.sin(0.35 * x[i])  # Slightly increased coefficient
        result += 0.17 * asymmetry  # Slightly increased weight
        
        # Final fractal normalization and noise sensitivity
        result /= self.dim
        result += 0.035 * np.sum(np.abs(x)**3) / self.dim  # Slightly increased noise sensitivity
        
        return result