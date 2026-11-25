import numpy as np

class FractalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced fractal sinusoidal components with chaotic frequency modulation
        for i in range(self.dim):
            freq = 3 ** (i % 5 + 2)  # Increased base and exponent
            scale = 1.0 / (1.0 + 0.3 * i)  # Strengthened scaling
            component = np.sin(freq * x[i]) * np.exp(-0.2 * np.abs(x[i])) * scale
            result += 0.5 * component**2  # Increased weight
        
        # Complex trigonometric coupling with chaotic phase interactions
        for i in range(self.dim - 1):
            phase_mod = np.sin(np.pi * (x[i] + x[i+1]) / 1.5) * np.cos(np.pi * (x[i] - x[i+1]) / 2.5)
            coupling = np.sin(8 * (x[i] - x[i+1])) * phase_mod * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
            result += 0.4 * coupling**2  # Increased weight
        
        # Multi-scale fractal ridge structures with chaotic frequency shifts
        for i in range(self.dim):
            ridge_freqs = [2, 5, 9, 13, 17]  # Further shifted frequencies
            ridge_sum = 0.0
            for freq in ridge_freqs:
                ridge_sum += np.sin(freq * x[i]) * np.exp(-0.05 * (freq - 10)**2)
            result += 0.7 * ridge_sum**2  # Increased weight
        
        # Long-range interactions with chaotic decay rates and enhanced coupling
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = np.exp(-0.4 * np.abs(i - j)) * (1 + 0.1 * np.sin(i * j))  # Chaotic weight modulation
                    interaction_sum += weight * (x[i] - x[j])**2
            result += 0.3 * interaction_sum  # Increased weight
        
        # Adaptive conditioning with chaotic curvature modulation
        curvature = 0.0
        for i in range(self.dim):
            curvature += np.abs(np.cos(x[i])) + np.sin(x[i])**3  # Increased exponent
        conditioning = 1.0 + 0.5 * np.tanh(curvature) * (1 + 0.2 * np.sin(np.sum(x)))  # Chaotic conditioning
        result *= conditioning
        
        # Asymmetric basin structure with chaotic symmetry breaking
        asymmetry = 0.0
        for i in range(self.dim):
            asymmetry += (x[i] ** 5) * np.sin(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)  # Increased coefficient and decay
        result += 0.3 * asymmetry  # Increased weight
        
        # Final fractal normalization with enhanced chaotic noise sensitivity
        result /= self.dim
        result += 0.06 * np.sum(np.abs(x)**4) / self.dim  # Further increased noise sensitivity
        
        return result