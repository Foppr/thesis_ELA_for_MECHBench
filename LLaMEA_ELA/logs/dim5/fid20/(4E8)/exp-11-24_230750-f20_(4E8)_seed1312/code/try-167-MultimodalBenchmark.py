import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier regions to guide search towards feasible areas
        barriers = np.sum(1.0 / (1.0 + np.exp(-10.0 * (np.abs(x) - 4.0))))
        
        # Fractal-like multimodal structure using recursive sine-cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2.0**i * x[i]) * np.cos(3.0**i * x[i])
        
        # Adaptive ridge navigation with variable step sizes and curvature
        ridges = 0.0
        for i in range(self.dim - 1):
            step_size = 0.5 + 0.5 * np.sin(x[i] * 0.5)
            ridges += step_size * (x[i] - x[i+1])**2
        
        # Self-similar structure with multi-scale sinusoidal modulation
        multiscale = 0.0
        for scale in [1, 2, 4]:
            multiscale += np.sum(np.sin(scale * x) * np.cos(scale * x) * 
                               np.exp(-0.1 * np.abs(x)))
        
        # Mixed convex-concave regions with controlled curvature transitions
        mixed = np.sum((x**2 + 0.1 * x**4) * (1.0 + 0.3 * np.tanh(x)))
        
        # Combined function value with enhanced fitness landscape complexity
        return barriers + fractal + ridges + multiscale + mixed