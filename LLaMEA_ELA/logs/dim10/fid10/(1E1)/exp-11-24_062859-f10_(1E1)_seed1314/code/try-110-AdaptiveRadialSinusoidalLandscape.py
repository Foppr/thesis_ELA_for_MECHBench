import numpy as np

class AdaptiveRadialSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for each dimension
        self.scaling = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with varying exponents
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 4) * self.scaling[i]
            
        # Sinusoidal modulation with adaptive frequencies
        for i in range(self.dim):
            result += 2.0 * np.sin(3.5 * x[i]) * np.cos(2.0 * x[i]) * self.scaling[i]
            
        # Radial basis functions with dynamic centers and widths
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(self.dim):
            rb_value = 0.0
            for j, center in enumerate(centers):
                width = 1.0 + 0.5 * np.sin(0.5 * i + j)
                rb_value += np.exp(-0.5 * ((x[i] - center) / width) ** 2)
            result += 1.5 * rb_value * self.scaling[i]
            
        # Cross-dimension coupling with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.8 + 0.2 * np.sin(0.3 * (i + j))
                result += coupling_strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Adaptive noise component
        noise_factor = 0.05 * np.mean(self.scaling)
        result += noise_factor * np.random.random()
        
        # Asymmetric penalty for large values
        penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                penalty += 0.3 * (np.abs(x[i]) - 3.0) ** 2.5
        result += penalty
        
        return result