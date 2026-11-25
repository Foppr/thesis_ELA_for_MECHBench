import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive scaling
        result = 0.1 * np.sum(x**4)
        
        # Multi-modal exponential peaks with varying heights
        peak_heights = 3.0 + 2.0 * np.sin(np.arange(self.dim) * 0.5)
        for i in range(self.dim):
            result += peak_heights[i] * np.exp(-0.5 * (x[i] - 2.0)**2) + \
                      peak_heights[i] * np.exp(-0.5 * (x[i] + 2.0)**2)
        
        # Trigonometric interference pattern with dynamic frequencies
        freqs = 1.0 + 0.5 * np.sin(np.arange(self.dim) * 0.3)
        for i in range(self.dim):
            result += 1.2 * np.sin(freqs[i] * x[i]) * np.cos(freqs[i] * x[i])
        
        # Cross-dimensional coupling with distance-dependent interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                result += 0.8 * np.exp(-dist) * np.sin(3 * (x[i] + x[j]))
        
        # Asymmetric polynomial with adaptive exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * x[i]**(2.5 + 0.3 * np.sin(i))
            else:
                result += 0.3 * x[i]**(3.5 + 0.2 * np.cos(i))
        
        # Adaptive noise component with dimensionality scaling
        noise_scale = 0.01 * self.dim
        result += noise_scale * np.random.random()
        
        return result