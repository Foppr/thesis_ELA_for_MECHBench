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
            freq = 2 ** (i % 6 + 1)  # Changed from %5 to %6 and shifted by 1
            scale = 1.0 / (1.0 + 0.4 * i)  # Increased scaling factor
            component = np.sin(freq * x[i]) * np.exp(-0.3 * np.abs(x[i])) * scale  # Slightly increased decay rate
            result += 0.6 * component**2  # Increased weight
        
        # Trigonometric coupling with enhanced phase modulation
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 2.0) * np.cos(np.pi * (x[i] - x[i+1]) / 3.0)  # Enhanced phases
            coupling = np.sin(9 * (x[i] - x[i+1])) * phase_mod  # Changed frequency from 8 to 9
            result += 0.55 * coupling**2  # Slightly increased weight
        
        # Multi-scale fractal-like ridge structures with enhanced self-similarity
        for i in range(self.dim):
            ridge_freqs = [3, 7, 11, 15, 19]  # Shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.07 * (freq - 12)**2)  # Changed decay rate and center
            result += 0.85 * ridge_sum**2  # Slightly increased weight
        
        # Exponentially weighted long-range interactions with enhanced scaling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.55 * np.abs(i - j))  # Slightly increased decay rate
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.45 * interaction_sum  # Slightly increased weight
        
        # Adaptive conditioning based on local curvature and dimensionality
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**3  # Changed to cubic term
        conditioning = 1.0 + 0.65 * np.tanh(curvature)  # Slightly increased conditioning factor
        result *= conditioning
        
        # Asymmetric basin structure with enhanced symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 6) * np.sin(0.6 * x[i])  # Increased power and coefficient
        result += 0.45 * asymmetry  # Slightly increased weight
        
        # Additional chaotic noise injection with enhanced sensitivity
        chaos_noise = 0.0
        for i in range(self.dim):
            chaos_noise += np.sin(15 * x[i]) * np.cos(19 * x[i]) * np.exp(-0.13 * np.abs(x[i]))
        result += 0.35 * chaos_noise**2  # Slightly increased weight
        
        # Final fractal normalization and enhanced noise sensitivity
        result /= self.dim
        result += 0.09 * np.sum(np.abs(x)**5) / self.dim  # Slightly increased noise sensitivity
        
        return result