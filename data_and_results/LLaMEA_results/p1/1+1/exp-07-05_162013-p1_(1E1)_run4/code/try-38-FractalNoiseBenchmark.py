import numpy as np

class FractalNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.5  # Fractal dimension parameter
        self.noise_level = 0.5  # Adaptive noise level
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal component using box-counting approximation
        for i in range(self.dim):
            # Scale x to [0, 1] for fractal generation
            scaled_x = (x[i] + 5.0) / 10.0
            # Generate fractal-like pattern using sine waves with decreasing frequencies
            fractal_term = 0.0
            for k in range(1, 11):
                fractal_term += (1.0 / (k ** self.fractal_dim)) * np.sin(k ** 2 * np.pi * scaled_x)
            result += fractal_term ** 2
            
        # Multi-scale harmonic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling with varying frequency ratios
                freq_ratio = (i + 1) / (j + 1)
                coupling = np.sin(freq_ratio * x[i]) * np.cos(freq_ratio * x[j])
                result += 0.3 * coupling ** 2
                
        # Adaptive noise component
        noise = np.random.normal(0, self.noise_level, self.dim)
        result += 0.2 * np.sum((x + noise) ** 2)
        
        # Sharp irregularity using absolute value and step functions
        for i in range(self.dim):
            result += 0.1 * np.abs(x[i]) ** 1.5
            
        # Global scaling and offset
        result = result * (1.0 + 0.1 * np.sum(x ** 2))
        
        return result