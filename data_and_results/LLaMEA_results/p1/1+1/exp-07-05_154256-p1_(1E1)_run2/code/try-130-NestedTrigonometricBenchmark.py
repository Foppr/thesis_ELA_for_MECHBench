import numpy as np

class NestedTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.base_freq = 2.0 * np.pi
        self.amplitude = 10.0
        self.poly_degree = 4
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize input to [-1, 1] for stable trigonometric evaluation
        x_norm = x / 5.0
        
        # Nested trigonometric components with varying frequencies
        nested_trig = 0.0
        for i in range(self.dim):
            freq = self.base_freq * (i + 1) * (1.0 + 0.5 * np.sin(x_norm[i]))
            nested_trig += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.3) + \
                          np.sin(freq * x_norm[i] * 0.7) * np.cos(freq * x_norm[i] * 0.5)
        
        # Radial polynomial terms with adaptive exponents
        r = np.sqrt(np.sum(x_norm**2))
        radial_poly = 0.0
        for i in range(1, self.poly_degree + 1):
            radial_poly += (i * 0.5) * (r**(i + 1)) * np.sin(self.base_freq * r * i)
        
        # Cross-dimensional coupling with sine modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_factor = np.sin(self.base_freq * x_norm[i] * x_norm[j])
                cross_coupling += coupling_factor * (x_norm[i]**2 + x_norm[j]**2)
        
        # Adaptive noise-like modulation based on position
        noise_mod = 0.0
        for i in range(self.dim):
            noise_mod += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Combine all components with weighted contributions
        result = (2.0 * nested_trig + 
                 1.5 * radial_poly + 
                 0.8 * cross_coupling + 
                 0.5 * noise_mod)
        
        # Apply global scaling and ensure positive fitness
        return np.abs(result) + 0.1 * np.sum(x**2)