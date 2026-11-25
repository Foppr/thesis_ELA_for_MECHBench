import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponentially decaying sinusoidal components with enhanced fractal scaling
        for i in range(self.dim):
            freq = 2 ** (i % 4 + 1)  # Changed from %3 to %4 and shifted by 1
            scale = 1.0 / (1.0 + 0.2 * i)  # Increased scaling factor
            component = np.sin(freq * x[i]) * np.exp(-0.15 * np.abs(x[i])) * scale  # Increased decay rate
            result += 0.4 * component**2  # Increased weight
        
        # Trigonometric coupling with enhanced phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.0) * np.cos(np.pi * (x[i] - x[i+1]) / 3.0)  # Enhanced phases
            coupling = np.sin(7 * (x[i] - x[i+1])) * phase_mod  # Changed frequency from 6 to 7
            result += 0.3 * coupling**2  # Reduced weight
        
        # Multi-scale fractal-like ridge structures with enhanced self-similarity
        for i in range(self.dim):
            ridge_freqs = [3, 7, 11, 15]  # Shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.04 * (freq - 9)**2)  # Changed decay rate and center
            result += 0.6 * ridge_sum**2  # Increased weight
        
        # Exponentially weighted long-range interactions with enhanced scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.3 * np.abs(i - j))  # Increased decay rate
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.2 * interaction_sum  # Increased weight
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**2
        conditioning = 1.0 + 0.4 * np.tanh(curvature)  # Increased conditioning factor
        result *= conditioning
        
        # Asymmetric basin structure with enhanced symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 4) * np.sin(0.4 * x[i])  # Increased coefficient
        result += 0.2 * asymmetry  # Increased weight
        
        # Final fractal normalization and enhanced noise sensitivity
        result /= self.dim
        result += 0.04 * np.sum(np.abs(x)**3) / self.dim  # Increased noise sensitivity
        
        return result