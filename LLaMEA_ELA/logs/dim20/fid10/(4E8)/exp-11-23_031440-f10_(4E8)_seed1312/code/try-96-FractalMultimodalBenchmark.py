import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like self-similar structure using recursive scaling
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale sinusoidal components with varying frequencies and amplitudes
            scale = 2.0 ** (i % 4)
            freq = scale * np.pi
            amp = 1.0 / (1.0 + 0.1 * i)
            fractal_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Multi-scale basin structure with varying depth and width
        basin_term = 0.0
        for i in range(self.dim):
            # Different basin depths based on dimension index
            depth = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            # Quadratic basin with fractal scaling
            basin_term += depth * (x_norm[i] ** 2) * (1.0 + 0.3 * np.sin(3 * np.pi * x_norm[i]))
        
        # Multi-modal interference with varying phase shifts and frequencies
        modal_interference = 0.0
        for i in range(self.dim):
            freq = 2.0 + (i % 5)
            phase = i * np.pi / (self.dim * 2.0)
            amp = 1.0 / (1.0 + 0.2 * i)
            modal_interference += amp * np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[i])
        
        # Cross-dimensional coupling with fractal scaling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on dimension indices
                coupling_strength = 1.0 / (1.0 + 0.1 * (i + j))
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_term += coupling_strength * np.sin(2 * np.pi * dist) * np.cos(np.pi * dist)
        
        # Logarithmic conditioning with varying exponents
        log_conditioning = 0.0
        for i in range(self.dim):
            # Varying conditioning exponents based on dimension index
            exponent = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            log_conditioning += (x_norm[i] ** (2 + exponent)) * np.cos(2 * np.pi * x_norm[i])
        
        # Combine all terms with dynamic weighting based on dimension
        result = 0.5 * fractal_term + 0.3 * basin_term + 0.2 * modal_interference + \
                 0.1 * coupling_term + 0.4 * log_conditioning
        
        return result