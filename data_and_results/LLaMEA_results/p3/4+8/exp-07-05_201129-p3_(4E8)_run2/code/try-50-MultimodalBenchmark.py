import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            # Use a fractal-like pattern with increasing frequency
            freq = 2**(i % 4 + 1)
            amp = 1.0 / (i + 1)
            fractal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Scale-dependent conditioning
        scale_cond = 0.0
        for i in range(self.dim):
            scale_cond += (x_normalized[i]**2) * (1.0 + 0.5 * np.abs(x_normalized[i]))
        
        # Radial fractal with multiple scales
        r = np.sqrt(np.sum(x_normalized**2))
        radial_fractal = r * (1.0 + 0.3 * np.sin(5 * r) * np.cos(3 * r) * np.sin(7 * r))
        
        # Multi-scale sinusoidal interaction
        multi_scale = 0.0
        for i in range(1, min(5, self.dim + 1)):
            freq = 3**i
            amp = 1.0 / (i * 3)
            multi_scale += amp * np.sin(freq * x_normalized[i-1]) * np.cos(freq * r)
        
        # Global minimum at origin with enhanced local optima
        return 0.5 * fractal + 0.3 * scale_cond + 0.2 * radial_fractal + 0.1 * multi_scale + 1.0