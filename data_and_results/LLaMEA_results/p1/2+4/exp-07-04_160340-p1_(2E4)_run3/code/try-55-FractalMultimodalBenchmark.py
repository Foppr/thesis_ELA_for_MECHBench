import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x_norm = x / 5.0
        
        # Base quadratic term
        base = np.sum(x_norm**2)
        
        # Fractal-like sinusoidal components with varying frequencies and amplitudes
        fractal_sum = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            amp = 1.0 / (i + 1)
            fractal_sum += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Overlapping wave interference pattern
        wave_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                wave_sum += np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Dynamic global minimum based on dimensionality
        dynamic_min = np.sum(np.sin(np.pi * x_norm)**2)
        
        # Add a complex nested structure with exponentially decaying terms
        nested = 0.0
        for i in range(self.dim):
            nested += np.exp(-0.5 * (x_norm[i] - np.sin(np.pi * x_norm[i]))**2) * np.cos(10 * x_norm[i])
        
        # Combine all components
        result = base + 0.5 * fractal_sum + 0.3 * wave_sum + 0.2 * dynamic_min + 0.1 * nested
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result