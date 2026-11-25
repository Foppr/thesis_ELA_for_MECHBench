import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Rotation-invariant base structure with polynomial decay
        base_decay = np.exp(-np.sum(x**2) / (2 * self.dim))
        
        # Multiple interacting sinusoidal waves with varying frequencies and amplitudes
        sin_waves = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sin_waves += np.sin(2 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Fractal-like nested structure with exponential scaling
        fractal = 0.0
        for k in range(1, 6):
            scale = 2**k
            fractal += np.sum(np.sin(scale * x) * np.cos(scale * x)) / (self.dim * k)
        
        # Polynomial interaction terms with chaotic coefficients
        poly_interaction = 0.0
        coeffs = [0.5, 0.3, 0.7, 0.2, 0.8]
        for i in range(self.dim):
            poly_interaction += coeffs[i % len(coeffs)] * x[i]**4 + (i+1) * np.sin(x[i])**2
        
        # Chaotic radial component with multiple frequencies
        radius = np.sqrt(np.sum(x**2))
        chaotic_radial = 0.5 * np.sin(10 * radius) * np.cos(7 * radius) * np.exp(-radius / 3)
        
        # Cross-dimensional coupling with rotation matrix elements
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(x[i] * x[j]) * np.cos(2 * x[i] + x[j])
        
        # Nested exponential decay with chaotic modulation
        nested_decay = 0.0
        for k in range(1, 4):
            nested_decay += np.exp(-np.sum((x - k)**2) / (2 * self.dim)) * np.sin(k * radius)
        
        # Combine all components
        result = base_decay * (sin_waves + fractal + poly_interaction + chaotic_radial + 
                              coupling + nested_decay)
        
        # Add a global minimum at origin with chaotic modulation
        result += 0.1 * np.sum(np.sin(x) * np.cos(2 * x) * np.exp(-x**2)) / self.dim
        
        return float(result)