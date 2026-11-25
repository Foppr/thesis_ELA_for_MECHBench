import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        # Fractal structure with recursive scaling
        for i in range(self.dim):
            # Power-law scaling with fractal dimension
            scale_factor = np.power(np.abs(x_norm[i]) + 1e-8, 0.33)
            
            # Sinusoidal components with multi-scale frequencies
            freq1 = 2 * np.pi * (i + 1) * (1 + 0.5 * np.sin(x_norm[i] * np.pi))
            freq2 = 4 * np.pi * (i + 1) * (1 + 0.3 * np.cos(x_norm[i] * np.pi / 2))
            
            # Recursive dimension coupling with fractal pattern
            coupling = 1.0
            for j in range(i):
                coupling *= (1 + 0.1 * np.sin(x_norm[j] * (j + 1) * np.pi / (i + 1)))
            
            # Multi-scale sinusoidal modulation
            term1 = np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i])
            term2 = np.sin(freq1 * x_norm[i]**2) * np.cos(freq2 * x_norm[i]**3)
            
            # Combine with power-law scaling and coupling
            result += scale_factor * coupling * (term1 + 0.5 * term2)
        
        # Add self-similar fractal component
        fractal_component = 0.0
        for i in range(self.dim):
            # Recursive pattern with decreasing amplitude
            amp = 0.1 / (i + 1)
            freq = 2**(i % 4 + 1) * (1 + 0.2 * np.sin(i * np.pi / self.dim))
            fractal_component += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Combine main and fractal components with dynamic weighting
        weight_main = 0.6 + 0.4 * np.sin(self.dim * 0.2)
        weight_fractal = 0.4 + 0.6 * np.cos(self.dim * 0.15)
        
        return weight_main * result + weight_fractal * fractal_component