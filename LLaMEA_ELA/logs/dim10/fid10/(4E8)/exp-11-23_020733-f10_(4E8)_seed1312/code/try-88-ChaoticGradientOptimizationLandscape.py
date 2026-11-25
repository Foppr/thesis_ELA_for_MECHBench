import numpy as np

class ChaoticGradientOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = 0.5 * np.sum(x**2)
        
        # Exponential potential fields with chaotic modulation
        for i in range(self.dim):
            # Chaotic modulation using logistic map-like behavior
            chaos_factor = 1.0 + 0.3 * np.sin(3.14159 * x[i]) * np.cos(2.718 * x[i])
            result += chaos_factor * np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i])**2
        
        # Asymmetric cubic interactions with dynamic coefficients
        for i in range(self.dim):
            # Dynamic coefficient based on position
            coeff = 1.0 + 0.5 * np.sin(x[i])
            result += coeff * x[i]**3 + 0.2 * x[i]**4
            
        # Multi-scale periodic modulation with varying frequencies
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 5.0]
            for freq in freqs:
                result += 0.15 * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with dynamic interaction strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Dynamic coupling strength based on position
                strength = 0.5 * (1 + np.tanh(x[i] + x[j]))
                result += strength * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Fractal-like noise with dynamic scaling
        noise = 0.05 * np.sum(np.sin(13 * x) + np.cos(11 * x) + np.tan(9 * x))
        result += noise
        
        # Add a global chaotic modulation factor
        chaos_mod = 1.0 + 0.2 * np.sin(np.sum(x**2)) * np.cos(np.sum(x))
        result *= chaos_mod
        
        return result