import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        result = 0.0
        
        # Recursive fractal pattern with multiple scales
        for i in range(self.dim):
            scale_factor = 2.0 ** (i % 4)
            amplitude = 1.0 / (1.0 + 0.5 * i)
            
            # Multi-scale sinusoidal components
            term1 = amplitude * np.sin(scale_factor * x_normalized[i])
            term2 = amplitude * np.cos(scale_factor * x_normalized[i] * 0.5)
            term3 = amplitude * np.sin(scale_factor * x_normalized[i] * 1.3)
            
            # Self-similar interaction between dimensions
            interaction = 0.0
            for j in range(i):
                freq = 3.0 ** (j % 3) * (1 + 0.1 * np.sin(j * 0.2))
                interaction += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[j])
            
            result += term1 + term2 + term3 + 0.3 * interaction
        
        # Add fractal-like curvature through polynomial interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                poly_term += (dist ** 3) * np.sin(5 * dist)
        
        # Add chaotic perturbations with varying intensity
        chaotic = 0.0
        for i in range(self.dim):
            freq = 7.0 + 2.0 * np.sin(i * 0.4)
            chaotic += np.sin(freq * x_normalized[i]) * np.exp(-0.1 * i)
        
        return 0.5 * result + 0.3 * poly_term + 0.2 * chaotic