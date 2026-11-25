import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractal-like multimodal components with self-similarity
        for i in range(self.dim):
            # Multi-scale sinusoidal components with varying frequencies
            freq = 2 ** (i % 3 + 1)
            amp = 0.5 / (i + 1)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
            
        # Exponential decay interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimensional interactions
                distance = np.abs(x[i] - x[j])
                result += 0.2 * np.exp(-distance) * (x[i]**2 + x[j]**2)
                
        # Dynamic scaling with fractal dimension characteristics
        scale_factor = 1.0
        for i in range(self.dim):
            scale_factor *= (1.0 + 0.1 * np.sin(0.5 * x[i]))
            
        # Multi-modal structure with varying local minima heights
        for i in range(self.dim):
            result += 0.3 * np.sin(4 * x[i]) * np.cos(6 * x[i]) * scale_factor
            
        # Asymmetric penalty terms that create complex basin boundaries
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.15 * (x[i] - 2)**4
            else:
                result += 0.15 * (x[i] + 2)**4
                
        # Self-similar structure with recursive scaling
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.05 * np.sin(8 * x[i]) * np.exp(-0.02 * x[i]**2)
            else:
                result += 0.05 * np.cos(8 * x[i]) * np.exp(-0.02 * x[i]**2)
                
        return result