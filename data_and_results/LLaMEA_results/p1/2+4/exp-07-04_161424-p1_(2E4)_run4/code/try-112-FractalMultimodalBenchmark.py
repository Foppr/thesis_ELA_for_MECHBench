import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = np.array([2**i for i in range(dim)])
        # Precompute wave frequencies
        self.frequencies = np.linspace(1, 10, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal wave component with self-similar structure
        fractal_waves = np.zeros(self.dim)
        for i in range(self.dim):
            freq = self.frequencies[i]
            scale = self.fractal_factors[i]
            fractal_waves[i] = np.sin(freq * x_norm[i] * scale) * np.cos(freq * x_norm[i] * scale)
        
        # Multiscale trigonometric interactions
        multiscale = np.sum(np.sin(self.frequencies * x_norm) * np.cos(self.frequencies * x_norm))
        
        # Adaptive conditioning based on input magnitude
        conditioning = 1 + 0.5 * np.sum(np.abs(x_norm)**3)
        
        # Self-similar fractal landscape with multiple peaks
        fractal_term = np.sum(fractal_waves**2 + 0.3 * np.sin(fractal_waves * np.pi))
        
        # Combine components with dynamic weights
        total = 0.4 * fractal_term + 0.3 * multiscale + 0.3 * conditioning
        
        # Add a global scaling factor to increase conditioning
        return total * (1 + 0.3 * np.sin(np.sum(x_norm**2) * 0.1))