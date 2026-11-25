import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        # Precompute fractal parameters
        self.fractal_dims = np.random.uniform(1.0, 2.5, dim)
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Fractal component using iterated function system
        fractal_sum = 0.0
        for i in range(self.dim):
            # Apply a fractal transformation with varying dimension
            dim_factor = self.fractal_dims[i]
            x_i = x_norm[i]
            
            # Use a combination of power and trigonometric functions to create fractal-like behavior
            term1 = np.abs(x_i) ** (dim_factor + 0.5)
            term2 = np.sin(np.pi * x_i ** 2) * np.cos(np.pi * x_i)
            term3 = np.exp(-x_i**2 / 2) * np.sin(5 * x_i)
            
            fractal_sum += term1 + term2 + term3
            
        # Multi-scale sinusoidal modulation with varying frequencies
        mod_sum = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1) * (1 + 0.5 * np.sin(i))
            amp = 1.0 + 0.3 * np.cos(i * np.pi / self.dim)
            mod_sum += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
            
        # Chaotic noise injection with logistic map
        noise_sum = 0.0
        r = 3.95  # Chaos parameter
        for i in range(self.dim):
            # Generate chaotic sequence using logistic map
            x_prev = x_norm[i]
            x_next = r * x_prev * (1 - x_prev)
            noise_sum += self.noise_levels[i] * np.sin(10 * x_next) * np.cos(5 * x_next)
            
        # Cross-dimensional interactions with fractal coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                coupling = np.sin(np.pi * x_norm[i] * x_norm[j] * (i+j+1))
                cross_sum += coupling * (x_norm[i]**2 + x_norm[j]**2) * (1 + 0.1 * i * j)
                
        # Combine components with dynamic weights
        weight_fractal = 0.5 + 0.2 * np.sin(self.dim * np.pi / 6)
        weight_mod = 0.3 + 0.1 * np.cos(self.dim * np.pi / 4)
        weight_noise = 0.1 + 0.05 * np.sin(self.dim * np.pi / 3)
        weight_cross = 0.2 + 0.1 * np.cos(self.dim * np.pi / 5)
        
        return (weight_fractal * fractal_sum + 
                weight_mod * mod_sum + 
                weight_noise * noise_sum + 
                weight_cross * cross_sum)