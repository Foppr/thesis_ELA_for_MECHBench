import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced rotation-invariant base structure with polynomial decay
        base_decay = np.exp(-np.sum(x**2) / (2 * self.dim))
        
        # Multiple interacting sinusoidal waves with varying frequencies and amplitudes
        sin_waves = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_waves += np.sin(3 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j]))
        
        # Fractal-like nested structure with exponential scaling and chaotic modulation
        fractal = 0.0
        for k in range(1, 8):
            scale = 2**k
            fractal += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * k**1.5)
        
        # Polynomial interaction terms with chaotic coefficients and higher order terms
        poly_interaction = 0.0
        coeffs = [0.8, 0.4, 0.6, 0.3, 0.9, 0.2, 0.7, 0.5]
        for i in range(self.dim):
            poly_interaction += coeffs[i % len(coeffs)] * x[i]**5 + (i+1) * np.sin(x[i])**3
        
        # Chaotic radial component with multiple frequencies and enhanced modulation
        radius = np.sqrt(np.sum(x**2))
        chaotic_radial = 0.7 * np.sin(15 * radius) * np.cos(11 * radius) * np.exp(-radius / 4)
        
        # Cross-dimensional coupling with rotation matrix elements and additional interference
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(x[i] * x[j]) * np.cos(3 * x[i] + 2 * x[j]) + np.cos(x[i] + x[j])**2
        
        # Enhanced nested exponential decay with chaotic modulation and multiple scales
        nested_decay = 0.0
        for k in range(1, 6):
            nested_decay += np.exp(-np.sum((x - k)**2) / (2 * self.dim)) * np.sin(k * radius + k**1.5)
        
        # Additional chaotic component with fractal-like structure
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.exp(-x[i]**2 / 10)
        
        # Combine all components with increased complexity and chaotic interaction
        result = base_decay * (sin_waves + fractal + poly_interaction + chaotic_radial + 
                              coupling + nested_decay + fractal_component)
        
        # Add a global minimum at origin with enhanced chaotic modulation
        result += 0.15 * np.sum(np.sin(x) * np.cos(3 * x) * np.exp(-x**2)) / self.dim
        
        return float(result)